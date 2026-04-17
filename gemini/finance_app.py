import json

# 1. Гүйлгээг төлөөлөх класс
class Transaction:
    def __init__(self, turul, utga, dun):
        self.turul = turul # "Income" эсвэл "Expense"
        self.utga = utga # Жишээ нь: "Цалин" эсвэл "Хоол"
        self.dun = dun # Тоон утга

# 2. Санхүүг удирдах класс
class FinanecManager: 
    def __init__(self, file_ner="finance_data.json"):
        self.file_ner = file_ner
        self.transactions = self.load_data()

    def load_data(self):
        try:
            with open(self.file_ner, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    def save_data(self):
        with open(self.file_ner, "w", encoding="utf-8") as f:
            json.dump(self.transactions, f, indent=4, ensure_ascii=False)
    
    def nemeh(self, turul, utga, dun):
        new_tx ={"turul": turul, "utga": utga, "dun": dun}
        self.transactions.append(new_tx)
        self.save_data()
        print(f"\n {utga} amjilttai burtgegdlee.")

    def tailan_haruulah(self):
        niit_orlogo = 0
        niit_zarlaga = 0
        print("\n--- Tanii Sanhuugiin Tailan ---")
        for tx in self.transactions:
            temdeg = "+" if tx['turul'] == "1" else "-"
            print(f"{tx['utga']}: {temdeg}{tx['dun']} Tugrug")

            if tx['turul'] == "1":
                niit_orlogo += tx['dun']
            else:
                niit_zarlaga += tx['dun']
        uldegldel = niit_orlogo - niit_zarlaga

        print(f"-------------------")
        print(f"Niit orlogo: {niit_orlogo} Tugrug")
        print (f"Niit zarlaga: {niit_zarlaga} Tugrug")
        print(f"Uldegdel: {niit_orlogo} - {niit_zarlaga} Tugrug")
        print(f"Uldegdel: {uldegldel} Tugrug")

# 3. Үндсэн програм (Main Loop)
def main():
    manager =  FinanecManager()

    while True:
        print("\n1. Orlogo nemeh")
        print("2. Zarlaga nemeh")
        print("3. Tailan harah")
        print("4. Garah")

        songolt = input("\nSongoltoo oruulna uu:")

        if songolt == "4":
            print("Bayarlalaa, Bayartai")
            break

        try:
            if songolt in ["1", "2"]:
                utga = input("Guilgeenii utga (Жишээ нь: Цалин):")
                dun = float(input("Dun:"))
                manager.nemeh(songolt, utga, dun)
            elif songolt == "3":
                manager.tailan_haruulah()
            else :
                print("Buruu songolt")
        except ValueError:
            print("Aldaa: Ta dungee toogoor oruulna uu!")

if __name__ == "__main__":
    main()