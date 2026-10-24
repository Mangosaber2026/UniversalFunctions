# VS Code Editor Configuration

This directory contains my personal Visual Studio Code configuration, including custom syntax highlighting, semantic token colors, bracket-pair colorization, and other editor appearance settings.

The configuration is intended for developers who wish to use the same visual styling when exploring and developing the UniversalFunctions package.

## Contents

- `vscode_settings.json` — The complete JSON configuration containing my custom editor settings.

## Installation

1. Open Visual Studio Code.
2. Open the Command Palette using `Ctrl+Shift+P`.
3. Search for **Preferences: Open User Settings (JSON)** and select it.
4. Open `vscode_settings.json` from this directory.
5. Copy the settings into your existing VS Code `settings.json`, merging them with your current configuration rather than replacing the entire file.
6. Save the changes and inspect the editor to see the configuration in effect.

## Requirements and Compatibility

- Visual Studio Code must be installed.
- Python language support and the appropriate language extensions may be required for some Python-specific highlighting rules.
- The appearance of certain colors depends on the active color theme and whether semantic highlighting is supported.
- Some settings may override existing editor preferences.

## Customization

Feel free to adapt the configuration to your own preferences. You can change the color values, font styles, and other supported settings to suit your development environment.

This configuration is provided as a convenience and is entirely optional. You do not need to install it to use UniversalFunctions.