import datetime

# Get the person's date of birth
dob = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.datetime.strptime(dob, '%Y-%m-%d')

# Get the expected lifespan in years
expected_lifespan = int(input("Enter your expected lifespan in years: "))

# Calculate the date of death
death_date = dob + datetime.timedelta(days=expected_lifespan*365)

# Calculate the number of weeks between now and the date of death
now = datetime.datetime.now()
weeks_until_death = (death_date - now).days // 7

print("You have approximately", weeks_until_death, "weeks left to live.")
