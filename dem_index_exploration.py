import pandas as pd
import matplotlib.pyplot as plt

dem_index = pd.read_excel("datasets\\all_data_fiw_2013-2023.xlsx", sheet_name="FIW13-23", header=1)
country_name = input("Country: ")
country_stats = dem_index[dem_index['Country/Territory'].str.contains(country_name)]

years = [year for year in country_stats["Edition"]][::-1]
dem_score = [dem_score for dem_score in country_stats["Total"]][::-1]

plt.title(f"{country_name.capitalize()}: Freedom in the World Index Rating 2013-2023")
plt.plot(years, dem_score)
plt.grid(True)
plt.ylim(0, 100)
x_labels = [str(year) for year in years]  # Convert years to strings
plt.xticks(years, x_labels)
plt.yticks(range(0, 101, 5))
plt.xlabel("Years")
plt.ylabel("Democracy Index Rating")

status_years = {"F": [], "PF": [], "NF": []}

# Iterate over the rows of the dataframe
for index, row in country_stats.iterrows():
    status = row["Status"]
    year = row["Edition"]
    
    # Append the year to the corresponding status list in the dictionary
    status_years[status].insert(0, year)

# Print the resulting dictionary

# Coloring based on "Free" years
free_years = status_years["F"]
if free_years:
    first_free_year = free_years[0]
    last_free_year = free_years[-1]
    plt.fill_between(range(first_free_year, last_free_year + 2), 0, 100, color='green', alpha=0.3)

# Coloring based on "Partly Free" years
partly_free_years = status_years["PF"]
if partly_free_years:
    first_partly_free_year = partly_free_years[0]
    last_partly_free_year = partly_free_years[-1]
    plt.fill_between(range(first_partly_free_year, last_partly_free_year + 2), 0, 100, color='orange', alpha=0.3)

# Coloring based on "Not Free" years
not_free_years = status_years["NF"]
if not_free_years:
    first_not_free_year = not_free_years[0]
    last_not_free_year = not_free_years[-1]
    plt.fill_between(range(first_not_free_year, last_not_free_year + 2), 0, 100, color='red', alpha=0.3)

print(status_years)

plt.show()