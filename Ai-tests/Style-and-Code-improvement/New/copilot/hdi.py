"""
HDI Calculation

This script calculates the HDI (Human Development Index) for a given country based on various
indicators such as life expectancy, education, and gross national income (GNI).

Inputs:
- country_name: The name of the country
- life_exp: The life expectancy in years
- exp_sch_years: The expected years of schooling
- mean_sch_years: The mean years of schooling
- gni: The gross national income

Outputs:
- life_exp_index: The normalized life expectancy index
- edu_index: The average of the normalized expected years of schooling index and mean years of
    schooling index
- gni_index: The normalized GNI index
- hdi: The calculated HDI
- min_index: The worst index among life expectancy, education, and GNI

The HDI is a measure of human development that takes into account factors related to health,
education, and standard of living. It provides a summary of a country's overall development level.
"""

from math import cbrt, log


country_name = input()
life_exp = float(input())
exp_sch_years = float(input())
mean_sch_years = float(input())
gni = float(input())

MIN_LIFE, MIN_SCH, MIN_MEAN, MIN_GNI = 20, 0, 0, 100
MAX_LIFE, MAX_SCH, MAX_MEAN, MAX_GNI = 85, 18, 15, 75000

life_exp_index = (life_exp - MIN_LIFE) / (MAX_LIFE - MIN_LIFE)
exp_sch_index = (exp_sch_years - MIN_SCH) / (MAX_SCH - MIN_SCH)
mean_sch_index = (mean_sch_years - MIN_MEAN) / (MAX_MEAN - MIN_MEAN)

log_max_gni = log(MAX_GNI)
log_min_gni = log(MIN_GNI)
gni_index = (log(gni) - log_min_gni) / (log_max_gni - log_min_gni)

edu_index = (exp_sch_index + mean_sch_index) / 2
hdi = cbrt(life_exp_index * edu_index * gni_index)

min_index = min(life_exp_index, gni_index, edu_index)

print(f"Life expectancy index for {country_name} is {life_exp_index:.4f}.\n"
    f"Education index for {country_name} is {edu_index:.4f}.\n"
    f"GNI index for {country_name} is {gni_index:.4f}.\n"
    f"HDI for {country_name} is {hdi:.3f}.\n"
    f"HDI for {country_name} is high: {hdi > 0.7}.\n"
    f"The worst index for {country_name} is {min_index:.4f}.")
