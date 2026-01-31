import asyncio
import websockets

URI = "ws://localhost:8765"


async def users_client():
    async with websockets.connect(URI) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")


asyncio.run(users_client())
