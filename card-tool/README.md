# Party Rumble Card Tool

## Overview

The Party Rumble Card Tool is a Python application designed to draw cards from various mini game decks. The tool allows users to randomly select mini games from five categories: `Knowledge`, `Sport`, `Dexterity`, `Estimation`, and `Luck`.

## Project Structure

```
card-tool
├── src
│   ├── main.py               # Entry point for the application
│   ├── decks
│   │   ├── __init__.py       # Package initialization for decks
│   │   └── deck_manager.py    Manages the mini game decks
│   ├── utils
│   │   ├── __init__.py       # Package initialization for utils
│   │   └── json_loader.py     Loads JSON data
├── data
│   └── mini_games.json       # JSON file containing mini game descriptions
├── requirements.txt          # Project dependencies
└── README.md                  Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd card-tool
   ```

2. **Install dependencies**:
   Create a virtual environment and install the required packages listed in `requirements.txt`:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the main script to start drawing cards:
   ```
   python src/main.py
   ```

## Usage

Upon running the application, you will be prompted to select a category from which to draw a mini game card. The application will then randomly select and display a mini game description from the chosen category.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.