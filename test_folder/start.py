import os
import random
import time

# Terminal size
rows, cols = os.get_terminal_size()

def print_firework(x, y, char, color):
    """Print a single firework explosion at a given position."""
    for _ in range(random.randint(5, 10)):
        dx = random.randint(-3, 3)
        dy = random.randint(-3, 3)
        new_x, new_y = x + dx, y + dy
        if 0 < new_x < cols and 0 < new_y < rows:
            print(f"\033[{new_y};{new_x}H{color}{char}\033[0m", end="")

def launch_firework():
    """Simulate a firework launch and explosion."""
    x = random.randint(10, cols - 10)
    height = random.randint(5, rows - 5)

    # Firework launch
    for y in range(rows, height, -1):
        print(f"\033[{y};{x}H|", end="", flush=True)
        time.sleep(0.05)
        print(f"\033[{y};{x}H ", end="", flush=True)

    # Firework explosion
    explosion_chars = ['*', 'o', '.', '+']
    explosion_colors = ['\033[91m', '\033[93m', '\033[94m', '\033[95m']
    for _ in range(10):
        char = random.choice(explosion_chars)
        color = random.choice(explosion_colors)
        print_firework(x, height, char, color)
        time.sleep(0.1)

    # Clear the explosion
    print("\033[2J", end="", flush=True)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[?25l", end="")  # Hide cursor
    try:
        while True:
            launch_firework()
    except KeyboardInterrupt:
        print("\033[?25h", end="")  # Show cursor
        print("\nGoodbye! 🎆")

if __name__ == "__main__":
    main()
