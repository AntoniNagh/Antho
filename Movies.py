thisdict = {}

thisdict["1st"] = input("What movie deserves 1st place? ")
thisdict["2nd"] = input("What movie deserves 2nd place? ")
thisdict["3rd"] = input("What movie deserves 3rd place? ")

print("\nYour top 3 favorite movies: ")
for key, value in thisdict.items():
    print(f"{key}: {value}")