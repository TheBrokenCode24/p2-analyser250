"""
This is the main program where the user will analyze the ranking sheet.
"""

# Imports the ranking and list of countries to this program.
from rankings import ranking_2023, ranking_2024, ranking_2025, countries_2023, countries_2024, countries_2025, years_2023, years_2024, years_2025, ranking_1732_2023, ranking_1769_2024, ranking_1806_2025, countries, users2023, users2024

# Global variables for all functions to use.
num_entries = {2023: 1732, 2024: 1769, 2025: 1806}

# Function prints out the entire ranking based on averages from all users.
def entire_ranking(edition, all_rankings=[ranking_2023, ranking_2024, ranking_2025]):
    # Gets the ranking depending on the edition.
    if edition == 2023:
        ranking = all_rankings[0]
    elif edition == 2024:
        ranking = all_rankings[1]
    else:
        ranking = all_rankings[2]

    # Print statement
    print(f"\nThe Entire Ranking of ALTESC250 {edition} (All Users):")
    
    # 2023 and 2024's spreadsheet are in the same format, so they share the same print statement format.
    # 2025's spreadsheet is in a different format, so it uses a different print statement format.
    if edition == 2025:
        for n in range(4, len(ranking)):
            entry = ranking[n]
            print(f"{entry[2]}. {entry[8]} {entry[5]}: {entry[10]} - {entry[11]} - {entry[14]}")
    elif edition == 2023 or edition == 2024:
        for n in range(4, len(ranking)):
            entry = ranking[n]
            print(f"{entry[0]}. {entry[7]} {entry[3]}: {entry[10]} - {entry[11]} - {entry[14]}")

# Function prints out the entire ranking based on averages of all users who ranked all songs.
def entire_ranking_all_songs(edition, all_rankings=[ranking_1732_2023, ranking_1769_2024, ranking_1806_2025]):
    if edition == 2023:
        ranking = all_rankings[0]
    elif edition == 2024:
        ranking = all_rankings[1]
    else:
        ranking = all_rankings[2]
    print(f"\nThe Entire Ranking of ALTESC250 {edition} ({num_entries[edition]} Club):")
    if edition == 2023:
        for n in range(4, len(ranking)):
            entry = ranking[n]
            print(f"{entry[1]}. {entry[8]} {entry[4]}: {entry[11]} - {entry[12]} - {entry[16]}")
    elif edition == 2024:
        for n in range(4, len(ranking)):
            entry = ranking[n]
            print(f"{entry[1]}. {entry[8]} {entry[4]}: {entry[11]} - {entry[12]} - {entry[15]}")
    elif edition == 2025:
        for n in range(4, len(ranking)):
            entry = ranking[n]
            print(f"{entry[1]}. {entry[6]} {entry[3]}: {entry[8]} - {entry[9]} - {entry[12]}")

# Function prints out the averages of each year.
def all_year_average(ranking, edition):
    print("\nAll Years Ranked by Averages:")
    for n in range(len(ranking)):
        year = ranking[n]
        print(f"{year[0]}. {year[1]} - {year[2]}")

# Function prints out the averages of each country.
def all_country_average(ranking, edition):
    print("\nAll Countries Ranked by Averages:")
    for n in range(len(ranking)):
        country = ranking[n]
        print(f"{country[0]}. {country[2]} - {country[3]}")

# 
def print_all_users(users, edition):
    print("\nAll Participating Users:")
    for n in range(len(users)):
        users_list = list(users.keys())
        user = users_list[n]
        user_num_entries = users[user]
        print(f" - {users_list[n]}: Ranked {user_num_entries} Songs")

# Main function containing the main program.
def main():
    # Print statements
    print("\nWelcome to the Analyzer250!\n")
    print("What edition would you like to analyze the results of ALTESC250 from?")
    print(" - 2023\n - 2024\n - 2025")

    edition = int(input("Select the year: "))

    while edition not in [2023, 2024, 2025]:
        print("Select a year that is ACTUALLY from this list here!")
        print(" - 2023\n - 2024\n - 2025")
        edition = int(input("Select the year FROM THE LIST: ")) 

    print(f"What would you like to get from the ranking of ALTESC250 {edition}?\n")
    
    # Choices
    # 1. List of the top 250 of the ranking of all users.
    # 2. List of the top 250 of the ranking of all users who ranked all songs.
    # 3. List of the top 250 of the ranking of a specific user.
    print("1 - List of the top 250.")
    # 1. List of the entire ranking. (ranking.csv)
    # 2. List of the entire ranking from those who ranked all the songs (club_1769.csv).
    # 3. List of the entire ranking from a specific user (ranking.csv).
    print("2 - List of the entire ranking.")
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
    # 21. Return the list of users who participated in the ranking.

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
    if choice1 == 1:
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

    elif choice1 == 2:
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
    #     else:
    #         print_all_users()
    # elif choice1 == 3:
    #     all_year_average()
    # elif choice1 == 4:
    #     all_country_average()
    # elif choice1 == 5:
    #     pass

    
# This runs the main program.
if __name__ == "__main__":
    main()