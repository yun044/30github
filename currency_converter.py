def convert_currency(amount, from_currency, to_currency):
    exchange_rates = {
        "USD": {"EUR": 0.92, "KGS": 89.5, "RUB": 90.0},
        "EUR": {"USD": 1.09, "KGS": 97.5, "RUB": 97.8},
        "KGS": {"USD": 0.011, "EUR": 0.0103, "RUB": 1.0},
        "RUB": {"USD": 0.011, "EUR": 0.0102, "KGS": 1.0}
    }

    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        return "Ошибка: Валюта не поддерживается."

    converted_amount = amount * exchange_rates[from_currency][to_currency]
    return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"


print("💰 Конвертер валют")
print("Доступные валюты: USD, EUR, KGS, RUB")
amount = float(input("Введите сумму: "))
from_currency = input("Из какой валюты? ").upper()
to_currency = input("В какую валюту? ").upper()

result = convert_currency(amount, from_currency, to_currency)
print(result)