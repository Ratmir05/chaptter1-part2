'''num = int(input('vvedite spisok chisel'))
spisok = list(num)
for i in spisok:
    print(int(i+1))'''

x = int(input("Enter the number: "))
print("All the squares in the given range are:")
print([i**2 for i in range(1,x+1) if i**2 <= x])