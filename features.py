# Imports the ranking and list of countries to this program.
from rankings import *

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