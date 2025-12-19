#!/usr/bin/env python3
"""
Terminal Snake Game
===================
A classic Snake game that runs in the terminal using only Python standard library.
Works on online Python interpreters (Replit, Trinket, Google Colab, etc.)

Controls:
- W or UP: Move up
- S or DOWN: Move down
- A or LEFT: Move left
- D or RIGHT: Move right
- Q: Quit game

Instructions:
1. Run the script: python snake_game.py
2. Enter your move direction and press Enter
3. Eat the food (*) to grow and increase your score
4. Avoid hitting walls or yourself!
"""

import random
import os
import sys
import time
from collections import deque


class SnakeGame:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.score = 0
        self.game_over = False
        
        # Initialize snake in the middle of the board
        start_x = width // 2
        start_y = height // 2
        self.snake = deque([(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)])
        
        # Initial direction (moving right)
        self.direction = (1, 0)
        
        # Spawn first food
        self.food = self._spawn_food()
    
    def _spawn_food(self):
        """Spawn food at a random empty position"""
        while True:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if (x, y) not in self.snake:
                return (x, y)
    
    def _is_valid_direction(self, new_direction):
        """Check if the new direction is valid (not opposite to current)"""
        # Can't go directly opposite
        return (new_direction[0] + self.direction[0] != 0 or 
                new_direction[1] + self.direction[1] != 0)
    
    def set_direction(self, direction):
        """Set the snake's direction if valid"""
        if self._is_valid_direction(direction):
            self.direction = direction
    
    def update(self):
        """Update game state (move snake, check collisions, etc.)"""
        if self.game_over:
            return
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Check wall collision
        if (new_head[0] <= 0 or new_head[0] >= self.width - 1 or
            new_head[1] <= 0 or new_head[1] >= self.height - 1):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.food = self._spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def render(self):
        """Render the game board"""
        # Clear screen (works on most terminals and online interpreters)
        clear_screen()
        
        # Print title and score
        print("=" * (self.width + 2))
        print(f"  SNAKE GAME - Score: {self.score}")
        print("=" * (self.width + 2))
        print()
        
        # Create game board
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw walls
        for x in range(self.width):
            board[0][x] = '#'
            board[self.height - 1][x] = '#'
        for y in range(self.height):
            board[y][0] = '#'
            board[y][self.width - 1] = '#'
        
        # Draw food
        board[self.food[1]][self.food[0]] = '*'
        
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                board[y][x] = 'O'  # Head
            else:
                board[y][x] = 'o'  # Body
        
        # Print board
        for row in board:
            print(''.join(row))
        
        print()
        if self.game_over:
            print("GAME OVER!")
            print(f"Final Score: {self.score}")
            print()
        else:
            print("Controls: W/A/S/D or arrows (then Enter) | Q to quit")
            print(f"Snake length: {len(self.snake)}")


def clear_screen():
    """Clear the terminal screen"""
    # Works on most systems and online interpreters
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac/Online interpreters
        os.system('clear')
        # Fallback: print newlines if clear doesn't work
        if not sys.stdout.isatty():
            print('\n' * 50)


def get_direction_input():
    """Get direction input from user"""
    valid_inputs = {
        'w': (0, -1), 'W': (0, -1),
        's': (0, 1), 'S': (0, 1),
        'a': (-1, 0), 'A': (-1, 0),
        'd': (1, 0), 'D': (1, 0),
        'up': (0, -1), 'UP': (0, -1),
        'down': (0, 1), 'DOWN': (0, 1),
        'left': (-1, 0), 'LEFT': (-1, 0),
        'right': (1, 0), 'RIGHT': (1, 0),
    }
    
    try:
        user_input = input("Direction: ").strip().lower()
        
        if user_input in ['q', 'quit', 'exit']:
            return None
        
        if user_input in valid_inputs:
            return valid_inputs[user_input]
    except (EOFError, KeyboardInterrupt):
        return None
    
    return 'continue'  # Continue in current direction


def main():
    """Main game loop"""
    print("\n" + "=" * 40)
    print("  WELCOME TO SNAKE GAME!")
    print("=" * 40)
    print("\nInstructions:")
    print("- Use W/A/S/D or arrow words (up/down/left/right)")
    print("- Type your direction and press Enter")
    print("- Eat the food (*) to grow")
    print("- Avoid walls (#) and yourself")
    print("- Type Q to quit")
    print("\nPress Enter to start...")
    input()
    
    game = SnakeGame(width=30, height=20)
    
    while not game.game_over:
        game.render()
        
        direction = get_direction_input()
        
        if direction is None:  # User wants to quit
            print("\nThanks for playing!")
            break
        elif direction != 'continue':  # User provided new direction
            game.set_direction(direction)
        
        game.update()
    
    if game.game_over:
        game.render()
        print("\nPress Enter to exit...")
        try:
            input()
        except (EOFError, KeyboardInterrupt):
            pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
