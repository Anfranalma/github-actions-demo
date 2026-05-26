import tkinter as tk
import subprocess

def scan_network():
    ip_address = entry_ip.get().strip()

    result_text.delete(1.0, tk.END)

    if not ip_address:
        result_text.insert(tk.END, "Please enter an IP address.")
        return

    result_text.insert(tk.END, f"Scanning network: {ip_address}\n\n")

    try:
        result = subprocess.run(
            ["nmap", "-F", ip_address],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            result_text.insert(tk.END, result.stdout)
        else:
            result_text.insert(tk.END, "An error occurred:\n\n")
            result_text.insert(tk.END, result.stderr)

    except FileNotFoundError:
        result_text.insert(
            tk.END,
            "Nmap was not found. Install Nmap and make sure it is added to PATH."
        )

window = tk.Tk()
window.title("Network Scanner")

label_ip = tk.Label(window, text="Enter IP Address:")
label_ip.pack()

entry_ip = tk.Entry(window)
entry_ip.pack()

scan_button = tk.Button(window, text="Scan Network", command=scan_network)
scan_button.pack()

result_text = tk.Text(window)
result_text.pack()

window.mainloop()