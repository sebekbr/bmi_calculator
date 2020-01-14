print("KALKULATOR BMI")
print("~~~~~~~~~~~~~~")
print("Podaj wymagane dane. Pamiętaj aby zamiast przecinka (,) stosować kropkę (.)")

height = input("Podaj wzrost w [m]: ")

weight = input("Podaj wagę w [kg]: ")

# konwersja string do float
floatHeight = float(height)
floatWeight = float(weight)

bmi = floatWeight / (floatHeight * floatHeight)

print(round(bmi,2)) # round zaokrągla liczbę do dwóch miejsc

if bmi < 18.5:
    print("Niedowaga!")
elif bmi > 18.5 and bmi < 24.99:
    print("Waga normalna")
elif bmi > 25 and bmi < 29.99:
    print("Nadwaga")
elif bmi > 30 and bmi < 34.99:
    print("Otyłość 1 stopnia")
elif bmi > 35 and bmi < 34.99:
    print("Otyłość 2 stopnia")
elif bmi > 40:
    print("Otyłość 3 stopnia")
else:
    print("Error!")