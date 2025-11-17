BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(f"{BLUE} Welcome to the Intro Program! {RESET}")


name = input(f"{YELLOW} Please enter your name: {RESET}")
age = input(f"{YELLOW} Please enter your age: {RESET}")
hobby = input(f"{YELLOW} Please enter your hobby: {RESET}")

print(f"\n{GREEN} Hello, {name}! You are {age} years old and you enjoy {hobby}. Nice to meet you! {RESET}")