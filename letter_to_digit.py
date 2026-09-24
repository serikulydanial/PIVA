def let(char):
    if 'А' <= char <= 'Я':
        return str(ord(char) - ord('А') + 1)
    return char

print("Введите буквы русского алфавита")

text = input("Текст: ").upper()

umn = [int(let(c)) for c in text]

print(umn)

for x in umn:
    if x % 5 == 0:
        print("(0 0 0 1)")
    elif x % 3 == 0:
        print("(0 0 1 0)")
    elif x % 2 == 0:
        print("(0 1 0 0)")
    else:
        print("(1 0 0 0)")