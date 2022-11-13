import random

f = open("eredmenyek_nyers.txt", "w")
for i in range(99999):  # number of outputs
    randomlist = random.randint(9000000000,9999999999) #range of numbers
    f.write(str(randomlist) + '\n')
f.close()

db=0
f = open("eredmenyek_nyers.txt", "r")
f2 = open("eredmenyek_szort.txt", "w")
szamok = f.read()
ezt = szamok.split("\n")
xxx=len(ezt)
print(ezt)
i=0
db=0

for xxx in ezt:
    if '80' > ezt[i]:
        if ezt[i] > '20':
            db+=1
            f2.write(str(ezt[i]) + ',')
    i+=1
print("Sayonara:",db)
f.close()
f2.close()
