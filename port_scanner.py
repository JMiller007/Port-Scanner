import tkinter as tk
from tkinter import messagebox, ttk
import socket
from datetime import datetime
import threading


# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout of 1 second
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False


# Function to scan a range of ports
def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports


# Function to start the scan
def start_scan():
    ip = ip_entry.get() or local_ip
    try:
        start_port = int(start_port_entry.get() or 20)
        end_port = int(end_port_entry.get() or 80)
    except ValueError:
        messagebox.showerror("Input Error", "Port numbers must be integers")
        return

    start_time = datetime.now()
    result_text.set(f"Scanning {ip} from port {start_port} to {end_port}...")
    progress.start()

    # Run the scan in a separate thread to prevent blocking the GUI
    scan_thread = threading.Thread(target=run_scan, args=(ip, start_port, end_port, start_time))
    scan_thread.start()


# Function to run the scan and update the UI with the results
def run_scan(ip, start_port, end_port, start_time):
    open_ports = scan_ports(ip, start_port, end_port)
    end_time = datetime.now()

    result_text.set(f"Open ports: {open_ports}\nTime taken: {end_time - start_time}")
    progress.stop()


# Set up the GUI
root = tk.Tk()
root.title("Port Scanner")
root.geometry("400x300")

local_ip = socket.gethostbyname(socket.gethostname())

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# IP address input
ttk.Label(root, text="IP Address:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ip_entry = ttk.Entry(root)
ip_entry.insert(0, local_ip)
ip_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Start port input
ttk.Label(root, text="Start Port:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
start_port_entry = ttk.Entry(root)
start_port_entry.insert(0, "20")
start_port_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# End port input
ttk.Label(root, text="End Port:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
end_port_entry = ttk.Entry(root)
end_port_entry.insert(0, "80")
end_port_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Scan button
scan_button = ttk.Button(root, text="Start Scan", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2, pady=10)

# Progress bar
progress = ttk.Progressbar(root, mode="indeterminate")
progress.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Result display
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, justify="left", wraplength=380)
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Make the columns expand with the window
root.columnconfigure(1, weight=1)

# Run the GUI event loop
root.mainloop()
