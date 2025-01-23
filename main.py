import tkinter as tk  # GUI library
import random  # Random library
import pygame  # For sound effects

# Initialize the window and pygame mixer
window = tk.Tk()
pygame.mixer.init()

# Function to load food list from a text file
def load_food_list():
    """Load the food list from a text file."""
    with open("food_list.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

# Food list
FOOD_LIST = load_food_list()

# Global variables
sound_played = False

# Fonts
RESULT_FOOD_TEXT = ("Arial", 20, "bold")
RANDOM_BUTTON_TEXT = ("Arial", 15, "bold")

# Function to update the result label with a random food item
def update_result():
    """Update the result label with a random food item."""
    current_food = FOOD_LIST.pop(0)
    result_food_label.config(text=current_food)
    FOOD_LIST.append(current_food)

# Function to play sound once
def play_sound_once():
    """Play the sound once when the button is pressed."""
    global sound_played

    if not sound_played:
        pygame.mixer.music.load("random.mp3")
        pygame.mixer.music.play()
        sound_played = True

# Function to simulate scrolling food items
def scroll_items(delay_index=0):
    """Scroll through food items with a delay and play sound once."""
    update_result()
    play_sound_once()

    delays = list(range(0, 600, 20))  # List of delays for scrolling

    if delay_index < len(delays):
        # Schedule the next scroll item update
        delay = delays[delay_index]
        window.after(delay, scroll_items, delay_index + 1)
        random_button.config(state=tk.DISABLED)  # Disable the button while scrolling
    else:
        global sound_played
        sound_played = False
        random_button.config(state=tk.NORMAL)  # Enable the button after scrolling is done

# Window configuration
window.title("กินอะไรดี")
window.minsize(500, 350)
window.maxsize(500, 350)
window.attributes('-toolwindow', 1)  # Remove minimize and maximize buttons
window.configure(background='#4B4758')

# Main content
result_food_label = tk.Label(window,
                             bg="black",
                             fg="white",
                             height=5,
                             width=25,
                             text="กินอะไรดีจ๊ะ?",
                             font=RESULT_FOOD_TEXT)

random_button = tk.Button(window,
                          bg="#30333C",
                          fg="#D9D9E3",
                          text="สุ่มเลย!",
                          command=scroll_items,
                          font=RANDOM_BUTTON_TEXT)

# Packing the elements
result_food_label.pack(pady=30)
random_button.pack(pady=25)

# Start the main loop
window.mainloop()
