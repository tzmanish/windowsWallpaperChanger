# Change Windows10 wallpaper

This script downloads a random, high resolution, landscape Image from [unsplash.com](https://unsplash.com/wallpapers) with query string `wallpaper` and sets it as current wallpaper.

## Requirements

* Windows 10
* Python 3
* Python requests module

## How to run

1. Install Python 3 (if not already installed)
    * [official python website](https://www.python.org/downloads/)
2. Install requests module (For making HTTP requests)
    * Execute `python -m pip install requests` in Powershell.
3. Run the script\
    * Open powershell in containing directory,
    * Execute `python .\windowsWallpaperChanger.py`.

## Setting as scheduled task

1. Open task scheduler,
    * Open `Run` dialogue (Windoes + R),
    * Run `taskschd.msc`.
2. Create a new task with following specifications:
    * Name: `wallpaper changer`
    * Goto `Triggers > New... > Repeat task every`,
        * check the checkbox,
        * set desired interval.
    * Goto `Actions > New... > Start a program`,
        * Program/script: `powershell.exe`,
        * Add Arguments: `-nologo -windowstyle Hidden python .\windowsWallpaperChanger.py`,
        * Start in: *Full path of script's parent directory*.
    * Goto `Conditions` tab,
        * Uncheck `Start the task only if the computer is on AC power`.
        * Check `Start only if the following network connection is available` and select `Any connection` from dropdown.
3. Leave all other fields as default and save.
