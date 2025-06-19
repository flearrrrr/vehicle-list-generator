# Vehicle List Generator

A simple Python script that generates a Lua vehicle list for QB-Core from folder names inside a selected directory. The script uses a GUI folder selector for convenience.

## Features

- Select a folder containing vehicle model folders via a GUI dialog.
- Automatically scans the folder names and creates Lua entries for each vehicle.
- Saves the output to `vehicles_output.lua` inside the selected folder.
- Removes existing output file before generating a new one.
- Provides simple status messages and progress info.

## Requirements

- Python 3.13
- Tkinter (usually included with standard Python installations)

## Usage

1. Clone this repository or download the `generator.py` file.
2. Run the script:
    ```bash
    python generator.py
    ```
3. A folder selection dialog will open. Choose the folder that contains vehicle folders.
4. The script will generate a `vehicles_output.lua` file with vehicle entries based on folder names.

## Example Output

```lua
{ model = 'modelname', name = 'MODELNAME', brand = 'Dev Testing', price = 10000, category = 'imports', type = 'automobile', shop = 'luxury' },
