import os 
os.system ("cls")


while True:
    n1 = float(input("Digite sua nota:"))
    if n1 <= 0 and n1 >= 10:
        break
    
while True:
    n2 = float(input("Digite sua nota:"))
    if n2 <= 0 and n2 >= 10:
        break
    
media = n1 + n2 / 2
    
print(f"Media: {media}")