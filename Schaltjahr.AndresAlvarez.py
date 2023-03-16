# Schaltjahr
jahr = 1984

if jahr % 4 != 0:
    print("Es ist kein Schaltjahr")
elif jahr % 4 == 0 and jahr % 100 != 0:
    print("Es ist Schaltjahr")
elif jahr % 4 == 0 and jahr % 100 == 0 and jahr % 400 != 0:
    print("Es ist kein Schaltjahr")
elif jahr % 4 == 0 and jahr % 100 == 0 and jahr % 400 == 0:
    print("Es ist Schaltjahr")