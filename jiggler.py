import time

import pyautogui


def jiggler(
    period: int = 60, duration: int | None = None, press_shift: bool = True
) -> None:
    """Jiggle the mouse every `period` seconds for `duration` minutes to prevent screen lock."""
    distance = 2
    end_time = (time.time() + duration * 60) if duration else None
    while True:
        for x, y in [
            (1, 0),
            (0, -1),
            (-1, 0),
            (0, 1),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 0),
        ]:
            try:
                posX, posY = pyautogui.position()
                newX = posX + x * distance
                newY = posY + y * distance
                pyautogui.moveTo(newX, newY)
            except pyautogui.FailSafeException:
                pass
        if press_shift:
            for _ in range(3):
                pyautogui.press("shift")
        if end_time:
            remaining = end_time - time.time()
            if remaining <= 0:
                break
            time.sleep(min(period, remaining))
        else:
            time.sleep(period)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="A simple program to jiggle the mouse periodically, to prevent screen lock."
    )
    parser.add_argument(
        "duration",
        type=int,
        nargs="?",
        default=None,
        help="Duration in minutes for jiggles (default: indefinitely)",
    )
    parser.add_argument(
        "period",
        type=int,
        nargs="?",
        default=120,
        help="Period in seconds between jiggles (default: 120)",
    )
    parser.add_argument(
        "--no-shift",
        action="store_true",
        help="Do not press the Shift key along with mouse movement",
    )
    args = parser.parse_args()
    period = args.period
    duration = args.duration if args.duration and args.duration > 0 else None
    press_shift = not args.no_shift

    duration_text = ""
    if duration is not None:
        end_time = time.strftime("%H:%M", time.localtime(time.time() + duration * 60))
        duration_text = f" for {duration}min (will stop at {end_time})"
    print(f"\nJiggling ({period}s){duration_text}...")
    print("\nPress Ctrl+C to exit")
    try:
        jiggler(period=period, duration=duration, press_shift=press_shift)

    except KeyboardInterrupt:
        pass
