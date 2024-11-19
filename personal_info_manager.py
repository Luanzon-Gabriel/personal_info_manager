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
    birthday = input("Birthday: ")
    height = input("Height: ")
    weight = input("Weight: ")
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