import shutil, itertools, random
elecstudentarr, a, abscount, countarr, grname1, grname2, grname, votearr,percent,tiearray = [], 0, 0, [0,0,0,0], ['7', '8', '9', '10', '11'], ['A', 'B', 'C', 'D', 'E', 'F'], [], [], [], []
gname = list(itertools.product(grname1, grname2))
for i in range(len(gname)):
  grname.append(''.join(gname[i]))
columns = shutil.get_terminal_size().columns
groupname = input("Group name: ")
while groupname not in grname:
  print('Please enter valid group name')
  groupname = input("Group name: ")
nostudent = int(input("Amount of student: "))
while nostudent < 1 or nostudent > 90:
  print('Please enter valid number of student')
  nostudent = int(input("Amount of student: "))
noelecstudent = int(input("Amount of candidates in election: "))
while noelecstudent <= 0 or noelecstudent > 4:
  print("Please enter a valid number")
  noelecstudent = int(input("Amount of candidates in election: "))
for i in range(noelecstudent):
  a = input("Student's name: ")
  elecstudentarr.append(a)
for i in range(nostudent):
  a = input("Please enter your vote: ")
  while a not in elecstudentarr:
    print("Please enter valid value")
    a = input("Please enter your vote: ")
  if a == 'abstain':
    abscount += 1
  else: 
    for i in range(len(elecstudentarr)):
      if a == elecstudentarr[i]:
        countarr[i] += 1
    r = random.randint(100000,999999)
    print(f'Your unique voter number is: VN{r}')
    votearr.append(r)
print(groupname.center(columns))

realvote = nostudent - abscount
for i in range(len(countarr)):
  b = countarr[i] / realvote
  percent.append([str(b * 100) + '%'])
studentstat = [[x]+y for x, y in zip(countarr, percent)]
studentdic = dict(zip(elecstudentarr, studentstat))
for i in studentdic:
  print(f'Name: {i}, No.vote: {studentdic[i][0]}, Percent: {studentdic[i][1]}')
highestvote = [key for key, value in studentdic.items() if value == max(studentdic.values())]
if len(highestvote) == 1:
  print(f'The winner is: {highestvote[0]}')
else:
  print('We have a tie!')
  for i in range (len(highestvote)):
    print(highestvote[i])
print(f'Total votes cast: {realvote} \n Total abstentions: {abscount}')







  
  
