#Program 2

while True:
    filename = "personal_info.txt"
    search_full_name = input("Enter full name to search: ")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        found = False
        info = ""


        for line in lines:
            if f"Full Name: {search_full_name}" in line:
                found = True
            if found:
                info += line
                if line.strip() ==  "":
                    break

        if found:
            print("Information found: ")
            print(info)
        else:
            print(f"No information found for {search_full_name}")
    except FileNotFoundError:
        print(f"The file {search_full_name} is not found")