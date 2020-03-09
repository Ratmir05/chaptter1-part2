'''stud_a = int(input('enter ur count of students'))
stud_b = int(input('enter ur count of students'))
stud_c = int(input('enter ur count of students'))'''

stud_abc = input('choose count of students in class (A:B:C):').split(':')
#desk_abc = input('count of desks for class (A:B:C):').split(':')
stud_abc = (int(stud_abc[0])+1)//2 + (int(stud_abc[1])+1)//2 + (int(stud_abc[2])+1)//2
#desk_abc = int(stud_abc[0])//2 + int(stud_abc[1])//2 + int(stud_abc[2])//2
#print(desk_abc)
print(stud_abc)

