m, n = map(int, input("Entrez votre fraction sous la forme a/b : ").split("/"))
fractionsUnitaires = []

while m != 1:
    q = n // m
    r = n % m
    fractionsUnitaires.append(q+1)
    m = m - r
    n = n*(q+1)

fractionsUnitaires.append(n)
print('+'.join([f"1/{fractionUnitaire}" for fractionUnitaire in fractionsUnitaires]))
