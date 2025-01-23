# Food Randomizer
A simple Python application using `tkinter` and `pygame` that helps you randomly choose a food item from a list. Ideal for anyone looking to decide what to eat.

## Features
- Randomly selects food items.
- Plays a sound effect when the button is pressed.
- Customizable food list (stored in a text file).

## Prerequisites
- Python 3.x
- Libraries:
  - `tkinter` (usually comes with Python)
  - `pygame`
  - `random`

  To install `pygame`, run:
  ```
  pip install pygame
  ```
## Installation
1. Clone or download the repository.
2. Ensure the `food_list.txt` file and `random.mp3` are in the same directory as `main.py`.
3. Run the application: 
    ```
    python main.py
    ```

## Usage
1. Click the "สุ่มเลย!" button to pick a random food.
2. The chosen food appears!
  
   [![Demo](https://i.imgflip.com/9hne7f.gif)](https://imgflip.com/gif/9hne7f)

## Contributing
Feel free to fork the repository and submit a pull request if you'd like to contribute. Any suggestions or improvements are welcome!

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Click the link for more details.

## Lessons Learned
### What I Learned
- **tkinter Basics**: I gained experience in using `tkinter` for building simple GUI applications. This helped me understand the basic layout of GUI components like buttons, labels, and window configurations.
- **pygame for Sound**: I learned how to integrate `pygame` to play sound effects within a Python program.
- **File Handling**: Working with the food list stored in a separate text file (`food_list.txt`) improved my understanding of file handling in Python, especially reading and writing to text files.
- **Randomization Logic**: I implemented a randomization feature using Python's `random` module, learning how to manage lists and change content in the GUI.

### Challenges and How I Overcame Them
- **GUI Layout**: I faced difficulty aligning the GUI components in a way that looked visually appealing. I overcame this by experimenting with different padding and positioning options in `tkinter`.
- **Sound Playing Multiple Times**: I encountered an issue where the sound would play multiple times if the button was clicked rapidly. I solved this by adding a flag (`sound_played`) to track whether the sound has already been played.

These challenges helped me improve my debugging and problem-solving skills, and I now feel more comfortable working with both GUI applications and sound integration in Python.
