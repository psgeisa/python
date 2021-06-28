# Concatenando numero inteiro e str
num_int = 5
num_dec = 7.3
val_str = "qualquer texto"

# %d é um marcador padrão

print("1ª forma - o valor é:", num_int)
print("2ª forma - o valor é:%i" %num_int) # %i de "inteiro"
print("3ª forma - o valor é:" + str(num_int)) # Essa concatenação necessita de conversão int > str

print("1ª forma - o valor é:", num_dec)
print("2ª forma - o valor é: %f" %num_dec) # %f de "float"
print("2ª forma - o valor é: %.4f" %num_dec)
print("3ª forma - o valor é:" + str(num_dec))

print("1ª forma - o valor é:", val_str)
print("2ª forma - o valor é: %s" %val_str) # %s de "string"
print("2ª forma - o valor é: %.4f" + val_str)
