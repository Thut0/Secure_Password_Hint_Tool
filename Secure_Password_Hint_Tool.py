# Secure Password Hint Tool

# Ask the user to enter their password
password = input("Enter your password: ")

# Use .strip() to clean up any accidental spaces they might have typed at the start or end
password = password.strip()

first_letter = password[0]
last_letter = password[-1]

password_hint = f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}."
print(password_hint)