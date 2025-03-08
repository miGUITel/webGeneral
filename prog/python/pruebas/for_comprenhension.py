temps = [100, 200]
print (temps)
for a in range(0, len(temps)): temps[a] = temps[a]*2
print (temps)

temps2 = [(2 * temp) for temp in temps]
print (temps2)

