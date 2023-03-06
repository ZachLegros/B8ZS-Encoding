import asyncio
import websockets
import B8ZS

async def handler(websocket):
    while True:
        response = await websocket.recv()
        if response == "sending":
            await websocket.send("ready")
            msg = await websocket.recv()
            print("Message received:", B8ZS.B8ZS_decode(msg))
            await websocket.send("received")

start_server = websockets.serve(handler, "localhost", 8000)
 
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()