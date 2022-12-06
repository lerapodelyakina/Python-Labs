notes = {1:"до", 2:"ре", 3:"ми", 4:"фа", 5:"соль"}
key = int(input("Введите число"))
def music(name_dict):
    note = name_dict.get(key)
    print(note)
music(notes)
    