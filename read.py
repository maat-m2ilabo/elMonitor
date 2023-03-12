import asyncio


async def read(websocket, path):
    file = await websocket.recv()

    f = open(file, 'r')
    currentread = f.read()
    await websocket.send(currentread)
    while True:
        f.seek(0)
        newread = f.read()
        if currentread != newread:
            currentread = newread
            await websocket.send(currentread)
        await asyncio.sleep(0.3)
