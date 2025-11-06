import time

import pyautogui


def jiggler(
    period: int = 60,
    duration: int | None = None,
    no_shift: bool = False,
    no_jiggle: bool = False,
    only_if_idle: bool = True,
    jiggle_distance: int = 2,
    shift_count: int = 3,
    verbose: bool = False,
) -> None:
    """Jiggle the mouse every `period` seconds for `duration` minutes to prevent screen lock."""
    end_time = (time.time() + duration * 60) if duration else None
    last_pos = pyautogui.position()
    while True:
        start_time = time.time()
        current_pos = pyautogui.position()
        if current_pos == last_pos or not only_if_idle:
            if verbose:
                print(f"\nJiggling mouse ({jiggle_distance}px) at {time.strftime('%H:%M:%S')}")
            if not no_jiggle:
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
                        pos_x, pos_y = pyautogui.position()
                        new_x = pos_x + x * jiggle_distance
                        new_y = pos_y + y * jiggle_distance
                        pyautogui.moveTo(new_x, new_y, duration=0.0)
                    except pyautogui.FailSafeException:
                        pass
            if not no_shift:
                if verbose:
                    print(f"Pressing Shift (x{shift_count}) at {time.strftime('%H:%M:%S')}")
                for _ in range(shift_count):
                    pyautogui.press("shift")
        elif verbose:
            print(f"\nJiggle skipped (no idle) at {time.strftime('%H:%M:%S')}")
        last_pos = pyautogui.position()
        time_used = time.time() - start_time
        if end_time:
            remaining = end_time - time.time()
            if remaining <= 0:
                break
            time.sleep(max(min(period - time_used, remaining), 0))
        else:
            time.sleep(max(period - time_used, 0))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "A program to jiggle the mouse and press the Shift key "
            "periodically to prevent screen lock."
        )
    )
    parser.add_argument(
        "duration",
        type=int,
        nargs="?",
        default=None,
        help="Duration in minutes for jiggles (default: indefinitely)",
    )
    parser.add_argument(
        "--period",
        type=int,
        default=120,
        help="Period in seconds between jiggles (default: 120)",
    )
    parser.add_argument(
        "--no-shift",
        action="store_true",
        help="Do not press the Shift key along with mouse movement",
    )
    parser.add_argument(
        "--no-jiggle",
        action="store_true",
        help="Do not move the mouse along with pressing Shift",
    )
    parser.add_argument(
        "--constant-jiggle",
        action="store_true",
        help="Jiggle the mouse even if it has been moved recently",
    )
    parser.add_argument(
        "--jiggle-distance",
        type=int,
        default=2,
        help="Distance in pixels to jiggle the mouse (default: 2)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output, print each jiggle action",
    )
    args = parser.parse_args()
    period = args.period if args.period > 0 else 120
    duration = args.duration if args.duration and args.duration > 0 else None
    no_shift = args.no_shift
    no_jiggle = args.no_jiggle
    only_if_idle = not args.constant_jiggle
    jiggle_distance = args.jiggle_distance
    verbose = args.verbose

    duration_text = ""
    if duration is not None:
        end_time = time.strftime("%H:%M", time.localtime(time.time() + duration * 60))
        duration_text = f" for {duration}min (will stop at {end_time})"
    print(f"\nJiggling ({period}s){duration_text}...")
    print("\nPress Ctrl+C to exit")
    try:
        jiggler(
            period=period,
            duration=duration,
            no_shift=no_shift,
            no_jiggle=no_jiggle,
            only_if_idle=only_if_idle,
            jiggle_distance=jiggle_distance,
            verbose=verbose,
        )

    except KeyboardInterrupt:
        pass
