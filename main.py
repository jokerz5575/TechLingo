import json

# Function to load the glossary from a JSON file
def load_glossary():
    try:
        with open("glossary.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save the glossary to a JSON file
def save_glossary(glossary):
    with open("glossary.json", "w") as file:
        json.dump(glossary, file)

# Function to add a new term to the glossary
def add_term(glossary):
    term = input("Enter the technical term: ")
    definition = input("Enter the definition: ")
    glossary[term.lower()] = definition
    save_glossary(glossary)
    print(f"Term '{term}' added to the glossary.")

# Function to search for a term in the glossary
def search_term(glossary):
    term = input("Enter the technical term you want to search for: ")
    definition = glossary.get(term.lower())
    if definition:
        print(f"Definition of '{term}': {definition}")
    else:
        print(f"'{term}' not found in the glossary.")

# Main function
def main():
    print("Welcome to TechLingo - Tech Jargon Buster!")
    glossary = load_glossary()

    while True:
        print("\nMenu:")
        print("1. Add a new term to the glossary")
        print("2. Search for a term in the glossary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_term(glossary)
        elif choice == "2":
            search_term(glossary)
        elif choice == "3":
            print("Exiting TechLingo - Tech Jargon Buster.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
