# Automated-System-Performance-Monitor
The System Monitor project is a lightweight yet powerful Python-based monitoring tool designed to track CPU, memory, and disk usage in real-time. This tool logs system resource consumption into a CSV file and provides colored visual feedback in the terminal for better readability.
The project is fully automated, running every 5 minutes using GitHub Actions, ensuring continuous tracking and logging, even when the local machine is turned off. This makes it useful for remote system monitoring and long-term performance analysis.

I developed this project as a self-learning experience to improve my skills in GitHub actions, Bash scripting, CI/CD pipelines and Cron Jobs.


## Installation
To use the System Monitor locally, follow these steps:

- Clone the Repository
- Install Dependencies - Ensure you have Python installed (preferably version **3.10** or higher). Then, install the required dependencies (pip install -r requirements.txt -> this will install 'psutil' and 'colorana').
- run - to run the monitor script manually, execute: python monitor.py
- (Optional) Automate Execution*- If you want the script to run every 5 minutes on your local machine, you can set up a crontab job (Linux/macOS) to execute `monitor.py` at regular intervals.

## GitHub Actions Automation
This project uses GitHub Actions to automatically execute the script every 5 minutes. The workflow is defined in `.github/workflows/monitor_tests.yml`.

## Example Output
### Terminal Output (Colored)
```
2025-03-22 12:43:11 - CPU: 23% |  Memory: 89.2% | Disk: 26.2%
```

### CSV Log Entry
```
Timestamp, CPU Usage (%), Memory Usage (%), Disk Usage (%)
2025-03-22 12:43:11,23,89.2,26.2
```

## Feedback & Contact

If you find any issues, have questions, or suggestions for improvement, feel free to reach out:

Email: yonzra12@gmail.com


## License
This project is open-source and available for personal and educational use.



 



