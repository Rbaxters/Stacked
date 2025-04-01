from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Define colors and ASCII art
colors = {
    'red': Fore.RED,
    'white': Fore.WHITE,
    'yellow': Fore.YELLOW,
    'green': Fore.GREEN,
    'blue': Fore.BLUE
}

ascii_art = {
    'red': r"""
        --------------------------------------------------
        |                                                |
        --------------------------------------------------
    """,
    'white': r"""
        ---------------------------------------------
        |                                           |
        ---------------------------------------------
    """,
    'yellow': r"""
       ---------------------------------------
       |                                     |
       ---------------------------------------
    """,
    'green': r"""
        ---------------------------------
        |                               |
        ---------------------------------
    """,
    'blue': r"""
        -----------------------------
        |                           |
        -----------------------------
    """
}

class RingStack:
    ##Class to manage the stack of rings
    def __init__(self):
        self.stack = []

    def push(self, ring_color):
        ##Add a colored ring to the stack
        if ring_color in colors:
            self.stack.append(ring_color)
            print(f"Added a {ring_color} ring to the stack.")
        else:
            print("You don't have that color, please choose from red, white, yellow, green, or blue.")
        self.print_stack()

    def pop(self):
        ##Remove the top ring from the stack
        if self.stack:
            removed_ring = self.stack.pop()
            print(f"Removed the top ring: {removed_ring.capitalize()} ring.")
        else:
            print("The stack is already empty.")
        self.print_stack()

    def print_stack(self):
        ##Print the stack of rings with color
        print("\nCurrent stack:")
        if not self.stack:
            print("The stack is empty.")
        else:
            for idx, ring in enumerate(reversed(self.stack), start=1):
                print(f"{colors[ring]}Ring {idx}: {ring.capitalize()}{Style.RESET_ALL}")
                print(f"{colors[ring]}{ascii_art[ring]}{Style.RESET_ALL}")  # Display the ASCII art with color
        print("\n")

def stackfunction():
    ##Main loop for managing the stack of rings
    ring_stack = RingStack()  # Create an instance of RingStack
    while True:
        print("Welcome to the Ring Stack!")
        print("Options:")
        print("1. Add a ring!")
        print("2. Remove the top ring!")
        print("3. Quit")
        choice = input("Choose an option from 1-3: ")

        if choice == '1':
            ring_color = input("Please enter the color of the ring. (red, white, yellow, green, blue): ").lower()
            ring_stack.push(ring_color)
        elif choice == '2':
            ring_stack.pop()
        elif choice == '3':
            print("Thank you for using the Ring Stack program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

# Directly call the main function
stackfunction()
