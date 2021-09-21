a=int(input("kelko cisel: "))
priemer = 0

for n in range(a):
    cisel = float(input("zadaj cislo: "))
    priemer += cisel

avg = priemer/a
print("primer", a ,"cislo je: ", avg)

    
