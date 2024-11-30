thisdict = {}

thisdict["Favorite Streamer"] = input("What's your favorite streamer: ")
thisdict["Age"] = input("How old is that streamer: ")
thisdict["Cars"] = input("What cars does said streamer own: ")

print("\nCurrent Streamer Information: ")
for key, value in thisdict.items():
    print(f"{key}: {value}")

update = input("\nWhould you like to update any information? ANSWER WITH yes OR no: ").lower()
if update == "yes":
    update_what = input("Streamer, Age, Cars, All: ").capitalize()
    if update_what == "Streamer":
        new_streamer = input("New streamer: ")
        thisdict["Favorite Streamer"] = new_streamer 
    elif update_what == "Age":
        new_age = input("New Age: ")
        thisdict["Age"] = new_age 
    elif update_what == "Cars":
        new_cars = input("New Cars: ")
        thisdict["Cars"] = new_cars
    elif update_what == "All":
        thisdict["Favorite Streamer"] = input("New Streamer: ")
        thisdict["Age"] = input("New Age: ")
        thisdict["Cars"] = input("New Cars: ")
    else:
        print("Invalid choice. No updates made.")

print("\nUpdated Streamer Information: ")
for key, value in thisdict.items():
    print(f"{key}: {value}")