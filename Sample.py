import os

# Map: 1 = floor, . = hole, X = goal
# Using characters for text-based rendering
grid = [
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,2,1,1,1],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,0,0]
]

block = {
    "x": 2,
    "y": 0,
    "orientation": "standing"
}

def get_cells():
    x, y = block["x"], block["y"]
    if block["orientation"] == "standing":
        return [(x, y)]
    elif block["orientation"] == "horizontal":
        return [(x, y), (x + 1, y)]
    else: # vertical
        return [(x, y), (x, y + 1)]

def draw():
    # Clear console (works on Windows/Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("--- BLOXORZ MINI (Console) ---")
    print("Controls: W (Up), S (Down), A (Left), D (Right), Q (Quit)\n")
    
    block_cells = get_cells()
    
    for y, row in enumerate(grid):
        line = ""
        for x, val in enumerate(row):
            if (x, y) in block_cells:
                line += " B "  # Block
            elif val == 2:
                line += " X "  # Goal
            elif val == 1:
                line += " . "  # Floor
            else:
                line += "   "  # Void
        print(line)
    print("\n------------------------------")

def is_valid(x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != 0

def move(dx, dy):
    x, y, o = block["x"], block["y"], block["orientation"]

    if o == "standing":
        if dx == 1: block.update(x=x+1, y=y, orientation="horizontal")
        elif dx == -1: block.update(x=x-2, y=y, orientation="horizontal")
        elif dy == 1: block.update(x=x, y=y+1, orientation="vertical")
        elif dy == -1: block.update(x=x, y=y-2, orientation="vertical")

    elif o == "horizontal":
        if dx == 1: block.update(x=x+2, y=y, orientation="standing")
        elif dx == -1: block.update(x=x-1, y=y, orientation="standing")
        elif dy != 0: block.update(x=x, y=y+dy, orientation="horizontal")

    elif o == "vertical":
        if dy == 1: block.update(x=x, y=y+2, orientation="standing")
        elif dy == -1: block.update(x=x, y=y-1, orientation="standing")
        elif dx != 0: block.update(x=x+dx, y=y, orientation="vertical")

    # Check state after move
    for cx, cy in get_cells():
        if not is_valid(cx, cy):
            draw()
            print("GAME OVER: You fell off!")
            return False
            
    if block["orientation"] == "standing" and grid[block["y"]][block["x"]] == 2:
        draw()
        print("CONGRATULATIONS: You Win!")
        return False
        
    return True

# Main Game Loop
running = True
while running:
    draw()
    cmd = input("Move: ").lower()
    
    if cmd == 'q':
        break
    elif cmd == 'w': running = move(0, -1)
    elif cmd == 's': running = move(0, 1)
    elif cmd == 'a': running = move(-1, 0)
    elif cmd == 'd': running = move(1, 0)
