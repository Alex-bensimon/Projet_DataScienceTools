ch = "slzi 23de"
chaine_sans_string = ch.translate ({ord(c): " " for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"})
test = chaine_sans_string.strip()
print(test)