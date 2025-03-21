#!/usr/bin/env python3
import psutil
import time
import os

HIGH_CPU_USAGE = 90
HIGH_MEMORY_USAGE = 80
LOG_FILE_PATH = os.path.join(os.getcwd(), "system_usage.log")


def get_system_usage():
    """
    Retrieves the current CPU, memory, and disk usage of the system.

    Returns:
        str: A formatted string containing CPU usage percentage, memory usage percentage, and disk usage percentage.
    """
    cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage percentage
    memory_usage = psutil.virtual_memory()  # Memory (RAM) usage
    disk_usage = psutil.disk_usage('/')  # Disk usage on the root directory

    return cpu_usage, memory_usage.percent, disk_usage.percent


def log_usage(cpu_usage, memory_usage, disk_usage):
    """
    Logs the system's CPU, memory, and disk usage to a file.

    The log entry includes a timestamp and is appended to the "system_usage.log" file.
    """
    cpu_label = f"⚠️ CPU: {cpu_usage}%" if cpu_usage > HIGH_CPU_USAGE else f"CPU: {cpu_usage}%"
    mem_label = f"⚠️ Memory: {memory_usage}%" if memory_usage > HIGH_MEMORY_USAGE else f"Memory: {memory_usage}%"
    disk_label = f"Disk: {disk_usage}%"

    log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - CPU: {cpu_label} | Memory: {mem_label} | Disk: {disk_label}"
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")

    return log_entry


if __name__ == "__main__":
    cpu_usage, memory_usage, disk_usage = get_system_usage()
    log_entry = log_usage(cpu_usage, memory_usage, disk_usage)
    print(f" {log_entry}")
