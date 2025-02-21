while True:
    with open('File_Handling/names.txt', "a") as file:
        name = input("Eklemek için isim giriniz:    ")
        file.write(name + "\n")
        continueOrNot = input("Devam etmek istiyor musunuz? (e/h)")
        if continueOrNot == "h" or continueOrNot == "H":
            break

with open('File_Handling/names.txt', "r") as file:
    lines = file.readlines()

for k in lines:
    print(k.strip().capitalize())