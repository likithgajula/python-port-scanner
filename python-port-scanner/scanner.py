import socket
import threading
import sys

# Get target from command-line argument or default to scanme.nmap.org
target_host = sys.argv[1] if len(sys.argv) > 1 else "scanme.nmap.org"
start_port = 1
end_port = 1024

# Lock for clean console output
print_lock = threading.Lock()

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                with print_lock:
                    print(f"[+] Port {port} is OPEN")
    except:
        pass

# Launch threads
threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"\nScan complete for target: {target_host}")
