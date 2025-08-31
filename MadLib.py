#MadLib.py
#Name: Pierce Limbo
#Date: 8/31/2025
#Assignment: Lab 1

def main():
    print("Madlib")

    # Ask user for words (at least 6)
    person = input("Enter a person: ")
    item_of_clothing = input("Enter an item of clothing: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    animal = input("Enter an animal: ")

    # Print the story with the user supplied words
    print("\nHere’s your story!\n")
    print(f"One day, {person} forgot to wear their {item_of_clothing} to {place}.")
    print(f"On the way, they saw a {adjective} {animal} ready to attack")
    print(f"They {verb} with fear and because they'd forgotten their {item_of_clothing} it was even more embarrassing.")

# Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
