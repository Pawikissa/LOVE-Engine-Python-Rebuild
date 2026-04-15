import os

def read_board_file(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    with open(file_path, 'r') as file:
        lines = file.readlines()

    lua_code = ""
    for line in lines:
        line = line.strip()
        if line.startswith("#") or not line:
            continue  # Skip comments and empty lines
        elif line.startswith("window"):
            _, width, height = line.split()
            lua_code += f"love.window.setMode({width}, {height})\n"
        elif line.startswith("title:"):
            title = line.split(":", 1)[1].strip()
            lua_code += f"love.window.setTitle('{title}')\n"
        elif line == "end":
            break  # Stop reading further commands

    with open("main.lua", 'w') as lua_file:
        lua_file.write(lua_code)
    print("Lua code has been written to main.lua")

read_board_file("board.mot")
