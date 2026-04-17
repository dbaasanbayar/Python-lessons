#11 Error Handling (Алдааг удирдах: Try / Except)

# try: 
#     too = int(input("Too oruulna uu:"))
#     hariu = 100 / too
#     print(f"100-g {too}-d huwaahad: {hariu}")
# except ValueError:
#     print('Aldaa: Ta zaawal too oruulah yostoi!')
# except ZeroDivisionError: 
#     print("Aldaa: Toog 0-d huwaaj bolohgui")
# except Exception as e:
#     print(f"Genetiin aldaa garlaa: {e}")

#12 "Мастер" Тооны машин (Calculator)

# Алхам 1: Функцүүдээ бэлдэх

# def nemeh(a, b): return a + b
# def hasah(a, b): return a - b
# def urjih(a, b): return a * b
# def huwaah(a, b):
#     if b == 0:
#         return "Aldaa: 0-d huwaaj bolohgui"
#     return a / b

# while True: # Энэ нь програмыг зогсолтгүй ажиллуулна
#     print("/n--- Toonii mashin (Garahiin  tuld 'exit' gej bicheerei) ---")

#     orolt = input("Urgeljluuleh uu? (ali neg towch darah / exit): ")
#     if orolt.lower() == "exit":
#         print("Bayartai")
#         break # Давталтыг зогсооно

# # Алхам 2: Үндсэн логик (Програм эхлэх хэсэг)

#     try: 
#         too1 = float(input("1-r too: "))
#         too2 = float(input("2-r too: "))
#         uildel = input("Uildel songo (+, -, *, /): ")

#         if uildel == "+":
#             print(f"Ur dun: {too1 + too2}")
#         elif uildel == "-":
#             print(f"Ur dun: {too1 - too2}")
#         elif uildel == "*":
#             print(f"Ur dun: {too1 * too2}")
#         elif uildel == "/": 
#             if too2 == 0:
#                 print("Aldaa: 0-d huwaaj bolohgui")
#             else:
#                 print(f"Ur dun: {too1 / too2}" )
#         else: 
#             print("Buruu uildel songoloo! (+, -, *, /) ashiglana uu")

#     except ValueError: 
#         print("Buruu utga oruulsan baina. Zaaval too oruulna uu")
#     except Exception as e:
#         print(f"Genetiin aldaa garlaa: {e}")

#13. Модуль (Modules) - Бэлэн хүчийг ашиглах
        
# import datetime
# import random

# print(f"Odoogiin tsag: {datetime.datetime.now()}")
# print(f"Chinii aziin too: {random.randint(1, 100)}")

# # 14. Файл нээх, унших, бичих (File I/O)

# with open("mini_hicheel.txt", "w", encoding="utf-8") as file:
#     file.write("bi Python surch baina. \n")
#     file.write("Filetai ajillaj surah mash sonirholtoi yum!")

# with open("mini_hicheel.txt", "r", encoding="utf-8") as file:
#     aguulga = file.read()
#     print(aguulga)

# with open ("mini_hicheel.txt", "a", encoding="utf-8") as file:
#     file.write("\n Ene mur umnuh medeeleliig ustgahguigeer nemegdene.")

# 1. Файлаас хоолнуудаа уншиж авах
import json
hool_menu = [
    {"ner" : "Buuz", "une" : 1000},
    {"ner" : "Buuz", "une" : 1000},
    {"ner" : "Buuz", "une" : 1000}
    ]
try:
    with open("hoolnuud.json", "r", encoding="utf-8") as f:
        hool_menu = json.load(f) # Текстийг шууд List/Dict болгож уншина
except (FileNotFoundError, json.JSONDecodeError):
    print("File baihgui bna, esvel hooson bna.")

# 2. Шинэ хоол нэмэх функц
def hool_nemeh():

    ner = input("shine hool ner: ")
    une = int(input("Une: "))
    shine_hool= {"ner" : ner, "une": une}

    hool_menu.append(shine_hool)

    with open("hoolnuud.json", "w", encoding="utf-8") as f:
        json.dump(hool_menu, f, ensure_ascii=False, indent=4)
    print("Amjilttai hadgalagdlaa!")

# Програмаа ажиллуулж шалгах
hool_nemeh()
print(f"Odoo baigaa tses: {hool_menu}")
