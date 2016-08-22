def kencanKelompok(pria, perempuan):
    return True if sorted(pria) == sorted(perempuan) else False

print kencanKelompok([168, 156, 180], [180, 156, 168])