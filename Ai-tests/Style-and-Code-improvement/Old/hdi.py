import math

country_name, life_exp, exp_sch_years, mean_sch_years, gni = (
    input(),
    float(input()),
    float(input()),
    float(input()),
    float(input()),
)
MIN_LIFE, MIN_SCH, MIN_MEAN, MIN_GNI = 20, 0, 0, 100
MAX_LIFE, MAX_SCH, MAX_MEAN, MAX_GNI = 85, 18, 15, 75000
life_exp_index = (life_exp - MIN_LIFE) / (MAX_LIFE - MIN_LIFE)
exp_sch_index = (exp_sch_years - MIN_SCH) / (MAX_SCH - MIN_SCH)
mean_sch_index = (mean_sch_years - MIN_MEAN) / (MAX_MEAN - MIN_MEAN)
gni_index = (math.log(gni) - math.log(MIN_GNI)) / (
    math.log(MAX_GNI) - math.log(MIN_GNI)
)
edu_index = (exp_sch_index + mean_sch_index) / 2
hdi = math.cbrt(life_exp_index * edu_index * gni_index)
print(
    f"Life expectancy index for {country_name} is {life_exp_index:.4f}.\n"
    f"Education index for {country_name} is {edu_index:.4f}.\n"
    f"GNI index for {country_name} is {gni_index:.4f}.\n"
    f"HDI for {country_name} is {hdi:.3f}.\n"
    f"HDI for {country_name} is high: {hdi>0.7}.\n"
    f"The worst index for {country_name} is {min(life_exp_index,min(gni_index,edu_index)):.4f}."
)
