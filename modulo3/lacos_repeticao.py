# Laços de repetição são: for, while

# 0 1 2 3 4 5
for i in range(0, 11, 2):
    print(i)

limite = 10

i = 0

while(True):

    print(i)
    if i == 3:
        continue
    
    if i == 11:
        break
    
    i = i + 1

print("Saiu do loop")