# 🕵️‍♀️ Chismosa

![Chismosa Logo](logo.png)

**Chismosa** *(Spanish for "nosy woman" or "gossip girl")* is a lightweight keylogger built with Python for **educational and ethical purposes only**. This project is intended to help you understand how keyboard input can be captured using Python for security research, parental controls, or authorized audits.

## ⚠️ Disclaimer

> **This project is for educational purposes only.**
>
> Do not use it on systems you do not own or without explicit permission.  
> Unauthorized use of keyloggers is illegal and unethical.

## 🛠 Features

- Simple keystroke logging using `pynput`
- Logs stored in a local `.txt` file
- Works on **Windows 10** and **Windows 11**
- Can be compiled into a hidden executable (with `pyinstaller`)

## 📦 Requirements

- Python 3
- `pynput` package

```bash
pip install pynput

▶️ Usage

python chismosa.py

## To generate an executable (Windows):

pip install pyinstaller
pyinstaller --noconsole --onefile chismosa.py

📄 Output
All keystrokes are stored in registro_teclas.txt in the same directory.

🧠 Why "Chismosa"?
In Spanish, chismosa means someone who likes to gossip or knows everything about everyone — just like this script 👀

🙋‍♂️ Author
Made with curiosity and humor by someone who wants you to hack ethically and code responsibly.
