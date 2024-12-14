n = int(input("Введите число от 3 до 20: "))
result = ""
for x in range(1, 21):
    for y in range(x, 21):
        if (x + y) % n == 0:
            result += f"{x}{y}"
print("Результат:", result)


