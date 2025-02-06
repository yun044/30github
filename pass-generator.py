import random
import string

emojis = ["🔥", "💎", "🚀", "🐍", "🔑", "🎲", "⚡", "❤️"]

def generate_password(length=12, use_emojis=True):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

    if use_emojis:
        emoji = random.choice(emojis)
        insert_pos = random.randint(0, length - 1)
        password = password[:insert_pos] + emoji + password[insert_pos:]

    return password

print(generate_password(16))