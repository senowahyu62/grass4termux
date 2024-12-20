import sys
import os  # Tambahkan import os
from loguru import logger
import asyncio
import random
import ssl
import json
import time
import uuid
import websockets

# Konfigurasi loguru agar hanya satu entri log ditampilkan di konsol
logger.remove()  # Hapus konfigurasi default
logger.add(sys.stdout, format="{message}", level="INFO", enqueue=True, backtrace=False, diagnose=False)

async def connect_to_wss(user_id):
    device_id = str(uuid.uuid4())
    while True:
        try:
            await asyncio.sleep(random.randint(1, 10) / 10)
            custom_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            }
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            uri = "wss://proxy.wynd.network:4650/"
            server_hostname = "proxy.wynd.network"
            async with websockets.connect(uri, ssl=ssl_context, extra_headers=custom_headers,
                                          server_hostname=server_hostname) as websocket:
                async def send_ping():
                    while True:
                        send_message = json.dumps(
                            {"id": str(uuid.uuid4()), "version": "1.0.0", "action": "PING", "data": {}})
                        # Bersihkan layar sebelum menampilkan log baru
                        os.system("clear")
                        logger.debug(send_message)
                        await websocket.send(send_message)
                        await asyncio.sleep(20)

                await asyncio.sleep(1)
                asyncio.create_task(send_ping())

                while True:
                    response = await websocket.recv()
                    message = json.loads(response)
                    # Bersihkan layar sebelum menampilkan log baru
                    os.system("clear")
                    logger.info(message)
                    if message.get("action") == "AUTH":
                        auth_response = {
                            "id": message["id"],
                            "origin_action": "AUTH",
                            "result": {
                                "browser_id": device_id,
                                "user_id": user_id,
                                "user_agent": custom_headers['User-Agent'],
                                "timestamp": int(time.time()),
                                "device_type": "extension",
                                "version": "2.5.0"
                            }
                        }
                        os.system("clear")
                        logger.debug(auth_response)
                        await websocket.send(json.dumps(auth_response))

                    elif message.get("action") == "PONG":
                        pong_response = {"id": message["id"], "origin_action": "PONG"}
                        os.system("clear")
                        logger.debug(pong_response)
                        await websocket.send(json.dumps(pong_response))
        except Exception as e:
            os.system("clear")
            logger.error(e)

async def main():
    _user_id = ''  # TODO: Sesuaikan user_id di sini
    await connect_to_wss(_user_id)

if __name__ == '__main__':
    asyncio.run(main())
