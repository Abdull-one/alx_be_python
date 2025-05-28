# Prompt the user for their current age
while True:
    try:
        current_age = int(input("How old are you? "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid age.")

# Calculate the user's age in 2050
age_in_2050 = current_age + 27

# Print the user's age in 2050
print(f"In 2050, you will be {age_in_2050} years old.")


