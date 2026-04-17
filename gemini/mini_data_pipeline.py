# Жишээ: Чамд түүхий дата (raw data) ирсэн гэж бодъё. Түүн доторх хоосон зайг арилгаж, бүх үсгийг том болгох хэрэгтэй:

raw_data = [" apple ", "  banana", "cherry  ", "  "]

# Хуучин арга:
cleaned_data = []
for item in raw_data:
    if item.strip(): # Хоосон биш бол
        cleaned_data.append(item.strip().upper())

print(f"old way {cleaned_data}")

# List Comprehension (Дата инженерийн арга):
cleaned_data = [item.strip().upper() for item in raw_data if item.strip()]

print(f"LC {cleaned_data}")

unuud = [100, 250, 400]

#Une bur deer 10% tatvar nemeh
tatwartai_une = list(map(lambda x: x * 1.1, unuud))
print(f"tatwartai une {tatwartai_une}")


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

filtered_users = [u for u in cleaned_users if u['age'] >= 18]

for u in cleaned_users: 
    print(u)
for u in filtered_users:
    print(u)

