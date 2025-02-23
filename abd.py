#!/usr/bin/python3
import os
import sys
import time
import atexit
import shutil
import signal

FRAME_DELAY = 0.05  # 50ms
ANDROID_ART = [
    "⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠙⢷⣤⣤⣴⣶⣶⣦⣤⣤⡾⠋⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⣼⣿⣿⣉⣹⣿⣿⣿⣿⣏⣉⣿⣿⣧⠀⠀⠀⠀",
    "⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀",
    "⣠⣄⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⣠⣄",
    "⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿",
    "⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿",
    "⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿",
    "⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿",
    "⠻⠟⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠻⠟",
    "⠀⠀⠀⠀⠉⠉⣿⣿⣿⡏⠉⠉⢹⣿⣿⣿⠉⠉⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠉⠉⠁"
]
ANDROID_HEIGHT = len(ANDROID_ART)
ANDROID_WIDTH = max(len(line) for line in ANDROID_ART)


def clear_screen():
    os.system("clear")  # Clear terminal screen


def get_terminal_width():
    return shutil.get_terminal_size((80, 24)).columns  # Get full terminal width


def draw_frame(position):
    clear_screen()
    terminal_width = get_terminal_width()
    for line in ANDROID_ART:
        print(" " * min(position, terminal_width - ANDROID_WIDTH) + line)
    sys.stdout.flush()  # Ensure smooth output


def restore_cursor():
    print("\033[?25h", end="")  # Show cursor again


def disable_ctrl_c():
    signal.signal(signal.SIGINT, signal.SIG_IGN)  # Ignore SIGINT (Ctrl+C)


def main():
    disable_ctrl_c()  # Disable Ctrl+C
    print("\033[?25l", end="")  # Hide cursor
    atexit.register(restore_cursor)  # Restore cursor on exit
    atexit.register(clear_screen)  # Ensure screen is cleared on exit

    terminal_width = get_terminal_width()

    # Run only one loop from start to end
    for pos in range(terminal_width - ANDROID_WIDTH):
        draw_frame(pos)
        time.sleep(FRAME_DELAY)

    clear_screen()  # Clear screen before exiting


if __name__ == "__main__":
    main()
