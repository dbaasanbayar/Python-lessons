# ner = "Baasanbayar"
# honog = 2
#print(f"Minii ner {ner}, bi Phyton suraad {honog} honoj baina")

#2 User Input

#ner = input("Ta neree oruulna uu:")
#honog = input("Hed honog surch baina we ?:")
#print(f"Sain uu {ner}! Chi Python suraad {honog} honoj baigaa yum bna. Amjilt!")

#3 Ugugdul turul huvirgah(Type Casting)
 
# ner = input("Ta neree oruulna uu:")
# honog_text = input("hed deh honogoo surch baina we?:")

# honog_too =int(honog_text)

# daraagiin_doloo_honog = honog_too + 7

# print(f"Sain uu {ner}!")
# print(f"doloo honogiin daraa chi {daraagiin_doloo_honog} dahi honogoo honogoo surch baih bolno.")

#4 Nuhtsul shalgah(If/ Else)

# honog = int(input("hed deh honog we?:"))

# if honog > 10:
#     print("chi mash tuushtai bna, amjilt!")
# elif honog > 0:
#     print("Shine zamdaa tawtai moril. Ehlel hamgiin chuhal!")
# else: 
# range(1, 6) gedeg ni 1-ees ehleed 6 hurtel (6 orohgui) toolno gesen ug


#5 For Loop (Тодорхой тооны давталт)

# honog = int(input("hicheel dawtah honog?:"))

# print("Python surah 5 honogiin tuluvluguu:")

# for honog in range(1, 6):
#     print(f"{honog} dahi honog: Hicheelee dawtah")

#6 while Loop (Нөхцөл биелэх хүртэл давтах)

# too = 1

# while too <= 5:
#     print(f"Toolj baina: {too}")

#     too = too + 1 #Тоог нэгээр нэмэгдүүлж байна. Үүнийг бичихгүй бол зогсолтгүй давтана!

#8 Жагсаалт (Lists)

# Жагсаалт үүсгэхдээ дөрвөлжин хаалт [ ] ашиглана
# hicheeluud = ["Variable", "Input", "If-Else", "Loop"]

# print(f"Unuudriin uzsen hicheeluud: {hicheeluud}")

# #Жагсаалтын эхний элементийг авах (Програмчлалд тоолохдоо 0-ээс эхэлдэг)

# print(f"Hamgiin ehnii hicheel: {hicheeluud[0]}")

# # Жагсаалтанд шинэ зүйл нэмэх

# hicheeluud.append("Functions")
# print(f"Shine jagsaalt: {hicheeluud}")

# daalgavar 1

# hoolnuud = ["Buuz", "Huushuur", "Pizza"]

# print(f"Odoo baigaa tses: {hoolnuud}")

# for hool in hoolnuud:
#     print(f"durtai hool {hool}")

# hoolnuud.append(input("chinii durtai hool yu we?:"))

# print(f"chinii durtai hool tsesend nemegdlee. Odoogiin tses: {hoolnuud}")

#9 Функц (Functions) - Кодоо дахин ашиглах

# Функц зарлахдаа 'def' (define) ашиглана

# def mendchilgee(ner): 
#     print(f"Sain uu {ner}, unuudur Python surahad belen uu?")

# mendchilgee("Baasanbayar")
# mendchilgee("Team-mate")

# daalgavar 2

# hool_menu = ["Buuz", "Huushuur", "Pizza"]
# print(f"odoo menu: {hool_menu}")

# # 1. Функцээ зарлах (Төлөвлөгөө гаргах)
# def hool_nemeh():
#     shine_hool = input("Нэмэх хоолны нэрээ оруулна уу: ")
#     hool_menu.append(shine_hool)
#     print(f"Амжилттай! {shine_hool} цэсэнд нэмэгдлээ.")

# # 2. Функцийг дуудах (Төлөвлөгөөгөө хэрэгжүүлэх)
# hool_nemeh() # Эхний удаа дуудах
# hool_nemeh() # Хоёр дахь удаа дуудах

# # 3. Эцэст нь бүх хоолоо хэвлэх
# print(f"Эцсийн цэс: {hool_menu}")

# Дараагийн шат: Параметр дамжуулах

# def sain_uu(ner): #"ner" bol parameter

#     print(f"Sain uu, {ner} bagshaa")

# sain_uu("Gemini")

# 10. Dictionary (Толь бичиг) - Түлхүүр ба Утга

# 'hool' гэдэг түлхүүр (key), 'Buuz' гэдэг утга (value)

# hool_medeelel = {
#     "ner": "Tsuivan",
#     "une": 12000,
#     "orts": ["guril", "mah", "luuwan"]
# }

# print(f"Hoolnii ner: {hool_medeelel["ner"]}")
# print(f"Une: {hool_medeelel["une"]} tugrug")

# 11. Өгөгдлийн бүтцүүдийг хослуулах (List of Dictionaries)

# restoran_tses = [
#     {"ner": "Buuz", "une": 1500},
#     {"ner": "Huushuur", "une": 2000},
#     {"ner": "Tsuivan", "une": 12000}
# ]
# print(f"{restoran_tses}")
# # Бүх хоолны үнийг хэвлэх

# for hool in restoran_tses:
#     print(f"{hool["ner"]} - {hool["une"]} tugrug")

# daalgavar

restoran_tses =  [
    {"ner": "Buuz", "une": 1500},
    {"ner": "Huushuur", "une": 2000},
    {"ner": "Tsuivan", "une": 12000}
]

print(f"aa {restoran_tses}")

def hool_nemeh():
    shine_hool_ner = input("Nemeh hoolnii neree oruulna uu:")
    shine_hool_une = int(input("Nemeh hoolnii unee oruulna uu:"))

    shine_hool = {"ner": shine_hool_ner, "une": shine_hool_une}

    restoran_tses.append(shine_hool)

    print(f"shine hool nemegdlee: {shine_hool}")

    for hool in restoran_tses:
       print(f"my menu {hool['ner']} - {hool['une']} tugrug")

hool_nemeh()
    