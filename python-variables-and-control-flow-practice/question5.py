
age = int(input("What is your Age: (1-100) "))

if 0 <= age <= 18:
    print(f"You are a minor: {age}")
elif 18 <= age <= 100:
    print(f"You are an Adult: {age}")
else:
    print(f"Your age {age} is outside the defined range.")

   