import asyncio
import websockets

URI = "ws://localhost:8765"


async def client():
    async with websockets.connect(URI) as websocket:
        message = "Привет, сервер!"
        print(f"Оправка: {message}")
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")


asyncio.run(client())
