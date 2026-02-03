"""
This Python file contains the ranking dataframe and the list of countries.
"""

# Imports pandas to the file.
import pandas as pd

# Set display options for rows and columns
pd.set_option('display.max_rows', None)  # None means no limit
pd.set_option('display.max_columns', None)

# If you want to control the column width:
pd.set_option('display.max_colwidth', None)

# Imports the ranking csv files and converts it to be printed out.
ranking_2023 = pd.read_csv("csv_files/2023/ranking.csv").values.tolist()
ranking_2024 = pd.read_csv("csv_files/2024/ranking.csv").values.tolist()
ranking_2025 = pd.read_csv("csv_files/2025/ranking.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
countries_2023 = pd.read_csv("csv_files/2023/countries.csv").values.tolist()
countries_2024 = pd.read_csv("csv_files/2024/countries.csv").values.tolist()
countries_2025 = pd.read_csv("csv_files/2025/countries.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
years_2023 = pd.read_csv("csv_files/2023/years.csv").values.tolist()
years_2024 = pd.read_csv("csv_files/2024/years.csv").values.tolist()
years_2025 = pd.read_csv("csv_files/2025/years.csv").values.tolist()
# Imports the ranking csv file and converts it to be printed out.
ranking_1732_2023 = pd.read_csv("csv_files/2023/club1732.csv").values.tolist()
ranking_1769_2024 = pd.read_csv("csv_files/2024/club1769.csv").values.tolist()
ranking_1806_2025 = pd.read_csv("csv_files/2025/club1806.csv").values.tolist()
# List of countries is empty, but will be appended.
countries = []
# List of all the users.
users2023 = {}
users2024 = {}

# Adds all the countries to the list of countries.
for row in ranking_2025:
    if row[7] not in countries:
        countries.append(row[7])
# Removes nan from the list, which is the first element.
countries.pop(0)

# Appends the dictionary containing the participating users and how many entries they ranked.
for k in range(17, len(ranking_2024[1])):
    us = ranking_2024[1][k]
    users2024[us] = int(ranking_2024[0][k])
