from tabulate import tabulate
import numpy as np

def fx(x, p, q, r, s):
    return p * x**3 + q * x**2 + r * x + s

def bisection(p, q, r, s, a, b, tol=1e-6, max_iter=100):
    # Check if the initial interval is valid
    if fx(a, p, q, r, s) * fx(b, p, q, r, s) >= 0:
        print('-'*70)
        print("\n\tKedua ujung interval memiliki tanda yang sama untuk nilai fungsi,\n\tsilakan masukkan ulang nilai a dan b.\n\t")
        print('-'*70)
        a = float(input("Masukkan nilai a (Interval) : "))
        b = float(input("Masukkan nilai b (Interval) : "))

        if fx(a, p, q, r, s) * fx(b, p, q, r, s) >= 0:
            print("Masih tidak mungkin menemukan akar dalam interval yang diberikan.")
            return None

    iterasi_data = []

    for iterasi in range(max_iter):
        c = (a + b) / 2
        fc = fx(c, p, q, r, s)
        iterasi_data.append([iterasi, a, b, c, fc])

        if abs(fc) < tol or (b - a) / 2 < tol:
            break
        elif fx(a, p, q, r, s) * fc < 0:
            b = c
        else:
            a = c

    print('-'*70)
    print(f"\nKonvergensi diperoleh setelah {iterasi + 1} iterasi.\n")
    return (a + b) / 2, iterasi_data

def main():
    print('-'*30, 'Welcome', '-'*30)

    try:
        p = float(input("Masukkan nilai dari p: "))
        q = float(input("Masukkan nilai dari q: "))
        r = float(input("Masukkan nilai dari r: "))
        s = float(input("Masukkan nilai dari s: "))

        a = float(input("Masukkan nilai dari a (Interval): "))
        b = float(input("Masukkan nilai dari b (Interval): "))
    except ValueError:
        print("Input tidak valid, pastikan untuk memasukkan angka.")
        return

    hasil, iterasi_data = bisection(p, q, r, s, a, b)
    if hasil is not None:
        headers = ["Iterasi", "a", "b", "c", "f(c)"]
        table_data = [[data[0], data[1], data[2], data[3], data[4]] for data in iterasi_data]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

        print(f"\nAproksimasi akar : {hasil}\n")
        print('-'*70)
    else:
        print("\n\tGagal mencari akar dalam iterasi yang di berikan\n")

if __name__ == "__main__":
    main()
