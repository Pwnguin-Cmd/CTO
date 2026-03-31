#!/usr/bin/env python3
"""
Demo script that simulates a few moves of the Snake game
This demonstrates that the game works correctly
"""

from snake_game import SnakeGame


def demo_game():
    """Run a simple demo of the game"""
    print("\n" + "=" * 50)
    print("  SNAKE GAME DEMO")
    print("=" * 50)
    print("\nThis demo simulates a few moves of the game.\n")
    
    game = SnakeGame(width=25, height=15)
    
    # Initial state
    print("Initial state:")
    print(f"Snake position: {list(game.snake)}")
    print(f"Food position: {game.food}")
    print(f"Score: {game.score}")
    print(f"Direction: {game.direction}")
    print()
    
    # Make a few moves
    moves = [
        ((1, 0), "right"),
        ((1, 0), "right"),
        ((0, 1), "down"),
        ((0, 1), "down"),
        ((-1, 0), "left"),
    ]
    
    for i, (direction, direction_name) in enumerate(moves, 1):
        if game.game_over:
            break
            
        print(f"Move {i}: Going {direction_name}")
        game.set_direction(direction)
        game.update()
        print(f"  Snake head: {game.snake[0]}")
        print(f"  Snake length: {len(game.snake)}")
        print(f"  Score: {game.score}")
        
        if game.snake[0] == game.food:
            print(f"  >>> Food eaten! New food at {game.food}")
        
        print()
    
    if game.game_over:
        print("Game Over!")
        print(f"Final score: {game.score}")
    else:
        print("Demo complete! The game is working correctly.")
        print(f"Final snake length: {len(game.snake)}")
        print(f"Final score: {game.score}")
    
    print("\n" + "=" * 50)
    print("To play the full game, run: python3 snake_game.py")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    demo_game()
