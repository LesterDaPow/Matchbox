# Matchbox CLI Toolbox v2 – Documentation

**Version:** 2  
**Platform:** macOS / Zsh compatible  
**Author:** Elijah  

---

## Overview

Matchbox is a lightweight CLI toolbox for macOS that provides a variety of utility commands for file management, system information, networking, weather, search, and more.  

All commands are standalone; there is **no menu system**.  

---

## Installation

### Option 1: Manual

1. Place `matchbox.py` in a folder of your choice (e.g., `~/tools`).  
2. Make it executable:

\```bash
chmod +x ~/tools/matchbox.py
\```

3. Add it to your PATH (example for Zsh):

\```bash
echo 'export PATH=$PATH:~/tools' >> ~/.zshrc
source ~/.zshrc
\```

4. Test:

\```bash
matchbox cwd
\```

---

### Option 2: Zsh Installer (`matchboxer.zsh`)

The `matchboxer.zsh` script provides a simple Zsh-specific installer for Matchbox v2. It can **install, uninstall, or update** Matchbox easily.  

#### Usage

\```bash
./matchboxer.zsh install    # Install Matchbox
./matchboxer.zsh uninstall  # Uninstall Matchbox
./matchboxer.zsh update     # Update Matchbox to latest local version
\```

#### Features

- Checks for Python 3 before installing.
- Creates `~/tools` directory if missing.
- Copies `matchbox.py` to `~/tools/matchbox`.
- Makes it executable.
- Adds the install directory to PATH in `.zshrc` if not already present.
- Provides clear emoji feedback during install/uninstall/update.
- Safe uninstall removes executable and PATH entry from `.zshrc`.

> After installation, restart your terminal or run `source ~/.zshrc` to apply PATH changes.  

---

## Usage

\```bash
matchbox <command> [arguments]
\```

---

## Commands

### Basic

| Command | Description | Example |
|---------|------------|---------|
| `cwd` | Show the current working directory | `matchbox cwd` |
| `ls` | List files in current directory | `matchbox ls` |
| `sysinfo` | Display formatted system information | `matchbox sysinfo` |
| `ping <host>` | Ping a host 4 times | `matchbox ping github.com` |

---

### Calculator

| Command | Description | Example |
|---------|------------|---------|
| `calc "<expression>"` | Evaluate a mathematical expression | `matchbox calc "2+2*5"` |

---

### Weather

| Command | Description | Example |
|---------|------------|---------|
| `weather <city>` | Show **short** weather forecast for a city | `matchbox weather "North Salt Lake"` |

> Supports spaces in city names automatically. Output is a one-line forecast.

---

### Networking

| Command | Description | Example |
|---------|------------|---------|
| `ip` | Show local and public IP | `matchbox ip` |
| `search <query>` | Open Google search for a query | `matchbox search funny cats` |

---

### File Management

| Command | Description | Example |
|---------|------------|---------|
| `take <filename>` | Create an empty file | `matchbox take test.txt` |
| `del <filename>` | Delete a file | `matchbox del test.txt` |

---

### System Tools

| Command | Description | Example |
|---------|------------|---------|
| `ps` | List running processes | `matchbox ps` |
| `disk` | Show disk usage | `matchbox disk` |
| `whoami` | Display current user | `matchbox whoami` |

---

## Notes

- All commands are **single-line, standalone**, and work without menus.  
- Weather uses **wttr.in**; requires internet connection.  
- System info is formatted for readability: OS, hostname, kernel, architecture.  
- Works best in **Zsh** or any modern macOS terminal.  
- Zsh installer simplifies setup and PATH management.  

---
