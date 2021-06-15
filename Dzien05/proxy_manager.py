import requests

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