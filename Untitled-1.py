import random
longitud_de_la_contrasena=int(input("introduse la longitud de la contraseña"))
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passward = ""
for i in range(longitud_de_la_contrasena):
    passward += random.choice(caracteres)
print(passward)

