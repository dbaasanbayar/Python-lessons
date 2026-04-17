#OOP (Object-Oriented Programming)

#16 Класс (Class) ба Объект (Object)

# class Hool: 
#     # __init__ бол объектыг үүсгэхэд ажилладаг "constructor" юм
#     def __init__(self, ner, une):
#         self.ner = ner # self гэдэг нь тухайн объектыг өөрийг нь хэлж байгаа хэрэг
#         self.une = une

#     # Энэ бол "Метод" буюу класс доторх функц
#     def medeelel_haruulah(self):
#         print(f"hool: {self.ner}, une: {self.une} tugrug")
    
# # Одоо бодит объект үүсгэе
# hool1 = Hool("Buuz", 1500)
# hool2 =Hool("Tsuivan", 12000)

# hool1.medeelel_haruulah()
# hool2.medeelel_haruulah()

#Удамшил (Inheritance) - Програмчлалын "Гэр бүл

# class UuhZuil(Hool): # Hool классаас бүх зүйлийг өвлөж авна
#     def __init__(self, ner, une, hemjee):
#         super().__init__(ner, une) # Эцэг классын (Hool) __init__-ийг дуудаж байна
#         self.hemjee = hemjee

#     def medeelel_haruulah(self):
#         print(f"Undaa: {self.ner}, Hemjee: {self.hemjee}ml, Une: {self.une} tugrug")
# undaa = UuhZuil("Coca Cola", 2500, 500)
# undaa.medeelel_haruulah()

# class Developer:
#     def __init__(self, ner, ProgrammingHel):
#         self.ner = ner
#         self.ProgrammingHel = ProgrammingHel

#     def kod_bichih(self):
#         print(f"Namaig {self.ner} gedeg. bi {self.ProgrammingHel} deer kod bichdeg.")

# bi = Developer("Baasanbayar", "Python")

# bi.kod_bichih()

#19. Encapsulation (Нууцлал)

class Developer: 
    def __init__(self, ner, hel, tsalin):
        self.ner = ner
        self.hel = hel
        self.__tsalin = tsalin # Энэ хувьсагч ОДОО НУУЦ болсон

    def tsalin_harah(self):
        # Нууц мэдээллийг зөвхөн класс доторх функцээр дамжуулж харна
        print(f"{self.ner}-iin tsalin nuuts bolovch chamd helchihye: {self.__tsalin}$")

bi = Developer("Baasanbayar", "Phyton", 5000)

print(bi.ner)
# print(bi.__tsalin)

bi.tsalin_harah()
