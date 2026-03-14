num_of_years = int(input("Enter number of years : "))
total_rainfall = 0
total_months = 0
for years in range(num_of_years):
    print(f"********** YEAR {years + 1} **********")
    for month in range(1,13):
        rainfall = float(input(f"Enter inches of rainfall for month {month} :"))
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months
print("******************************")
print("\nNumber of months :", total_months)
print("Total inches of rainfall :", total_rainfall)
print("Average rainfall per month :", average_rainfall)

