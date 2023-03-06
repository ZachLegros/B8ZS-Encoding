import asyncio
import websockets
import B8ZS

async def send_message(websocket):
    while True:
        valid_input = False
        msg = ""
        while not valid_input:
            msg = input('Enter the message: ')
            if not B8ZS.validate_message(msg):
                print("Invalid message. Please only enter '0's and '1's.")
            else:
                valid_input = True

        await websocket.send("sending")
        response = await websocket.recv()
        if response == "ready":
            encoded_msg = B8ZS.B8ZS_encode(msg)
            print(f'Message sent: {encoded_msg}')
            await websocket.send(encoded_msg)
            response = await websocket.recv()
            if response == "received":
                print(f"Message {msg} was received.")
    

async def client():
    async with websockets.connect('ws://localhost:8000') as websocket:
        send_task = asyncio.create_task(send_message(websocket))
        await asyncio.gather(send_task)


if __name__ == "__main__": 
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(client())
    except KeyboardInterrupt:
        loop.close()