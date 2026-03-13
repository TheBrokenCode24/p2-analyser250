"""
This is the main program where the user will analyze the ranking sheet.
"""

# Imports the ranking and list of countries to this program.
from rankings import *
# Imports the features such as printing out the top 250 of each user's 
from features import *

# Main function containing the main program.
def main():
    # Print statements
    print("\nWelcome to the Analyzer250!\n")
    print("What edition would you like to analyze the results of ALTESC250 from?")
    print(" - 2023\n - 2024\n - 2025")

    edition = int(input("Select the year: "))

    while edition not in [2023, 2024, 2025]:
        print("\nSelect a year that is ACTUALLY from this list here!")
        print(" - 2023\n - 2024\n - 2025")
        edition = int(input("Select the year FROM THE LIST: ")) 

    print(f"What would you like to get from the ranking of ALTESC250 {edition}?\n")
    
    # Choices
    if edition in [2023, 2024]:
        # 1. Return the list of users who participated in the ranking.
        # Only 
        print(f"1 - List of the users who participated in ALTESC250 {edition}")
        numbers = [n for n in range(2, 7+1)]
    else:
        numbers = [n for n in range(1, 7+1)]
    # 1. List of the top 250 of the ranking of all users.
    # 2. List of the top 250 of the ranking of all users who ranked all songs.
    # 3. List of the top 250 of the ranking of a specific user.
    print(f"{numbers[0]} - List of the top 250.")
    # 1. List of the entire ranking. (ranking.csv)
    # 2. List of the entire ranking from those who ranked all the songs (club_1769.csv).
    # 3. List of the entire ranking from a specific user (ranking.csv).
    print(f"{numbers[1]} - List of the entire ranking.")
    # 4. All years ranked by average.
    # 5. All years ranked by average from those who ranked all the songs.
    # 6. All years ranked by average of a specific user.
    # print("2 - All the years ranked by average.")
    # # 7. All the countries ranked by average.
    # # 8. All the countries ranked by average from those who ranked all the songs.
    # # 9. All the countries ranked by average of a specific user.
    # print("3 - All the countries ranked by average.")
    # # 10. All the entries from a specific year ranked.
    # # 11. All the entries from a specific year ranked from those who ranked all the songs.
    # # 12. All the entries from a specific year ranked from a specific user.
    # print("4 - All the entries from a specific year ranked.")
    # # 13. All the entries from a specific country ranked.
    # # 14. All the entries from a specific country ranked from those who ranked all the songs.
    # # 15. All the entries from a specific country ranked from a specific user.
    # print("5 - All the entries from a specific country ranked.")
    # 16. A specific entry's overall result.
    # 17. A specific entry's result on someone's ranking.
    # 18. List of a specific placement range of the ranking.
    # 19. A specific placement's entry.
    # 20. A country's highest/lowest/most average result.
    # 21. 

    # Gets user input
    choice1 = input("\nType in the number associated with the choice you want: ")
    
    # Ensures that the user enters the number listed in the choices
    while choice1 not in [str(c) for c in range(1, 6)]:
        print("That is not a number listed. Try a number listed!")
        print("Here are the choices again.\n")
        choice1 = input("Type in the number associated with the choice you want: ")
    # Else statement converts the choice into an int value.
    else:
        choice1 = int(choice1)
    
    # If statements that calls each function depending on the choice.
    if edition in [2023, 2024]:
        if choice1 == 1:
            print_all_users()
    elif choice1 == numbers[0]:
        # Print statement
        print("\nWhere would you like to get the top 250 from?")
        print("1 - All users")
        print(f"2 - All users who ranked all {num_entries[edition]} songs")
        # Due to the 2025 spreadsheet not containing the names of each user, only the organizer's ranking will be shown.
        if edition == 2025:
            print("3 - The organizer's top 250")
        else:
            print("3 - A specific user's top 250")

        # Gets user input
        choice2 = input("Type in the number associated with the choice you want: ")
        
        # Ensures that the user enters the number listed in the choices
        while choice2 not in [str(c) for c in range(1, 4)]:
            print("That is not a number listed. Try a number listed!")
            print("Here are the choices again.\n")
            choice2 = input("Type in the number associated with the choice you want: ")
        # Else statement converts the choice into an int value.
        else:
            choice2 = int(choice2)

        if choice2 == 1:
            entire_ranking(edition)
        elif choice2 == 2:
            entire_ranking_all_songs(edition)

    elif choice1 == numbers[1]:
        # Print statement
        print("\nWhere would you like to get the ranking from?")
        print("1 - All users")
        print(f"2 - All users who ranked all {num_entries[edition]} songs")
        # Due to the 2025 spreadsheet not containing the names of each user, only the organizer's ranking will be shown.
        if edition == 2025:
            print("3 - The organizer's ranking")
        else:
            print("3 - A specific user")

        # Gets user input
        choice2 = input("Type in the number associated with the choice you want: ")
        
        # Ensures that the user enters the number listed in the choices
        while choice2 not in [str(c) for c in range(1, 4)]:
            print("That is not a number listed. Try a number listed!")
            print("Here are the choices again.\n")
            choice2 = input("Type in the number associated with the choice you want: ")
        # Else statement converts the choice into an int value.
        else:
            choice2 = int(choice2)

        if choice2 == 1:
            entire_ranking(edition)
        elif choice2 == 2:
            entire_ranking_all_songs(edition)
    # elif choice1 == 4:
    #     all_year_average()
    # elif choice1 == 5:
    #     all_country_average()
    # elif choice1 == 6:
    #     pass

    
# This runs the main program.
if __name__ == "__main__":
    main()