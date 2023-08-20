import os
import random
import string
import threading
import time

# Global variables to track the total generated passwords and current count
total_generated = 0
current_count = 0

def generate_password(length, difficulty):
    if difficulty == "easy":
        characters = string.ascii_lowercase
    elif difficulty == "medium":
        characters = string.ascii_letters + string.digits
    elif difficulty == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid difficulty level")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def write_passwords_to_file(filename, passwords):
    with open(filename, 'w') as file:
        file.write("MADE BY SIWAMKING1\n")
        file.write("\n".join(passwords))

def update_display():
    global total_generated, current_count
    while current_count < num_passwords:
        print(f"Generating passwords... Total generated: {total_generated}", end="\r")
        time.sleep(0.001)  # Update every millisecond

def print_colored_text(text, color_code):
    print(color_code + text + '\033[0m')

if __name__ == "__main__":
    print_colored_text("Connected:> ", '\033[32m')  # Green color
    print_colored_text("Loading:> ", '\033[33m')   # Yellow color
    
    # Multiline ASCII art with different colors
    ascii_art = [
        '\033[34m╔══╦╗░░░░░░░░╔╗╔╗░░░░░╔╗░\033[0m',
        '\033[35m║══╬╬╦╦╦═╗╔══╣╠╬╬═╦╦═╦╝║░\033[0m',
        '\033[36m╠══║║║║║╬╚╣║║║═╣║║║║╬╠╗║░\033[0m',
        '\033[37m╚══╩╩══╩══╩╩╩╩╩╩╩╩═╬╗║║║░\033[0m',
        '\033[38m░░░░░░░░░░░░░░░░░░░╚═╬╝╚╗\033[0m'
    ]
    
    for line in ascii_art:
        print_colored_text(line, '\033[39m')  # Default color
    
    print_colored_text("siwamking@sk1:~>$ cd siwamking", '\033[31m')  # Red color
   
    input("Press Enter to continue...")
    
    min_length = int(input("Enter the minimum password length: "))
    max_length = int(input("Enter the maximum password length: "))
    difficulty = input("Enter the password difficulty (easy/medium/hard): ")
    
    num_passwords = int(input("Enter the quantity of passwords to generate: "))
    
    # Get the user's "Downloads" folder path
    downloads_folder = os.path.expanduser("~/Downloads")
    filename = os.path.join(downloads_folder, "passwords.txt")
    
    # Create and start the display update thread
    display_thread = threading.Thread(target=update_display)
    display_thread.daemon = True
    display_thread.start()
    
    print("Generating passwords... Total generated: 0")
    
    passwords = []
    for _ in range(num_passwords):
        password_length = random.randint(min_length, max_length)
        passwords.append(generate_password(password_length, difficulty))
        total_generated += 1
        current_count += 1
    
    # Wait for the display thread to finish
    display_thread.join()
    
    # Save passwords to a file
    write_passwords_to_file(filename, passwords)
    
    print(f"\n{num_passwords} passwords generated and saved to {filename}")
    print(f"Password file location: {filename}")
