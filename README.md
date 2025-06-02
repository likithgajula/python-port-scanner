# 🔍 python-port-scanner

A fast, simple, and efficient **multi-threaded TCP port scanner** written in Python.  
This project helps identify open ports on a target using raw socket programming and threading for performance — a great way to learn how tools like Nmap work under the hood.

---

## 🧑‍💻 How It Works

- Creates TCP socket connections to the target host’s ports  
- Uses `connect_ex()` to check if a port is open (non-blocking)  
- Implements threading to scan multiple ports concurrently  
- Uses `threading.Lock()` for clean console output  
- Sets a 0.5 second timeout per connection to avoid delays

---

## 🔧 Customizing Port Range

By default, the script scans ports **1 to 1024**, which includes the most commonly used system and service ports.

👨‍💻 **Want to scan more ports (like up to 65535)?**

Open `scanner.py` and find this line:

```python
for port in range(1, 1025):  # Default range from port 1 to 1024
```

🔁 **Change it to:**

```python
for port in range(1, 65536):  # Full range up to port 65535
```

💡 You can modify the range as needed depending on your scan requirements.

---

## 🚀 How to Use

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/python-port-scanner.git
   cd python-port-scanner
   ```

2. **Run the scanner script:**

   ```bash
   python3 scanner.py
   ```

3. **Observe the output listing open ports.**

---

## 💡 Sample Output

```plaintext
[+] Port 22 is OPEN
[+] Port 80 is OPEN
[+] Port 443 is OPEN

Scan complete.
```

---

## ⚠️ Important Ethical Reminder

Always scan **only** targets you **own** or have **explicit permission** to test.  
❗ **Unauthorized scanning is illegal and unethical. Use this tool responsibly.**

---

## 📽️ Demo Video

Watch a live demo of this scanner running on Kali Linux:  
🔗 [LinkedIn Demo Video](https://www.linkedin.com/your-demo-link) <!-- Replace this with your actual LinkedIn video link -->

---
