#Program 1

print("Enter Personal Information")
full_name = input("Full name: ")
age = int(input("Age: "))
address = input("Address: ")
birthday = input("Birthday: ")
height = input("Height: ")
weight = input("Weight: ")
nationality = input("Nationality: ")
music_genre = input("Music genre: ")
hobby = input("Hobby: ")

info = (
    f"Full Name: {full_name}/n"
    f"Age: {age}/n"
    f"Address: {address}/n"
    f"Birthday: {birthday}/n"
    f"Height: {height}/n"
    f"Weight: {weight}/n"
    f"Nationality: {nationality}/n"
    f"Music genre: {music_genre}/n"
    f"Hobby: {hobby}/n/n"
)

with open("personal_info.txt", "a") as info_file:
    info_file.write(info)