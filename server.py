import asyncio
import websockets
import read

async def start_server():
    async with websockets.serve(read.read, "localhost", 8000):
        await asyncio.Future()

asyncio.run(start_server())
