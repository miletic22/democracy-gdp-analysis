import pandas as pd
import matplotlib.pyplot as plt
import math

gdp_per_capita = pd.read_excel("datasets\\API_NY.GDP.PCAP.CD_DS2_en_excel_v2_5607109.xls", sheet_name="Data", header=3)
country_name = input("Country: ")
country_stats = gdp_per_capita[gdp_per_capita['Country Name'] == country_name]
years = country_stats.columns[56:].tolist()
gdp_per_capita_list = country_stats.iloc[:, 56:].values.flatten().tolist()


plt.title(f"{country_name}: GDP Per Capita 2013-2022")
plt.plot(years, gdp_per_capita_list)
plt.grid(True)
x_labels = [str(year) for year in years]  # Convert years to strings
plt.xticks(years, x_labels)
plt.xlabel("Years")
plt.ylabel("GDP Per Capita")
plt.show()