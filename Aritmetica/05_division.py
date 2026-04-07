# DIVISIÓN

# Si a y b son números enteros, la división de a entre b, siendo b un número entero diferente de cero, consiste en encontrar a los números
# entros p y r, tales que:

#       a = b*p + r

# Primera división
x = 10
y = 2

x_div_y = f"La divisón de {x} entre {y} es:\n"
x_div_y += f"Cociente: {x//y}\n"
x_div_y += f"Resíduo {x%y}"

# print(x_div_y)


# Segunda división
x = 47
y = 3

x_div_y = f"La divisón de {x} entre {y} es:\n"
x_div_y += f"Cociente: {x//y}\n"
x_div_y += f"Resíduo {x%y}"

# print(x_div_y)


# División en una funcion:

def division(x,y):
    x_div_y = f"La divisón de {x} entre {y} es:\n"
    x_div_y += f"Cociente: {x//y}\n"
    x_div_y += f"Resíduo {x%y}\n"
    x_div_y += f"División directa: {x/y}"
    return x_div_y


resultado = division(47,3)

print(resultado)
