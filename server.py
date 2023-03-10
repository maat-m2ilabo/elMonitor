import asyncio
import websockets

async def handler(websocket, path):
    last_data = ""
    while True:
        data = await websocket.recv()
        print(data)
        reply = f"Data received as {data}"
        await websocket.send(reply)
        if last_data == "":
            await websocket.send("Before the Data, there was no Data")
        else:
            reply_of_last = f"Last data was {last_data}"
            await websocket.send(reply_of_last)
        last_data = data

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()