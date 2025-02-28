import requests

def get_exchange_rates():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data["rates"]
    except Exception as e:
        print("⚠ Не удалось получить актуальные курсы, используются фиксированные данные.")
        return {
            "USD": {"EUR": 0.92, "KGS": 89.5, "RUB": 90.0},
            "EUR": {"USD": 1.09, "KGS": 97.5, "RUB": 97.8},
            "KGS": {"USD": 0.011, "EUR": 0.0103, "RUB": 1.0},
            "RUB": {"USD": 0.011, "EUR": 0.0102, "KGS": 1.0}
        }


def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return "❌ Ошибка: Валюта не поддерживается."

    if from_currency == to_currency:
        return f"🔄 {amount} {from_currency} = {amount:.2f} {to_currency} (без изменений)"

    converted_amount = amount * (rates[to_currency] / rates[from_currency])
    return f"💱 {amount} {from_currency} = {converted_amount:.2f} {to_currency}"

# Основная программа
print("💰 Конвертер валют")
print("📌 Доступные валюты: USD, EUR, KGS, RUB")

# Получаем курсы валют
exchange_rates = get_exchange_rates()

try:
    amount = float(input("💵 Введите сумму: "))
    from_currency = input("🔄 Из какой валюты? ").upper()
    to_currency = input("🔄 В какую валюту? (или 'ALL' для всех) ").upper()

    if to_currency == "ALL":
        print("🌍 Конвертация во все доступные валюты:")
        for currency in exchange_rates.keys():
            if currency != from_currency:
                print(convert_currency(amount, from_currency, currency, exchange_rates))
    else:
        print(convert_currency(amount, from_currency, to_currency, exchange_rates))

except ValueError:
    print("❌ Ошибка: Введите корректное число.")