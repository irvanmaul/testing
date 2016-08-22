def antrianSempurna(antrian):
    return True if antrian == sorted(antrian) else False

print antrianSempurna([12,3,6])