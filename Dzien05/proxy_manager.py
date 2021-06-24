import requests
import asyncio
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class ProxyManager:
    def __init__(self, db, proxy_list_url):
        self._db = db
        self._coll = self._db["proxies"]
        self._proxy_list_url = proxy_list_url

    async def set(self):
        try:
            r = requests.get(self._proxy_list_url)
        except Exception as exc:
            return False
        lines = r.text.split("\n")
        for line in lines:
            items = line.strip().split(" ")
            if len(items)<3 or (not ":" in items[0]) :
                continue
            ip_addr, port = items[0].split(":")
            port = int(port)
            country = items[1].split("-")[0]
            is_https = False
            if items[1][-1]=="S":
                is_https = True

            query = {"proxy_server" : items[0]}
            res = await self._coll.find_one(query)
            if res:
                if items[2]=='-':
                    await self._coll.delete_one(query)
                continue

            if items[2]=="+":
                data = {
                    "proxy_server" : items[0],
                    "https" : is_https,
                    "country" : country,
                    "status_check" : 0
                }
                await self._coll.insert_one(data)
        return True

    def validate_proxy(self, row):
        """
        Pobiera testowy URL z wykorzystaniem serwera proxy
        """
        if not row.get("proxy_server"):
            return
        if row.get("https", False):
            url = "https://lumtest.com/myip.json"
        else:
            url = "http://lumtest.com/myip.json"
        status, latency, response, response_code, last_alive = [None]*5
        print(f"Checcking {row.get('proxy_server')}.....")
        try:
            _proxies = {
                "http" : f"http://{row.get('proxy_server')}",
                "https" : f"https://{row.get('proxy_server')}",
            }
            ts1 = time.monotonic()
            r = requests.get(url, proxies=_proxies, timeout=(5, 30) )
            ts2 = time.monotonic()
            latency, response, response_code = ts2-ts1, r.text, r.status_code
            if response_code==200:
                status = 1
                last_alive = datetime.utcnow()
        except requests.exceptions.HTTPError as exc:
            status = -1
        except requests.exceptions.ProxyError as exc:
            status = -2
        except requests.exceptions.Timeout as exc:
            status = -3
        except requests.exceptions.ConnectionError as exc:
            status = -4
        except Exception as exc:
            status = -5

        status_data = {
            "status_check" : status,
            "http_code" : response_code,
            "latency" : latency,
            "response" : response,
            "last_check" : datetime.utcnow(),
            "last_alive" : last_alive
        }
        values = { "$set" : status_data }
        return row.get("proxy_server"),  values


    async def check(self):
        """checking state of proxy servers
        """
        print("check proxy status...")
        docs = await self._coll.find({}, {"_id":0}).to_list(20)
        # uruchamianie puli wątków w celu równoległego sprawdzania statusu proxy
        with ThreadPoolExecutor(max_workers=10) as pool:
            loop = asyncio.get_running_loop()
            futures = [
                loop.run_in_executor(pool, self.validate_proxy, doc)
                for doc in docs
            ]
            try:
                results = await asyncio.gather(*futures, return_exceptions=False)
            except Exception as exc:
                raise
        for server, values in results:
            cond = {"proxy_server": server}
            print(cond)
            await self._coll.update_one(cond, values)
