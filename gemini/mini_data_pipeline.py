# # Жишээ: Чамд түүхий дата (raw data) ирсэн гэж бодъё. Түүн доторх хоосон зайг арилгаж, бүх үсгийг том болгох хэрэгтэй:

# raw_data = [" apple ", "  banana", "cherry  ", "  "]

# # Хуучин арга:
# cleaned_data = []
# for item in raw_data:
#     if item.strip(): # Хоосон биш бол
#         cleaned_data.append(item.strip().upper())

# print(f"old way {cleaned_data}")

# # List Comprehension (Дата инженерийн арга):
# cleaned_data = [item.strip().upper() for item in raw_data if item.strip()]

# print(f"LC {cleaned_data}")

# unuud = [100, 250, 400]

# #Une bur deer 10% tatvar nemeh
# tatwartai_une = list(map(lambda x: x * 1.1, unuud))
# print(f"tatwartai une {tatwartai_une}")


#bohir data

users = [
    {"name": "  Baasan ", "age": "25", "email": "BAASAN@GMAIL.COM"},
    {"name": "Demberel", "age": "unknown", "email": "demberel@yahoo.com"},
    {"name": "John ", "age": "30", "email": "JOHN@outlook.com"}
]

    #1. ners dotorh iluu zaig arilgah
    #2. ehnii usgiig tomoor bolgoh
    #3. age hesegt unknown utgiig 0 bolgoh (try-except ashiglah)
    #4. email-uudiig jijig usegtei bolgoh

def clean_user_data(user):
    # 1. Нэр цэвэрлэх
    name = user["name"].strip().capitalize()

    # 2. Нас цэвэрлэх (Try-Except ашиглаарай)
    try: 
        age = int(user["age"])
    except ValueError:
        age = 0
    # 3. Email цэвэрлэх
    email = user["email"].lower()

    return {"name": name, "age": age, "email": email}

# Бүх хэрэглэгчийг цэвэрлэх (Map ашиглаад үзээрэй)

cleaned_users = [clean_user_data(u) for u in users ]

# filtered_users = [u for u in cleaned_users if u['age'] >= 18]

# for u in cleaned_users: 
#     print(u)
# for u in filtered_users:
#     print(u)

# 24. Өгөгдлийг нэгтгэх (Aggregation)

# total_users= len(cleaned_users)
# print(f"Niit hereglegch too: {total_users}")

# nasnuud = [u['age'] for u in cleaned_users if u['age'] > 0]
# average_age = sum(nasnuud) / len(nasnuud)
# print(f"Dundaj nas: {average_age}")

# max_nas = max(nasnuud)
# print(f"Undur nas oloh: {max_nas}")

# # Энгийн жагсаалт (Санах ой их идэх аюултай)
# data_list = [x for x in range(1000000)] 

# # Generator (Хаалтыг нь ( ) болгоход л хангалттай)
# data_gen = (x for x in range(1000000))

# print(next(data_gen)) # 0
# print(next(data_gen)) # 1
# Энэ нь санах ойг бараг ашиглахгүй!

# 26. Sorting (Эрэмбэлэх) ба Grouping (Бүлэглэх)

# Насаар нь багаас их рүү эрэмбэлэх
# sorted_users = sorted(cleaned_users, key=lambda u: u['age'])

# for u in sorted_users:
#     print(f" sorted suer{u}")


# 27. Dictionary-г "Map" болгож ашиглах
    
# user_lookup = {u['email']: u for u in cleaned_users}
# user_lookup_name = {u['name']: u for u in cleaned_users}

# def user_haih(user_lookup):
#     user_email = input("emaileer haih: ").lower().strip()

#     try: 
#         ur_dun = user_lookup[user_email]
#         print(f"Oldloo: {ur_dun}")
#     except KeyError:
#         print("Uuchlaarai, iim emailtei hereglegch oldsongui.")
    
# user_haih(user_lookup)

# def user_haih_ner(user_lookup_name):
#     user_name = input("nereer haih: ").capitalize().strip()

#     try:
#         ur_dun = user_lookup_name[user_name]
#         print(f"Oldloo: {ur_dun}")
#     except KeyError:
#         print("uuchlaarai, iim nertei hereglegch oldsongui.")

# user_haih_ner(user_lookup_name) 

# 29. Pandas
import pandas as pd

# 1. Өгөгдлөө DataFrame (Хүснэгт) болгож хувиргах

df = pd.DataFrame(cleaned_users)

# 2. Дундаж насыг ганц мөрөөр олох
print(f"Dundaj nas: {df['age'].mean()}")

# 3. Зөвхөн 18-аас дээш настнуудыг шүүх
full_age_users = df[df['age'] >= 18]

print(df)
print(full_age_users)

# 31. Датаг "Бүлэг" (Group) болгох

# Нас тус бүрээр хэдэн хүн байгааг тоолох
print(df.groupby('age').count())

# 32. Өгөгдлийг Файл руу хадгалах (CSV - Дата инженерийн стандарт)

df.to_csv("tsewerlesen_hereglegchid.csv", index=False)
print("Data amjilttai hadgalagdlaa!")
