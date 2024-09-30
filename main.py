from pokemon import Pokemon
from effectiveness import Effectiveness

def main():
    print("Welcome to the Pokémon CLI App!")
    print("Enter a Pokémon name to get info or a Pokémon name followed by a type to check effectiveness.")

    while True:
        user_input = input("\nEnter your input (or 'exit' to quit): ").strip().lower()

        if user_input == 'exit':
            print("Exiting...")
            break

        inputs = user_input.split()

        if len(inputs) == 1:
            pokemon_name = inputs[0]
            pokemon = Pokemon(pokemon_name)
            if isinstance(pokemon.types, str) and pokemon.types.startswith("Error"):
                print(pokemon.types)
            else:
                print(pokemon)

        elif len(inputs) == 2:
            pokemon_name, attack_type = inputs
            pokemon = Pokemon(pokemon_name)
            if isinstance(pokemon.types, str) and pokemon.types.startswith("Error"):
                print(pokemon.types)
            else:
                effectiveness = Effectiveness(attack_type, pokemon.types)
                results = effectiveness.check_effectiveness()
                for defense_type, result in zip(pokemon.types, results):
                    print(f"{result} when used against {pokemon_name.capitalize()} ({defense_type.capitalize()})!")

        else:
            print("Invalid input format. Please enter a Pokémon name or a Pokémon name followed by a type.")

if __name__ == "__main__":
    main()
