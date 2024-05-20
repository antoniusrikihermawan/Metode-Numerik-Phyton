import numpy as np

print('='*30,'Bisection','='*30)

def fungsi(x, p, q, r, s, t):
    return p * x**4 + q * x**3 + r * x**2 + s * x + t

def bisection(p, q, r, s, t, a, b, tol=1e-6, max_iter=100):
    while fungsi(a, p, q, r, s, t) * fungsi(b, p, q, r, s, t) >= 0:
        print('-'*70)
        print("\n\tKedua ujung interval memiliki tanda yang sama untuk nilai fungsi,\n\tsilakan masukkan ulang nilai a dan b.\n\t")
        print('-'*70)
        a = float(input("Masukkan nilai a (Interval): "))
        b = float(input("Masukkan nilai b (Interval): "))
        # Tambahkan kondisi untuk menghentikan loop jika a dan b sudah valid
        if fungsi(a, p, q, r, s, t) * fungsi(b, p, q, r, s, t) < 0:
            break

    iterasi = 0
    while (b - a) / 2 > tol and iterasi < max_iter:
        c = (a + b) / 2
        print(f"Iterasi {iterasi + 1}: a = {a}, b = {b}, c = {c}, f(c) = {fungsi(c, p, q, r, s, t)}")
        if fungsi(c, p, q, r, s, t) == 0:
            break
        elif fungsi(c, p, q, r, s, t) * fungsi(a, p, q, r, s, t) < 0:
            b = c
        else:
            a = c
        iterasi += 1

    print('-'*70)
    if iterasi >= max_iter:
        print("\n\tMetode tidak konvergen setelah jumlah iterasi maksimum yang ditentukan.\n")
        print('-'*70)
        return None
    else:
        print(f"\nKonvergensi diperoleh setelah {iterasi} iterasi.\n")
        print('-'*70)
        return (a + b) / 2

p = float(input("Masukkan nilai dari p: "))
q = float(input("Masukkan nilai dari q: "))
r = float(input("Masukkan nilai dari r: "))
s = float(input("Masukkan nilai dari s: "))
t = float(input("Masukkan nilai dari t: "))

a = float(input("Masukkan nilai dari a (Interval): "))
b = float(input("Masukkan nilai dari b (Interval): "))

hasil = bisection(p, q, r, s, t, a, b)
if hasil is not None:
    print(f"\nPerkiraan akar: {hasil}\n")
    print('-'*70)
