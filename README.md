# Pokémon CLI App

## Overview

The Pokémon CLI App is a command-line application that utilizes the PokéAPI to fetch and display Pokémon information, including its type(s) and effectiveness against other types. It is structured into separate classes and files (`pokemon.py`, `type.py`, and `effectiveness.py`) for easy maintainability and scalability.

### Key Features

- Fetch and display a Pokémon's type(s).
- Check type effectiveness for attack and defense types.
- Modular structure with separate classes for Pokémon and Type management.
- Error handling for invalid inputs or API issues.

## Project Requirements

This project is developed using Python 3.8+ and utilizes the following libraries:

- **`requests`**: To handle API requests.
  
## Installation & Setup Guide

### 1. **Clone the Repository**
First, clone the repository to your local machine:

```bash
git clone https://github.com/Dtn2901/Pokemon_Weakness_Explorer_App.git
cd Pokemon_Weakness_Explorer_App
```

### 2. **Set Up a Virtual Environment**

Create and activate a virtual environment to manage dependencies:

```bash
# Create the virtual environment
python -m venv env

# Activate the environment (Windows)
.\env\Scripts\activate

# Activate the environment (macOS/Linux)
source env/bin/activate
```

### 3. **Install Dependencies**

Install all the required packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. **Run the Application**

After setting up the environment and installing the dependencies, you can run the main script:

```bash
python main.py
```

## How to Use

- **To get information about a Pokémon**, enter the Pokémon's name:
  
  Example: `Pikachu`
  
- **To evaluate type effectiveness**, enter a Pokémon's name followed by an attack type:
  
  Example: `Charmander water`
  
- **To exit the application**, type `exit`.

## Directory Structure

```plaintext
pokemon_cli_app/
├── env/                     # Virtual environment directory
├── effectiveness.py         # Class for type effectiveness calculations
├── main.py                  # Main application script
├── pokemon.py               # Class for handling Pokémon attributes
├── requirements.txt         # Dependency file
└── type.py                  # Class for handling type details
```

## Error Handling & Best Practices

- **Invalid Pokémon or Type Name:** The application will display a friendly error message if an invalid Pokémon name or type is entered.
- **API Connection Issues:** If the API is unreachable, the application will notify the user and suggest checking their network connection.
- **Modular Design:** Each class handles its specific functionality, making it easy to maintain and extend.

## Legal & Ethical Considerations

This project uses the [PokéAPI](https://pokeapi.co/) under the PokéAPI License. Ensure that any use of this app follows the API’s terms and does not violate their rate limits or terms of service.

- **Third-Party Libraries:** The app uses the `requests` library, which is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). This license allows for open use but requires proper attribution.
- **Privacy Considerations:** This app does not collect or store user data. All interactions are limited to retrieving data from external APIs.
... (14 lines left)
