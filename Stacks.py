from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Define colors and ASCII art
colors = {
    'red': Fore.RED,
    'orange': Fore.YELLOW + Style.BRIGHT,
    'yellow': Fore.YELLOW,
    'green': Fore.GREEN,
    'blue': Fore.BLUE
}

ascii_art = {
    'red': r"""
        ......................................................
        =:...................................................+
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =....................................................+
        .::::::::::::::::::::::::::::::::::::::::::::::::::::.
    """,
    'orange': r"""
        ......................................................
        =:...................................................+
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =....................................................+
        .::::::::::::::::::::::::::::::::::::::::::::::::::::.
    """,
    'yellow': r"""
        ......................................................
        =:...................................................+
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =....................................................+
        .::::::::::::::::::::::::::::::::::::::::::::::::::::.
    """,
    'green': r"""
        ......................................................
        =:...................................................+
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =....................................................+
        .::::::::::::::::::::::::::::::::::::::::::::::::::::.
    """,
    'blue': r"""
        ......................................................
        =:...................................................+
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =.                                                  .=
        =....................................................+
        .::::::::::::::::::::::::::::::::::::::::::::::::::::.
    """
}

# Stack list
stack = []

def print_stack():
    """Print the stack of rings with color"""
    print("\nCurrent stack:")
    if not stack:
        print("The stack is empty.")
    else:
        for idx, ring in enumerate(reversed(stack), start=1):
            print(f"{colors[ring]}Ring {idx}: {ring.capitalize()}{Style.RESET_ALL}")
            print(f"{colors[ring]}{ascii_art[ring]}{Style.RESET_ALL}")  # Display the ASCII art with color
    print("\n")

def add_ring(ring_color):
    """Add a colored ring"""
    if ring_color in colors:
        stack.append(ring_color)
        print(f"Added a {ring_color} ring to the stack.")
    else:
        print("Invalid color, please choose from red, orange, yellow, green, or blue.")
    print_stack()

def remove_ring():
    """Remove the top ring from the stack"""
    if stack:
        removed_ring = stack.pop()
        print(f"Removed the top ring: {removed_ring.capitalize()} ring.")
    else:
        print("The stack is already empty.")
    print_stack()

def bigbucks():
    """Main loop for managing the stack of rings"""
    while True:
        print("Options:")
        print("1. Add a ring")
        print("2. Remove the top ring")
        print("3. Quit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            ring_color = input("Enter the color of the ring (red, orange, yellow, green, blue): ").lower()
            add_ring(ring_color)
        elif choice == '2':
            remove_ring()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

# Directly call the main function
bigbucks()
