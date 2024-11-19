#Program 1

while True:
    print("Enter Personal Information")
    while True:
        full_name = input("Full name: ")
        if len(full_name.split()) >= 2 and all(char.isalpha() or char in [" ", "'", "-", "."] for char in full_name):
            break 
        else:
            print("Error: Name must be a full name containing at least two words, with alphabetic characters, spaces, apostrophes, period, or hyphens.")

    while True:
        try:
            age = int(input("Age: "))
            if 0 <= age <= 120:
                break 
            else:
                print("Error: Age must be a number between 0 and 120.")

        except ValueError:
            print("Error: Age must be a valid number.")

    address = input("Address: ")

    while True:
        birthday = input("Birthday (MM-DD-YYYY): ")
        if len(birthday) == 10:
            break
        print("Error: Enter birthday in the format MM-DD-YYYY.")

    while True:
        height = input("Height (ex. 5'7 ft or 178 cm ): ")
        if any(unit in height for unit in ["'", "cm", "ft", "m"]):
            break
        print("Error: Please input a valid height (ex. 5'6 ft, 167 cm, or 1.7 m).")

    while True:
        weight = input("Weight (ex. 75 kg or 150 lbs): ")
        if any(unit in weight for unit in ["kg", "lbs"]):
            break
        print("Error: Please input a valid weight with units (ex. 70 kg or 154 lbs).")

    nationality = input("Nationality: ")
    music_genre = input("Music genre: ")
    hobby = input("Hobby: ")

    info = (
        f"Full Name: {full_name}\n"
        f"Age: {age}\n"
        f"Address: {address}\n"
        f"Birthday: {birthday}\n"
        f"Height: {height}\n"
        f"Weight: {weight}\n"
        f"Nationality: {nationality}\n"
        f"Music genre: {music_genre}\n"
        f"Hobby: {hobby}\n\n"
    )

    with open("personal_info.txt", "a") as info_file:
        info_file.write(info)

    another_input = input("Would you like to input another informations for another person? (yes/no): ")
    if another_input == "no":
        print("Information saved!")
        break



#Program 2

filename = "personal_info.txt"
search_full_name = input("Enter full name to search: ")    