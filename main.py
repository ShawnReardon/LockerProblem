lockers = []
twice = []
# Number of Students/Lockers
i = int(input("Please Enter the Number of Students: "))

#Intiliaze Array of Lockers
for doors in range(0,i):
  lockers.append(False)


#print(*lockers)
print("Starts: \n")

n = 1
while n <= i:
  for student in range(0,i,n):
    if lockers[student-1] == False:
      lockers[student-1] = True
      print(student)
    else:
      if student - 1 != -1:
        twice.append(student-1)
      lockers[student-1] = False
      #print(student)

  #print(*lockers)
  print("\n")
  n+=1
opened = 0
closed = 0
for bools in lockers:
  if bools:
    opened+=1
  else:
    closed+=1
print("Open:", opened, "\n")
print("Closed:", closed)
y = 0

for n in lockers:
  y+=1
  if n:
    print(y, n)
#print(*twice)
