# 🖱️ Mouse Jiggler (Anti Screen Lock)

A lightweight Python script that **periodically moves your mouse** (and optionally presses Shift) to prevent your computer from going idle or locking the screen.

## ✨ Features

- 🕐 **Configurable interval** – set how often the mouse moves.  
- ⏳ **Optional duration** – stop automatically after a set number of minutes.  
- ⌨️ **Optional Shift press** – simulate Shift key presses to ensure activity detection.  
- 🚫 **Fail-safe support** – ignores `pyautogui.FailSafeException` so you can move the mouse manually.  
- 🧠 **Simple CLI** – easy to run from the terminal.

## 🚀 Usage
To start the jiggler with default settings (moves mouse and presses Shift every 2 minutes, runs indefinitely):
```bash
uv run jiggler.py
```

To customize the interval and duration (in this example, jiggle every 30 seconds for 2 hours, then stop):
```bash
uv run jiggler.py 120 30
```

To prevent Shift key presses, and only move the mouse:
```bash
uv run jiggler.py --no-shift
```
