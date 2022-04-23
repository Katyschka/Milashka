s=input("slovo:")
f=s[::-1]
def poli(s):
    while True:
        if s[::1]==f:
            print("Polindrom")
            break
        if s!=f:
            print("not polindrom")
            break

print(poli(s))
