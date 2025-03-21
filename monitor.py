#!/usr/bin/env python3
import psutil
import time
import os
import sys
from colorama import init, Fore, Style

# Constants for alert thresholds
HIGH_CPU_USAGE = 90  # Percentage threshold for high CPU usage
HIGH_MEMORY_USAGE = 80  # Percentage threshold for high memory usage

# Define log file path in the current working directory
LOG_FILE_PATH = os.path.join(os.getcwd(), "system_usage.log")

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Colors for terminal output
WARNING_COLOR = Fore.RED + Style.BRIGHT  # Red for high usage warnings
OK_COLOR = Fore.GREEN + Style.BRIGHT  # Green for normal usage


def get_system_usage():
    """
    Retrieves the current CPU, memory, and disk usage of the system.

    Returns:
        tuple: A tuple containing three float values:
            - CPU usage percentage (float)
            - Memory usage percentage (float)
            - Disk usage percentage (float)
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    return cpu_usage, memory_usage, disk_usage


def log_usage(cpu_usage, memory_usage, disk_usage):
    """
    Logs the system's CPU, memory, and disk usage to a file and returns the formatted log entry.

    Args:
        cpu_usage (float): The percentage of CPU usage.
        memory_usage (float): The percentage of memory usage.
        disk_usage (float): The percentage of disk usage.

    Returns:
        tuple:
            - log_entry (str): Plain text log entry for file logging.
            - print_entry (str): Colored log entry for terminal output.
    """
    # Labels for logging (plain text)
    cpu_label_log = f"⚠️ CPU: {cpu_usage}%" if cpu_usage > HIGH_CPU_USAGE else f"CPU: {cpu_usage}%"
    mem_label_log = f"⚠️ Memory: {memory_usage}%" if memory_usage > HIGH_MEMORY_USAGE else f"Memory: {memory_usage}%"
    disk_label_log = f"Disk: {disk_usage}%"

    log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {cpu_label_log} | {mem_label_log} | {disk_label_log}"

    # Labels for terminal output (colored, only if output is a terminal)
    if sys.stdout.isatty():
        cpu_label_color = f"{WARNING_COLOR}⚠️ CPU: {cpu_usage}%{Style.RESET_ALL}" if cpu_usage > HIGH_CPU_USAGE else f"{OK_COLOR}CPU: {cpu_usage}%{Style.RESET_ALL}"
        mem_label_color = f"{WARNING_COLOR}⚠️ Memory: {memory_usage}%{Style.RESET_ALL}" if memory_usage > HIGH_MEMORY_USAGE else f"{OK_COLOR}Memory: {memory_usage}%{Style.RESET_ALL}"
        disk_label_color = f"{OK_COLOR}Disk: {disk_usage}%{Style.RESET_ALL}"
    else:
        cpu_label_color, mem_label_color, disk_label_color = cpu_label_log, mem_label_log, disk_label_log

    print_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {cpu_label_color} | {mem_label_color} | {disk_label_color}"

    # Write the plain text log entry to the file
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")

    return log_entry, print_entry


if __name__ == "__main__":
    cpu_usage, memory_usage, disk_usage = get_system_usage()
    log_entry, print_entry = log_usage(cpu_usage, memory_usage, disk_usage)
    print(print_entry)  # Prints colored output only in terminal
