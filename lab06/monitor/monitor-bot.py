import psutil
import logging
import time
import asyncio
from telegram import Bot

BOT_TOKEN = '6808243924:AAFJCe4KtZVGPhz2_D074K148ZJOhsNAMQQ'

CHAT_ID = '-4031606701'

logging.basicConfig(filename='system_monitor_bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def log_info(category, message):
    logger.info(f"{category}: {message}")
    print(f"{category}: {message}")
    
async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)
def monitor_cpu_memory():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    
    log_info("CPU", f"Usage :{cpu_percent}%")
    log_info("Memory", f"Usage : {memory_info.percent}%")
    
    message = f"CPU Usage: {cpu_percent}%\nMemory Usage: {memory_info.percent}%"
    asyncio.run(send_telegram_message(message))
def monitor_system():
    log_info("System Monitor", "Starting system monitoring...")
    while True:
        monitor_cpu_memory()
        log_info("System Monitor", "-------------------------------")
        time.sleep(60)
if __name__ == "__main__":
    monitor_system()   
        