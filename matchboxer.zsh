#!/bin/zsh
# install_matchbox_zsh.sh
# Zsh-specific installer for Matchbox v2

# ----------------------
# Config
# ----------------------
INSTALL_DIR="$HOME/tools"
MATCHBOX_FILE="matchbox.py"
DEST="$INSTALL_DIR/matchbox"

echo "🚀 Matchbox v2 Installer for Zsh"

# ----------------------
# Install function
# ----------------------
install_matchbox() {
    # Check for Python 3
    if ! command -v python3 &> /dev/null; then
        echo "❌ Python 3 is required. Install it first."
        exit 1
    fi

    # Create tools directory if missing
    mkdir -p "$INSTALL_DIR"

    # Copy Matchbox
    cp "$MATCHBOX_FILE" "$DEST"

    # Make executable
    chmod +x "$DEST"

    # Add to PATH in .zshrc if not already
    if ! grep -q "$INSTALL_DIR" "$HOME/.zshrc"; then
        echo "export PATH=\$PATH:$INSTALL_DIR" >> "$HOME/.zshrc"
        echo "✅ Added $INSTALL_DIR to PATH in .zshrc"
    fi

    echo "✅ Matchbox installed! Restart your terminal or run 'source ~/.zshrc'"
    echo "Try it: matchbox cwd"
}

# ----------------------
# Uninstall function
# ----------------------
uninstall_matchbox() {
    echo "⚠️ Uninstalling Matchbox..."
    rm -f "$DEST"
    echo "✅ Matchbox executable removed"

    # Remove PATH entry from .zshrc
    sed -i '' "/$INSTALL_DIR/d" "$HOME/.zshrc"
    echo "✅ Removed PATH from .zshrc (restart terminal)"
}

# ----------------------
# Update function
# ----------------------
update_matchbox() {
    echo "🔄 Updating Matchbox..."
    if [ -f "$MATCHBOX_FILE" ]; then
        cp "$MATCHBOX_FILE" "$DEST"
        chmod +x "$DEST"
        echo "✅ Matchbox updated!"
    else
        echo "❌ matchbox.py not found in current directory"
    fi
}

# ----------------------
# Parse argument
# ----------------------
case "$1" in
    install)
        install_matchbox
        ;;
    uninstall)
        uninstall_matchbox
        ;;
    update)
        update_matchbox
        ;;
    *)
        echo "Usage: $0 {install|uninstall|update}"
        exit 1
        ;;
esac
