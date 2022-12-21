
t = input("Digite o tempo (emsegundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida!")
    quit()

# 120 / 60 = 2
# 150 / 60 = 2 | 30

while t:
    minutes, seconds = divmod(t, 60)
    timer = f"{minutes}:{seconds}"
    print(timer, end="\r")
    t = t - 1