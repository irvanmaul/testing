def lulus(nilai, kuota):
    result = sorted([n if n >= 90 else 0 for n in nilai], reverse=True)[0:kuota]
    return result

print lulus((32, 61, 75, 89, 91, 92), 3)