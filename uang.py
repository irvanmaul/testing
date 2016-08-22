from collections import OrderedDict

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

pecahanBesar = OrderedDict([
    (1000000000000, "trilyun"),
    (1000000000, "milyar"),
    (1000000, "juta"),
    (1000, "ribu"),
    (100, "ratus"),
])

pecahanKecil = OrderedDict([
    (100, "ratus"),
    (10, "puluh"),
])


def konversiAngkaToEjaan(nilai):
    ejaan = ""

    for p in pecahanBesar:
        nilai_tmp = (nilai / p) * p

        if p == 100:
            ejaan += ejaanUmum(nilai, True)
        else:
            if nilai_tmp:
                ejaan += "{}{} ".format(ejaanUmum((nilai_tmp + nilai % p) / p), pecahanBesar[p])
            nilai -= ((nilai_tmp + nilai % p) / p) * p

        nilai = nilai % p

    return ejaan


def ejaanUmum(nilai, maxSeribu=True):
    ejaan = ""
    belas = False

    for p in pecahanKecil:
        if nilai % p != nilai:
            if nilai / p == 1 and maxSeribu:
                if p == 10 and nilai % p:
                    if nilai % p == 1:
                        ejaan += "sebelas "
                    else:
                        ejaan += "{} belas ".format(angka[nilai % p])
                    belas = True
                else:
                    ejaan += "se{} ".format(pecahanKecil[p])
            else:
                ejaan += "{} {} ".format(angka[nilai / p], pecahanKecil[p])

            if nilai % p == 0:
                break

            nilai = nilai % p

    if nilai % 10 != 0 and not belas:
        ejaan += "{} ".format(angka[nilai])

    return ejaan


if __name__ == '__main__':
    uang = raw_input('Masukan nilai uang: ')

    if int(uang) == 0:
        print 'nol'
    else:
        print konversiAngkaToEjaan(int(uang))
