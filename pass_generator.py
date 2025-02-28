import random
import string

emojis = ["🔥", "💎", "🚀", "🐍", "🔑", "🎲", "⚡", "❤️"]

def generate_password(length=12, use_emojis=True, emoji_count=1, use_special_chars=True):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов.")

    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))

    if use_emojis:
        for _ in range(min(emoji_count, length)):  # Вставляем не больше, чем длина пароля
            emoji = random.choice(emojis)
            insert_pos = random.randint(0, len(password) - 1)
            password = password[:insert_pos] + emoji + password[insert_pos:]

    return password

print(generate_password(16))  # Обычный пароль с 1 эмодзи
print(generate_password(20, emoji_count=3))  # Пароль с 3 эмодзи
print(generate_password(12, use_special_chars=False))  # Без спецсимволов
print(generate_password(8, use_emojis=False))  # Без эмодзи