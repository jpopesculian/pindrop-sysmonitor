import threading, time
from .metrics import get_disk_stats, get_mem_stats, get_cpu_stats
from .repo import connect, insert

def save_stats(conn):
    insert(conn, "Cpu", get_cpu_stats())
    insert(conn, "Mem", get_mem_stats())
    insert(conn, "Disk", get_disk_stats())

def save_stats_every(interval):
    conn = connect()
    while True:
        save_stats(conn)
        time.sleep(interval)

def start_monitor(interval):
    monitor_thread = threading.Thread(target=save_stats_every, args=(interval,))
    monitor_thread.start()