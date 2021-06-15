
# Proxychecker

from fastapi import FastAPI
import motor.motor_tornado
import uvicorn
from proxy_manager import ProxyManager
import asyncio

def get_db_conn():
    client = motor.motor_tornado.MotorClient("mongodb://18.156.117.57:27017/")
    return client["mar_wit"]

db_conn = get_db_conn()
proxy = ProxyManager(db_conn, "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt")
app = FastAPI()

@app.on_event("startup")
async def boot():
    await asyncio.sleep(5)
    asyncio.create_task(proxy.set())

if __name__ == "__main__":
    uvicorn.run("proxychecker:app", port=8000, reload=True)