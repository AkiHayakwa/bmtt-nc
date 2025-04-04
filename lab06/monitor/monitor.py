import psutil
import platform
import socket
import logging
import time

logging.basicConfig(filename='system_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def log_info(category,message):
    logger.info(f"{category}: {message}")
    print(f"{category}: {message}")
def monitor_cpu_memory():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    
    log_info("CPU ", f"Usage :{cpu_percent}%")
    log_info("Memory", f"Usage : {memory_info.percent}%")