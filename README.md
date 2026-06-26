# 🐾 pocket-creatures

> **A cozy little virtual pet game that lives in your terminal.**
> Adopt a creature, keep it happy, and watch it grow — all from your command line!

---

```
  /\_/\    (\(\ 
 ( o.o )   ( -.-)
  > ^ <    o_(")(")

  Your new best friend is waiting...
```

---

[![PyPI version](https://badge.fury.io/py/pocket-creatures.svg)](https://pypi.org/project/pocket-creatures/)
----

## 📖 What Is pocket-creatures?

**pocket-creatures** is a terminal-based virtual pet game written in Python. You adopt a creature, give it a name, and take care of it by feeding it, playing with it, and putting it to sleep. Your pet has real stats — hunger, happiness, health, and energy — that change over time. Neglect your creature and it'll get grumpy; shower it with attention and it'll thrive!

Random events keep things interesting: your pet might find a treasure, catch a cold, or learn a new trick when you least expect it.

**Perfect for:**
- Python beginners who want a fun first project to install and run
- Anyone who misses the Tamagotchi era
- People who spend a lot of time in the terminal and want some company

---

## ✨ Features

- 🐱 **Multiple creature types** — each with unique ASCII art and personality
- 📊 **Real-time stats** — track Hunger, Happiness, Health, and Energy at a glance
- 🎲 **Random events** — surprises that keep every session fresh
- 💾 **Auto-save** — your pet's progress is saved automatically when you quit
- 🎨 **ASCII art animations** — your creature reacts visually to its mood
- 🏆 **Milestones & aging** — watch your creature grow through life stages
- 🩺 **Status effects** — pets can get sick, tired, or extra-hyper
- 🌈 **Colourful terminal UI** — works on Windows, macOS, and Linux

---

## 🖥️ Before You Begin: What You'll Need

Don't worry if you've never run a Python program before — this section walks you through everything step by step.

### 1. Check if Python is Installed

Open your terminal (instructions below) and type:

```bash
python --version
```

or, on some systems:

```bash
python3 --version
```

You should see something like `Python 3.8.0` or higher. **pocket-creatures requires Python 3.8 or newer.**

> **How to open a terminal:**
> - **Windows:** Press `Win + R`, type `cmd`, press Enter. Or search for "Command Prompt" or "Windows Terminal" in the Start Menu.
> - **macOS:** Press `Cmd + Space`, type "Terminal", press Enter.
> - **Linux:** Press `Ctrl + Alt + T`, or search for "Terminal" in your app launcher.

### 2. Install Python (if needed)

If you got an error like `'python' is not recognized` or your version is below 3.8:

1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click the big yellow **"Download Python"** button
3. Run the installer
4. ⚠️ **Windows users:** On the first screen of the installer, make sure to tick the box that says **"Add Python to PATH"** before clicking Install!
5. Close and reopen your terminal, then check `python --version` again

---

## 📦 Installation

Once Python is ready, installing pocket-creatures is just one command!

```bash
pip install pocket-creatures
```

> **What is `pip`?** It's Python's package manager — a tool that downloads and installs Python programs from the internet automatically. It comes bundled with Python.

If you see a "permission denied" error, try:

```bash
pip install --user pocket-creatures
```

### Upgrading to the Latest Version

Already have it installed and want the newest version?

```bash
pip install --upgrade pocket-creatures
```

### Verifying the Installation

After installing, confirm it worked by checking the version:

```bash
pocket-creatures --version
```

You should see a version number printed. If you do — you're all set! 🎉

---

## 🚀 Running the Game

Starting pocket-creatures is simple. In your terminal, type:

```bash
pocket-creatures
```

The game will launch directly in your terminal window. On your **very first run**, you'll be greeted with a welcome screen and asked to:

1. **Choose your creature type** — pick the one that calls to you!
2. **Give your creature a name** — make it personal 🐾
3. **Watch your adventure begin**

> **Tip:** Make your terminal window a bit wider and taller for the best experience. Aim for at least 80 columns × 24 rows.

### Alternative Launch Commands

```bash
# You can also run it as a Python module if the command isn't found:
python -m pocket_creatures

# Or with python3 specifically:
python3 -m pocket_creatures
```

---

## 🎮 How to Play

### The Main Screen

When you launch the game, you'll see your creature displayed with ASCII art in the centre of the screen. Around it you'll find:

```
╔══════════════════════════════════╗
║  🐾 Biscuit  |  Age: 3 days     ║
╠══════════════════════════════════╣
║                                  ║
║         /\_/\                    ║
║        ( ^.^ )    "I'm hungry!"  ║
║         > ~ <                    ║
║                                  ║
╠══════════════════════════════════╣
║  ❤  Health    ████████░░  80%   ║
║  😊 Happiness ██████░░░░  60%   ║
║  🍖 Hunger    ████░░░░░░  40%   ║
║  ⚡ Energy    ██████████  100%  ║
╠══════════════════════════════════╣
║  [F]eed  [P]lay  [S]leep  [Q]uit ║
╚══════════════════════════════════╝
```

### Controls & Commands

Press a key at any time — **no need to press Enter** after single-letter commands!

| Key | Action | Effect on your pet |
|-----|--------|--------------------|
| `F` | **Feed** | Reduces hunger, slightly increases happiness |
| `P` | **Play** | Boosts happiness and energy (costs some hunger) |
| `S` | **Sleep** | Restores energy and health (pet is unavailable while sleeping) |
| `M` | **Medicine** | Cures sickness (only appears when your pet is ill) |
| `C` | **Clean** | Cleans up your pet's space, boosts happiness |
| `I` | **Info** | Shows detailed stats and your creature's history |
| `H` | **Help** | Displays an in-game help screen |
| `Q` | **Quit** | Saves your game and exits |

> **Keyboard shortcut tip:** You can also use the **arrow keys** to navigate menus and press **Enter** to confirm selections.

---

## 📊 Understanding Your Pet's Stats

Your creature has four core stats. They all change over time, so check in regularly!

### ❤️ Health (0–100)
Your pet's overall wellbeing. Health drops slowly when your pet is hungry or exhausted for too long. Give medicine when sick.
- **80–100:** Thriving
- **50–79:** Doing okay
- **20–49:** Needs attention
- **0–19:** Critical — act fast!

### 😊 Happiness (0–100)
How cheerful your creature is. It drops when your pet is ignored, hungry, or sick.
- Play with your pet and keep it fed to maintain high happiness.
- A very unhappy pet may refuse to eat or play.

### 🍖 Hunger (0–100)
How hungry your pet is — **higher is hungrier.** Feed your pet before this gets too high!
- Hunger rises steadily over time.
- At 80+, your pet starts losing health.
- At 100, your pet is starving — health drops quickly.

### ⚡ Energy (0–100)
How energetic your creature is. Playing costs energy; sleeping restores it.
- At low energy, your pet becomes sluggish and won't want to play.
- At 0, your pet falls asleep automatically.

---

## 🎲 Random Events

Life with your creature is full of surprises! Random events can happen any time you interact with your pet. Some are good, some are bad — all are part of the adventure.

**Examples of events you might encounter:**

| Event | Description |
|-------|-------------|
| 🎁 **Found a treasure!** | Your pet discovered a shiny object — happiness boost! |
| 🤧 **Caught a cold** | Your pet is sick and needs medicine |
| ✨ **Learned a trick!** | Your creature discovered a new skill |
| ⛈️ **Stormy night** | Bad weather made your pet anxious — happiness drops |
| 🌟 **Extra energetic** | Your pet is buzzing with energy today |
| 💤 **Feeling extra sleepy** | Your pet needs more rest than usual |

> Events are displayed as a pop-up message on screen. Read them carefully — some require action from you!

---

## 🌱 Creature Life Stages

Your creature grows and changes over time. Each life stage brings new ASCII art and behaviors:

| Stage | Age | Description |
|-------|-----|-------------|
| 🥚 **Egg** | Day 0 | Your adventure begins! |
| 🐣 **Baby** | Days 1–2 | Tiny and needy — check in often |
| 🐾 **Young** | Days 3–6 | Playful and curious |
| 🌟 **Adult** | Days 7–13 | Well-rounded and independent |
| 👑 **Elder** | Day 14+ | Wise and a little slower-paced |

---

## 💾 Saving & Loading

pocket-creatures **automatically saves your progress** whenever you quit with `Q`. The next time you launch the game, your pet will be right where you left it.

### Where is my save file?

| Operating System | Save file location |
|---|---|
| Windows | `C:\Users\YourName\AppData\Local\pocket_creatures\` |
| macOS | `~/Library/Application Support/pocket_creatures/` |
| Linux | `~/.local/share/pocket_creatures/` |

> **Note:** `~` means your home folder. `YourName` is your Windows username.

### Backing Up Your Pet

Want to keep your save safe? Copy the `save.json` file from the folder above to a safe place. To restore it, just copy it back.

---

## 🛠️ Troubleshooting

### "pocket-creatures: command not found"

This usually means Python's script folder isn't in your system's PATH. Try these alternatives:

```bash
python -m pocket_creatures
# or
python3 -m pocket_creatures
```

**Permanent fix on Windows:**
1. Search for "Environment Variables" in the Start Menu
2. Click "Edit the system environment variables"
3. Click "Environment Variables…"
4. Under "User variables", find `Path` and click Edit
5. Add `%APPDATA%\Python\Python3x\Scripts` (replace `3x` with your Python version number, e.g. `312`)
6. Restart your terminal

---

### "pip: command not found"

Try using `pip3` instead:

```bash
pip3 install pocket-creatures
```

Or invoke pip through Python directly:

```bash
python -m pip install pocket-creatures
# or
python3 -m pip install pocket-creatures
```

---

### The ASCII art looks broken or garbled

Your terminal may not support Unicode characters fully. Try:

1. **Windows:** Use **Windows Terminal** (download free from the Microsoft Store) instead of the classic Command Prompt
2. **All platforms:** Make sure your terminal's font is set to a monospace font like `Consolas`, `Courier New`, or `Fira Code`
3. Set your terminal's encoding to UTF-8:
   ```bash
   # Windows Command Prompt only:
   chcp 65001
   ```

---

### Colors aren't showing / terminal looks plain

Some older terminals don't support colors. pocket-creatures detects this automatically and falls back to plain text. For the best experience, use:
- **Windows:** Windows Terminal or VS Code's integrated terminal
- **macOS:** The default Terminal app or iTerm2
- **Linux:** Any modern terminal emulator (gnome-terminal, konsole, alacritty, etc.)

---

### My pet's stats seem wrong after reloading

If your save file gets corrupted (this is rare!), you can reset your game:

```bash
pocket-creatures --reset
```

> ⚠️ **Warning:** This will permanently delete your current pet. Make a backup first if you want to keep your save!

---

### The game crashes on startup

1. Make sure you have Python 3.8 or newer: `python --version`
2. Try reinstalling: `pip install --upgrade --force-reinstall pocket-creatures`
3. Check if there's an error message — if so, copy the full message and open an issue on GitHub (link below)

---

## 📁 Project Structure (for the curious)

If you're a developer or just want to peek under the hood:

```
pocket_creatures/
├── __init__.py          # Package entry point
├── __main__.py          # Launch point (python -m pocket_creatures)
├── game.py              # Core game loop and logic
├── creature.py          # Creature class, stats, and life stages
├── events.py            # Random event system
├── renderer.py          # ASCII art and terminal UI rendering
├── save.py              # Save/load game state to disk
└── assets/
    └── ascii_art/       # ASCII art files for each creature and mood
```

---

## 🤝 Contributing

Found a bug? Have an idea for a new creature type or random event? Contributions are warmly welcomed!

1. Fork the repository on GitHub
2. Create a feature branch: `git checkout -b my-new-feature`
3. Make your changes and add tests if applicable
4. Open a Pull Request with a clear description of what you changed

Please be kind and constructive in all interactions — this is a friendly project!

---

## 🐛 Reporting Bugs

If something goes wrong, please open a GitHub issue and include:

- Your operating system and version (e.g. Windows 11, macOS 14, Ubuntu 24.04)
- Your Python version (`python --version`)
- Your pocket-creatures version (`pocket-creatures --version`)
- The full error message or a description of what happened
- Steps to reproduce the problem

---

## 📜 License

pocket-creatures is released under the **MIT License** — free to use, modify, and share. See `LICENSE` for full details.

---

## 🙏 Acknowledgements

- Inspired by the classic Tamagotchi virtual pets of the 1990s
- ASCII art crafted with love
- Built with ❤️ for anyone who ever wished their terminal had a little more life in it

---

<p align="center">
  Made with 🐾 &nbsp;|&nbsp; Happy creature-keeping!
</p>
