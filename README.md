# 🖱️ Mouse Jiggler (Anti Screen Lock)

A lightweight Python script that **periodically moves your mouse** (and optionally presses Shift) to prevent your computer from going idle or locking the screen.

## ✨ Features

- 🕐 **Configurable interval** – set how often the mouse moves.
- ⏳ **Optional duration** – stop automatically after a set number of minutes.
- 🤝 **Polite behavior** – by default, **does not jiggle if you’re using the mouse**, so it never interrupts your work.
- 🧩 **Selective awake actions** – choose to only move the mouse, only press Shift, or both.
- 🎯 **Adjustable jiggle distance** – control how far the cursor moves.
- 🧠 **Simple CLI** – easy to run and configure from the terminal.

## 🚀 Usage
To start the jiggler with default settings
*(moves the mouse and presses Shift every 2 minutes, runs indefinitely)*:
```bash
uv run jiggler.py
```

### Custom Duration
Run for a specific number of minutes (e.g., 60 minutes):
```bash
uv run jiggler.py 60
```

### Change Jiggle Interval
Set a custom period (in seconds) between jiggles (e.g., every 30 seconds):
```bash
uv run jiggler.py --period 30
```

### Disable Shift Key Press or Mouse Movement
Only move the mouse, without pressing Shift:
```bash
uv run jiggler.py --no-shift
```

Only press the Shift key periodically, without moving the mouse:
```bash
uv run jiggler.py --no-jiggle
```

### Constant Jiggle Mode (Impolite Mode)
Always jiggle even if the mouse was moved recently:
```bash
uv run jiggler.py --constant-jiggle
```

### Adjust Jiggle Distance
Change how far the mouse moves (default is 2 pixels):
```bash
uv run jiggler.py --jiggle-distance 5
```

### Verbose Output
Print a message every time the mouse jiggles:
```bash
uv run jiggler.py --verbose
```

## ⚙️ Full Command Reference
```bash
usage: jiggler.py [-h] [--period PERIOD] [--no-shift] [--no-jiggle]
                  [--constant-jiggle] [--jiggle-distance JIGGLE_DISTANCE]
                  [--verbose]
                  [duration]
```
| Argument | Type | Description | Default |
|-----------|------|--------------|----------|
| `duration` | Positional | Duration in minutes to run | Runs indefinitely |
| `--period` | Option | Time (seconds) between jiggles | `120` |
| `--no-shift` | Flag | Skip Shift key press | Off |
| `--no-jiggle` | Flag | Skip mouse movement | Off |
| `--constant-jiggle` | Flag | Always move the mouse even if recently moved | Off |
| `--jiggle-distance` | Option | Movement distance in pixels | `2` |
| `--verbose` | Flag | Print each jiggle action | Off |

---

💡 **Tip:** By default, the jiggler is polite — it won’t interfere while you’re actively using the mouse. This makes it ideal for having it active while you are working.