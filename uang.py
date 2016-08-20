angka = {
    1: "satu",
    2: "dua",
    3: "tiga",
    4: "empat",
    5: "lima",
    6: "enam",
    7: "tujuh",
    8: "delapan",
    9: "sembilan",
}

def getEjaanUang(nilai):
    ejaan = ""
    ribuan = nilai % 1000

    if not ribuan:
        return "seribu"
    else:
        if ribuan / 100:
            ejaan = getEjaanRatusan(ribuan)
        else:
            ejaan = getEjaanPuluhan(ribuan)

    return ejaan

def getEjaanRatusan(nilai):
    ejaan = ""
    if nilai / 100 and not nilai % 100:
        if nilai / 100 == 1:
            return "seratus"
        else:
            ejaan += "{} ratus".format(angka[(nilai / 100)])
            # ejaan += getEjaanPuluhan(nilai)
    else:
        if nilai / 100 == 1:
            ejaan += "seratus "
            ejaan += getEjaanPuluhan(nilai % 100)
        else:
            ejaan += "{} ratus ".format(angka[(nilai / 100)])
            ejaan += getEjaanPuluhan(nilai % 100)

    return ejaan

def getEjaanPuluhan(nilai):
    ejaan = ""
    if nilai / 10 and not nilai % 10:
        if nilai / 10 == 1:
            return "sepuluh"
        else:
            return "{} puluh ".format(angka[(nilai / 10)])
    else:
        if nilai / 10 == 1:
            if nilai % 10 == 1:
                ejaan += "sebelas "
            else:
                ejaan += "{} belas ".format(angka[nilai % 10])
        else:
            if nilai /10:
                ejaan += "{} puluh {}".format(angka[nilai / 10], angka[nilai % 10])
            else:
                ejaan += "{}".format(angka[nilai % 10])

    return ejaan


if __name__ == '__main__':
    uang = raw_input('Masukan nilai uang (20 - 1000): ')

    if int(uang) not in range(20, 1000 + 1):
        print 'error'
    else:
        print getEjaanUang(int(uang))
