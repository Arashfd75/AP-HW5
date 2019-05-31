input1 = [int(x) for x in input("Enter multiple value: ").split()] 
print(*sorted(set([item for item in input1 if(item % 6 == 0 and (input1.index(item) + 1) % 6 == 0 )])))
