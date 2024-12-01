import random
import matplotlib.pyplot as plt

def create_word_search(words, grid_size=15):
    # Initialize the grid with empty spaces
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Directions for placing words (dx, dy)
    directions = [
        (0, 1),  # Horizontal (right)
        (1, 0),  # Vertical (down)
        (1, 1),  # Diagonal (down-right)
        (-1, 1), # Diagonal (up-right)
    ]

    def can_place_word(word, x, y, dx, dy):
        """Check if a word can be placed starting at (x, y) in the direction (dx, dy)."""
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= grid_size or ny >= grid_size or (grid[nx][ny] != ' ' and grid[nx][ny] != word[i]):
                return False
        return True

    def place_word(word, x, y, dx, dy):
        """Place a word on the grid starting at (x, y) in the direction (dx, dy)."""
        for i in range(len(word)):
            grid[x + i * dx][y + i * dy] = word[i]

    # Shuffle the word list to randomize placement order
    random.shuffle(words)

    # Place each word in the grid
    for word in words:
        placed = False
        attempts = 0
        while not placed and attempts < 100:  # Try up to 100 times to place the word
            direction = random.choice(directions)
            start_x = random.randint(0, grid_size - 1)
            start_y = random.randint(0, grid_size - 1)
            if can_place_word(word, start_x, start_y, direction[0], direction[1]):
                place_word(word, start_x, start_y, direction[0], direction[1])
                placed = True
            attempts += 1

    # Fill the rest of the grid with random letters
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice(alphabet)

    return grid

def draw_word_search(grid):
    grid_size = len(grid)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    
    # Draw the grid
    for x in range(grid_size + 1):
        ax.axhline(x, color='black', linewidth=1)
        ax.axvline(x, color='black', linewidth=1)
    
    # Add the letters in the grid
    for i in range(grid_size):
        for j in range(grid_size):
            ax.text(j + 0.5, grid_size - i - 0.5, grid[i][j], 
                    fontsize=12, va='center', ha='center', weight='bold')

    # Remove axes
    ax.axis('off')
    plt.tight_layout()
    plt.show()

# Main Program
print("Welcome to the Word Search Puzzle Generator!")
num_words = int(input("How many words do you want to include in the puzzle? "))

words = []
print(f"Please enter {num_words} words (one at a time):")
for _ in range(num_words):
    word = input().strip().upper()
    words.append(word)

# Generate the puzzle
grid = create_word_search(words)

# Display the puzzle
draw_word_search(grid)
