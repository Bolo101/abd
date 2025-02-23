# Android Terminal Animation (abd)

A fun terminal animation that displays an ASCII art Android mascot moving across your terminal, inspired by the classic `sl` command. Written in Python for simplicity and portability.

## Features

- Smooth terminal animation
- Unicode-based Android mascot design
- Configurable animation speed
- Proper cursor handling (hidden during animation, restored on exit)
- Cross-platform compatibility

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/abd.git
cd abd
```

2. Make the script executable:
```bash
chmod +x abd.py
```

3. Optional: Create a symbolic link to make it globally accessible:
```bash
sudo ln -s $(pwd)/abd.py /usr/local/bin/abd
```

## Usage

Simply run the command:
```bash
./abd.py
```

Or if you created the symbolic link:
```bash
abd
```

## Configuration

You can modify these constants in the script to customize the animation:

- `FRAME_DELAY`: Animation speed (default: 0.05 seconds)
- `TERMINAL_WIDTH`: Maximum terminal width (default: 80 characters)
- `ANDROID_ART`: ASCII art design

## Requirements

- Python 3.x
- Unix-like operating system (Linux, macOS) for the `clear` command
- Terminal that supports Unicode characters


## License

MIT License - feel free to use this code in your own projects.

## Credits

- Inspired by the classic `sl` command
- Android mascot design using Unicode characters

## Author

[Bolo101]
