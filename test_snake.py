#!/usr/bin/env python3
"""
Simple test script to verify Snake game logic
"""

import sys
from snake_game import SnakeGame


def test_game_initialization():
    """Test that the game initializes correctly"""
    game = SnakeGame(width=20, height=15)
    assert game.width == 20
    assert game.height == 15
    assert game.score == 0
    assert not game.game_over
    assert len(game.snake) == 3
    print("✓ Game initialization test passed")


def test_snake_movement():
    """Test that snake moves correctly"""
    game = SnakeGame(width=20, height=15)
    initial_head = game.snake[0]
    game.update()
    new_head = game.snake[0]
    
    # Snake should have moved right (default direction)
    assert new_head[0] == initial_head[0] + 1
    assert new_head[1] == initial_head[1]
    print("✓ Snake movement test passed")


def test_direction_change():
    """Test that direction changes work correctly"""
    game = SnakeGame(width=20, height=15)
    
    # Change direction to down
    game.set_direction((0, 1))
    assert game.direction == (0, 1)
    
    # Try to change to opposite direction (should not work)
    game.set_direction((0, -1))
    assert game.direction == (0, 1)  # Should still be down
    
    print("✓ Direction change test passed")


def test_wall_collision():
    """Test that wall collisions are detected"""
    game = SnakeGame(width=20, height=15)
    
    # Move snake to the right wall
    game.snake.clear()
    game.snake.append((18, 10))
    game.snake.append((17, 10))
    game.direction = (1, 0)
    
    game.update()
    assert game.game_over
    print("✓ Wall collision test passed")


def test_self_collision():
    """Test that self collisions are detected"""
    game = SnakeGame(width=20, height=15)
    
    # Create a snake that will collide with itself
    game.snake.clear()
    game.snake.append((10, 10))
    game.snake.append((11, 10))
    game.snake.append((11, 11))
    game.snake.append((10, 11))
    game.direction = (0, 1)  # Moving down will hit position (10, 11)
    
    game.update()
    assert game.game_over
    print("✓ Self collision test passed")


def test_food_eating():
    """Test that eating food works correctly"""
    game = SnakeGame(width=20, height=15)
    
    initial_length = len(game.snake)
    initial_score = game.score
    
    # Place food in front of snake
    head_x, head_y = game.snake[0]
    game.food = (head_x + 1, head_y)
    
    game.update()
    
    assert len(game.snake) == initial_length + 1
    assert game.score == initial_score + 10
    print("✓ Food eating test passed")


def test_food_spawn():
    """Test that food spawns in valid positions"""
    game = SnakeGame(width=20, height=15)
    
    # Food should not spawn on snake or walls
    food_x, food_y = game.food
    assert food_x > 0 and food_x < game.width - 1
    assert food_y > 0 and food_y < game.height - 1
    assert game.food not in game.snake
    print("✓ Food spawn test passed")


def run_all_tests():
    """Run all tests"""
    print("\nRunning Snake Game Tests...\n")
    
    try:
        test_game_initialization()
        test_snake_movement()
        test_direction_change()
        test_wall_collision()
        test_self_collision()
        test_food_eating()
        test_food_spawn()
        
        print("\n" + "=" * 40)
        print("All tests passed! ✓")
        print("=" * 40 + "\n")
        return True
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}\n")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}\n")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
