A0 = dict(zip(('a', 'b', 'c', 'd', 'e'),('1', '2', '3', '4', '5' )))
print(A0)
A1 = range(10)
print(A1)
A2 = [i for i in A1 if i in A0]
print(A2)
A3 = sorted(A0[i] for i in A0)
print(A3)
A4 = [[i, i*i] for i in A1]
print(A4)

for i in A0,A1,A2,A3,A4:
    print(i)