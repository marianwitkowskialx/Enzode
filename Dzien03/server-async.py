
# Prosty serwer TCP z wykorzystanie asyncio

import asyncio, socket
import os

filename = "c:\\tmp\\flik.txt"
filename = r"c:\tmp\flik.txt"
filename = "c:/tmp/flik.txt"


async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = ""
    while True:
        ch = (await loop.sock_recv(client, 255)).decode("utf-8")
        request += ch

        if ch!=os.linesep:
            continue

        request = request.strip()
        if request=="quit":
            break
        respose = request[::-1] + os.linesep
        await loop.sock_sendall(client, respose.encode('utf-8') )
    client.close()

async def run_server():
    server = socket.socket()
    server.bind( ('localhost', 8888) )
    server.listen()
    server.setblocking(False)

    loop = asyncio.get_event_loop()
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))

asyncio.run(run_server())