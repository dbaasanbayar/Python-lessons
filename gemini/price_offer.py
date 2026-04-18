import pandas as pd

prices_data = [
    {"baraa": "Notebook", "price": 1500},
    {"baraa": "Pen", "price": "10"},
    {"baraa": "Eraser", "price": "free"},
    {"baraa": "Mouse", "price": 250},
    {"baraa": "Keyboard", "price": None}
]

# (List, Dict, Loop) болон Pandas

def clean_price_data(item):
    try :
        price = int(item['price'])
    except (ValueError, TypeError):
        price = 0
    return {"baraa" : item['baraa'],"price": price}

cleaned_price_data = [clean_price_data(item) for item in prices_data]
for item in cleaned_price_data:
    print(f"price tsewerlesen data, {item}")

prices = [item['price'] for item in cleaned_price_data]

average_price = sum(prices) / len(prices)
print(f"Dundaj une: {average_price}")

max_price = max(prices)
print(f"Undur une: {max_price}")

df_prices_data = pd.DataFrame(cleaned_price_data)
print(df_prices_data)

high_prices = df_prices_data[df_prices_data['price'] >= 100]
print(high_prices)

high_prices.to_csv("high_prices.csv", index=False)
print("Data amjilttai hadgalagdlaa!")
