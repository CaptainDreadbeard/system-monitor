from time import sleep
import psutil
from rich.live import Live
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.layout import Layout  
import wmi

def cpu_bar(percent):
    # Create a simple bar using block characters
    bar_length = 20
    filled = int((percent / 100) * bar_length)
    return "█" * filled + "░" * (bar_length - filled)

def get_top_processes(limit=5):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)
    return processes[:limit]


def get_temperatures_wmi():
    try:
        w = wmi.WMI(namespace="root\\wmi")
        sensors = w.MSAcpi_ThermalZoneTemperature()
        results = []
        for sensor in sensors:
            # convert tenth of Kelvin to Celsius
            temp_c = (sensor.CurrentTemperature / 10.0) - 273.15
            results.append((sensor.InstanceName, f"{temp_c:.1f}°C"))
        return results if results else [("No WMI temperature sensors", "")]
    except Exception as e:
        return [("WMI temperature error", str(e))]

def make_table():
    layout = Layout()

    # Main system stats table
    table = Table(title="Real Time System Monitor", box=box.ROUNDED, expand=True)
    table.add_column("Metric", justify="left")
    table.add_column("Value", justify="right")

    # Total CPU 
    cpu = psutil.cpu_percent(interval=None)
    table.add_row("CPU Total", f"{cpu_bar(cpu)}" f"{cpu}%")

    # Per Core CPU
    per_core = psutil.cpu_percent(interval=None, percpu=True)
    for i, pct in enumerate(per_core):
        table.add_row(f"Core {i}", f"{cpu_bar(pct)} {pct}%")

    # RAM
    mem = psutil.virtual_memory()
    table.add_row("RAM Usage", f"{mem.percent}% ({mem.used // (1024**2)}) MB")

    # Disk
    disk = psutil.disk_usage("/")
    table.add_row("Disk Usage", f"{disk.percent}")

    # Network
    net1 = psutil.net_io_counters()
    sleep(0.2)
    net2 = psutil.net_io_counters()

    up = (net2.bytes_sent - net1.bytes_sent) / 1024
    down = (net2.bytes_recv - net1.bytes_recv) / 1024


    # Temperatures
    for label, temp in get_temperatures_wmi():
        table.add_row(label, temp)

    # Top processes table
    proc_table = Table(title="Top Processes", box=box.SIMPLE_HEAVY, expand=True)
    proc_table.add_column("PID", justify="right")
    proc_table.add_column("Name", justify="left")
    proc_table.add_column("CPU%", justify="right")
    proc_table.add_column("MEM%", justify="right")

    for p in get_top_processes():
        proc_table.add_row(
            str(p['pid']),
            p['name'][:20] if p['name'] else "Unknown",
            f"{p['cpu_percent']:.1f}",
            f"{p['memory_percent']:.1f}"
        )

    # Build layout
    layout.split_column(
        Layout(Panel(table, title="System Stats")),
        Layout(Panel(proc_table, title="Processes"))
    )

    

    table.add_row("Upload", f"{up:.1f} KB/s")
    table.add_row("Download, f{down:.1f} KB/s")

    return layout

with Live(refresh_per_second=4) as live:
    while True:
        live.update(make_table())