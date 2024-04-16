"""
This module calculates the Human Development Index (HDI) for a country based on its life
expectancy, education, and GNI.

The HDI is a measure of well-being and is calculated as the geometric mean of normalized
indices for life expectancy, education, and GNI.

The normalization process involves converting each input variable into an index between 0 and
1, with 0 representing the lowest value observed historically and 1 representing the highest
value observed historically.

The formula for calculating the HDI is:
HDI = (life_exp_index * edu_index * gni_index)^(1/3)

Where:
- life_exp_index: Normalized index for life expectancy
- edu_index: Normalized index for education (average of expected years of schooling and mean
  years of schooling)
- gni_index: Normalized index for GNI (Gross National Income)

The module provides a function 'calculate_index' that takes the country's name, life
expectancy, expected years of schooling, mean years of schooling, and GNI as input, and prints
out the calculated indices and HDI for the country.

Example usage:
    calculate_index("Country", 75, 16, 12, 50000)
"""

import math

MIN_LIFE, MIN_SCH, MIN_MEAN, MIN_GNI = 20, 0, 0, 100
MAX_LIFE, MAX_SCH, MAX_MEAN, MAX_GNI = 85, 18, 15, 75000

def calculate_index(country_name, life_exp, exp_sch_years, mean_sch_years, gni):
    """
    Calculate the Human Development Index (HDI) for a country.

    :param country_name: Name of the country
    :param life_exp: Life expectancy in years
    :param exp_sch_years: Expected years of schooling
    :param mean_sch_years: Mean years of schooling
    :param gni: Gross National Income (GNI)
    :return: None
    """

    life_exp_index = (life_exp - MIN_LIFE) / (MAX_LIFE - MIN_LIFE)
    exp_sch_index = (exp_sch_years - MIN_SCH) / (MAX_SCH - MIN_SCH)
    mean_sch_index = (mean_sch_years - MIN_MEAN) / (MAX_MEAN - MIN_MEAN)
    gni_index = (math.log(gni) - math.log(MIN_GNI)) / (math.log(MAX_GNI) - math.log(MIN_GNI))
    edu_index = (exp_sch_index + mean_sch_index) / 2

    hdi = math.cbrt(life_exp_index * edu_index * gni_index)

    print(f"Life expectancy index for {country_name} is {life_exp_index:.4f}.")
    print(f"Education index for {country_name} is {edu_index:.4f}.")
    print(f"GNI index for {country_name} is {gni_index:.4f}.")
    print(f"HDI for {country_name} is {hdi:.3f}.")
    print(f"HDI for {country_name} is high: {hdi > 0.7}.")
    print(f"The worst index for {country_name} is {min(life_exp_index, gni_index, edu_index):.4f}.")

if __name__ == "__main__":
    country = input("Enter country name: ")
    life = float(input("Enter life expectancy: "))
    exp_sch = float(input("Enter expected years of schooling: "))
    mean_sch = float(input("Enter mean years of schooling: "))
    country_gni = float(input("Enter GNI: "))

    calculate_index(country, life, exp_sch, mean_sch, country_gni)
