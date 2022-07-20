from forex_python.converter import CurrencyRates

jumlah = int(input('Silahkan masukan jumlah: '))
mata_uang = input('Mata uang: ').upper()
to_mata_uang = input('Mata uang tujuan : ').upper()
print(mata_uang, " ke ", to_mata_uang, jumlah)
hasil = CurrencyRates().convert(mata_uang, to_mata_uang, jumlah)
print(hasil)
