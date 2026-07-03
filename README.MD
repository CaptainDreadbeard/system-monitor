System Monitor — Real‑Time Terminal Dashboard
A clean, fast, and highly readable real‑time system monitoring dashboard built in Python.
Designed as a modern, text‑based alternative to Task Manager and Ctrl+Alt+Delete, this tool provides live system metrics in a beautifully formatted terminal interface powered by the Rich library.

This monitor displays:

CPU usage (total + per‑core bars)

RAM usage

Disk usage

Network upload/download speeds

Top processes by CPU usage

Hardware temperatures via LibreHardwareMonitor (CPU, GPU, NVMe, motherboard, etc.)

It runs on Windows, macOS, and Linux — with full temperature support on Windows via LibreHardwareMonitor.

Features
🧠 CPU Monitoring
Total CPU usage

Per‑core usage with visual bar graphs

Smooth live updates

💾 Memory & Disk
RAM usage with MB readout

Disk usage percentage

🌐 Network Throughput
Live upload speed (KB/s)

Live download speed (KB/s)

📊 Top Processes
Displays the top 5 CPU‑hungry processes:

PID

Process name

CPU%

Memory%

🌡️ Hardware Temperatures (Windows)
Using LibreHardwareMonitor’s JSON API, the dashboard can show:

CPU package temperature

Individual CPU core temps

GPU core + hotspot temps

NVMe SSD temps

Motherboard sensors

Fan speeds (if exposed)

This makes the monitor a powerful diagnostic tool for thermal throttling, gaming loads, and hardware health.

Screenshots
(Add your own screenshots here — your dashboard looks great in the terminal.)

Example:

Code
CPU Total     ███████░░░░░░░░░░ 37%
Core 0        ██████░░░░░░░░░░░ 30%
Core 1        █████████░░░░░░░░ 48%
Core 2        ████░░░░░░░░░░░░░ 22%
Core 3        ████████████░░░░░ 63%

Upload         12.4 KB/s
Download       54.1 KB/s

CPU Package    67°C
GPU Core       54°C
NVMe SSD       41°C
Installation
1. Clone the repository
Code
git clone https://github.com/yourusername/system-monitor.git
cd system-monitor
2. Install dependencies
Code
pip install -r requirements.txt
Your requirements.txt should include:

Code
psutil
rich
requests
3. (Windows only) Enable temperature monitoring
Download LibreHardwareMonitor:

https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases (github.com in Bing)

Then:

Run LibreHardwareMonitor.exe

Go to Options → Remote Web Server → Run

Leave the port at 8085

Your sensors will now be available at:

Code
http://localhost:8085/data.json
The monitor will automatically detect and display them.

Usage
Run the dashboard:

Code
python monitor.py
The interface updates live at 4 frames per second.

Project Structure
Code
system-monitor/
│
├── monitor.py        # Main dashboard script
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
Why This Project Exists
Task Manager is powerful but:

visually cluttered

slow to navigate

not customizable

not cross‑platform

This project provides a clean, readable, terminal‑based alternative that’s perfect for:

developers

sysadmins

gamers

hardware enthusiasts

anyone who wants a quick, beautiful system overview

It’s also a great learning project for Python, Rich, psutil, and hardware monitoring APIs.

Future Improvements
Planned enhancements:

GPU usage + VRAM usage

Fan RPM monitoring

ASCII network throughput graph (sparkline)

Tabbed interface (switch views with keyboard)

Logging mode (write metrics to CSV)

Alerts (high temp, high CPU, etc.)