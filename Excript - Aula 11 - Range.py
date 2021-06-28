#Break
print("antes de entrar no laço de repetição")
for item in range(10):
    print(item)
    if (item==6):
        print("retornou True")
        break
print("depois do laço")

#Continue
print()
print("inicio")
i = 0
while(i<10):
    i += 1
    if (i%2==0):
         continue
    print(i)
else:
    print("else")
print("fim")

#Continue vs Break 
print()
print("inicio")
i = 0
while(i<10):
    i += 1
    if (i%2==0):
         continue
    if (i>5):
         break
    print(i)
else:
    print("else")
print("fim")
