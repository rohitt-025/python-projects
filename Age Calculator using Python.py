import datetime

# Get the current date and time.
now = datetime.datetime.now()

# Get the user's birth date.
birth_date = input("Enter your birth date (YYYY-MM-DD): ")

# Convert the birth date to a datetime object.
birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

# Calculate the age in years.
age_in_years = now.year - birth_date.year

# Calculate the age in months.
age_in_months = now.month - birth_date.month

# Calculate the age in days.
age_in_days = now.day - birth_date.day

# Print the user's age.
print("You are {} years, {} months, and {} days old.".format(age_in_years, age_in_months, age_in_days))

# Print the user's birth month.
print("You were born in {}.".format(birth_date.month))

# Print the user's birth day.
print("You were born on {}.".format(birth_date.day))
