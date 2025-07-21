# 🔍 Python Multi-threaded Port Scanner (Custom Target Support)

A fast, simple, and efficient **multi-threaded TCP port scanner** written in Python.  
Now with **command-line support** to specify any target host — giving users full control over where and what they scan.

Perfect for learning socket programming, ethical hacking fundamentals, or building your own tools inspired by Nmap.

---

## 🧑‍💻 How It Works

- Accepts a **target host** as a command-line argument  
  (defaults to `scanme.nmap.org` if none is provided)
- Creates TCP socket connections to the target host’s ports  
- Uses `connect_ex()` to check if a port is open (non-blocking)  
- Implements threading to scan multiple ports concurrently  
- Uses `threading.Lock()` for clean console output  
- Sets a 0.5 second timeout per connection to avoid long delays

---

## 🔧 Customizing Port Range

By default, the script scans ports **1 to 1024**, which covers the most common service ports.

👨‍💻 **Want to scan more ports (like up to 65535)?**

Open `scanner.py` and find this section:

```python
start_port = 1
end_port = 1024
```

🔁 **Change it to:**

```python
start_port = 1
end_port = 65535
```

💡 You can modify the range as needed depending on your scan requirements.

---

## 🚀 How to Use

1. **Clone this repository:**

   ```bash
   git clone https://github.com/likithgajula/python-port-scanner.git
   cd python-port-scanner
   ```

2. **Run the scanner script with a custom target:**

   ```bash
   python3 scanner.py <target>
   ```

   ✅ If no target is provided, it defaults to `scanme.nmap.org`.

3. **Observe the output listing open ports.**

---

## 💡 Sample Output

```plaintext
[+] Port 22 is OPEN
[+] Port 80 is OPEN
[+] Port 443 is OPEN

Scan complete for target: scanme.nmap.org
```

---

## ⚠️ Important Ethical Reminder

Always scan **only** targets you **own** or have **explicit permission** to test.  
❗ **Unauthorized scanning is illegal and unethical. Use this tool responsibly.**

---

## 📽️ Demo Video

Watch a live demo of this scanner running on Kali Linux:  
🔗 [LinkedIn Demo Video](https://www.linkedin.com/posts/likithgajula_python-cybersecurity-portscanner-activity-7335301127074152448-ikFk?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFKYyccBUMcsEb9xU18G0waIobWaFyCS4Vw) <!-- Replace with your real video -->

---

## 🛠️ Tech Stack

- Python 3
- `socket` for TCP connections  
- `threading` for concurrency  
- `sys.argv` for command-line input

---

## ⭐ Like This Project?

- Star the repo if you found it helpful  
- Fork it to expand or experiment  
- Share with others learning cybersecurity

---

## 📬 Contact

For feedback, collaboration, or walkthroughs — connect with me on [LinkedIn](https://www.linkedin.com/in/likithgajula)

---
