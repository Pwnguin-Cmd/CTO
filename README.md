# Terminal Snake Game 🐍

A classic Snake game that runs in the terminal using only Python standard library. No external dependencies required!

## Features

- ✅ Pure Python implementation (standard library only)
- ✅ Works on online Python interpreters (Replit, Trinket, Google Colab, etc.)
- ✅ Simple ASCII-based graphics
- ✅ Score tracking
- ✅ Collision detection (walls and self)
- ✅ Dynamic food spawning
- ✅ Growing snake mechanic

## How to Run

### Local Machine

```bash
python snake_game.py
```

or

```bash
python3 snake_game.py
```

### Online Interpreters

#### Replit
1. Create a new Python repl
2. Copy the contents of `snake_game.py` into the main.py file
3. Click "Run"

#### Google Colab
1. Create a new notebook
2. Copy the contents of `snake_game.py` into a code cell
3. Run the cell

#### Trinket
1. Create a new Python trinket
2. Copy the contents of `snake_game.py`
3. Click "Run"

## Game Controls

- **W** or **up** - Move up
- **S** or **down** - Move down
- **A** or **left** - Move left
- **D** or **right** - Move right
- **Q** - Quit game

After typing your direction, press **Enter** to execute the move.

## Game Rules

1. **Objective**: Eat the food (`*`) to grow your snake and increase your score
2. **Movement**: The snake moves continuously in the current direction
3. **Growing**: Each food item eaten adds one segment to the snake and 10 points to your score
4. **Game Over**: The game ends when:
   - The snake hits a wall (`#`)
   - The snake collides with itself

## Game Elements

- `O` - Snake head
- `o` - Snake body
- `*` - Food
- `#` - Wall

## Example Gameplay

```
==============================
  SNAKE GAME - Score: 30
==============================

##############################
#                            #
#                            #
#         *                  #
#                            #
#                            #
#                            #
#                            #
#          Oooo              #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
#                            #
##############################

Controls: W/A/S/D or arrows (then Enter) | Q to quit
Snake length: 5
Direction: 
```

## Technical Details

- **Language**: Python 3
- **Dependencies**: None (uses only standard library)
- **Compatibility**: Works on Windows, Mac, Linux, and online Python interpreters
- **Screen Clearing**: Uses `os.system('clear')` or `os.system('cls')` with fallback for online interpreters

## Design Decisions

This implementation prioritizes **compatibility with online interpreters** over real-time gameplay. Instead of using the `curses` library (which is not available on many online platforms), the game uses:

- Standard input/output for controls
- `os.system()` for screen clearing
- Turn-based input (press Enter after each move)

This ensures the game works reliably across all platforms, including Replit, Trinket, and Google Colab.

## License

Free to use and modify!
