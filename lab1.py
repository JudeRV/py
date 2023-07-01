print("What is your name?") # output - Asks the user for their name
user_name = input() # input - Prompts the user to type in their name

print(f"Hello, {user_name}. How old are you?") # output - Greets the user by name and asks them to type in their age
user_age = int(input()) # input - Prompts the user to type in their age
birth_year = 2023 - user_age # internal - performs arithmetic from user's entered age to calculate their birth year

print(f"So you were born in {birth_year}! At what age do you expect to retire?") # output - Prints the user's birth year and asks them to type in their age of retirement
user_retire_age = int(input()) # input - Prompts the user to type in their age of retirement
years_till_retire = user_retire_age - user_age # internal - Calculates the amount of years until retirement from the two ages the user entered
year_of_retire = 2023 + years_till_retire # internal - Calculates the year that the user will retire from the two ages they entered

print(f"In {years_till_retire} years. You will be retiring in {year_of_retire} then.") # output - Prints the length of time before retirement & the year of retirement