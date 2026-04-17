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

while True: # Энэ нь програмыг зогсолтгүй ажиллуулна
    print("/n--- Toonii mashin (Garahiin  tuld 'exit' gej bicheerei) ---")

    orolt = input("Urgeljluuleh uu? (ali neg towch darah / exit): ")
    if orolt.lower() == "exit":
        print("Bayartai")
        break # Давталтыг зогсооно

# Алхам 2: Үндсэн логик (Програм эхлэх хэсэг)

    try: 
        too1 = float(input("1-r too: "))
        too2 = float(input("2-r too: "))
        uildel = input("Uildel songo (+, -, *, /): ")

        if uildel == "+":
            print(f"Ur dun: {too1 + too2}")
        elif uildel == "-":
            print(f"Ur dun: {too1 - too2}")
        elif uildel == "*":
            print(f"Ur dun: {too1 * too2}")
        elif uildel == "/": 
            if too2 == 0:
                print("Aldaa: 0-d huwaaj bolohgui")
            else:
                print(f"Ur dun: {too1 / too2}" )
        else: 
            print("Buruu uildel songoloo! (+, -, *, /) ashiglana uu")

    except ValueError: 
        print("Buruu utga oruulsan baina. Zaaval too oruulna uu")
    except Exception as e:
        print(f"Genetiin aldaa garlaa: {e}")

#13. Модуль (Modules) - Бэлэн хүчийг ашиглах