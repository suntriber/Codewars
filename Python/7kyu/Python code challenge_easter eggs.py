# For easter dinner you want to use your 9 colored easter eggs
# as decorations. You need to program your robot to put one egg
# of each color on each table

eggs = ['r2', 'g1', 'y2', 'r3', 'g3', 'r1', 'y1', 'g2', 'y3']

# write code to create this output
tables = [['g1', 'r1', 'y1'], ['g2', 'r2', 'y2'], ['g3', 'r3', 'y3']]

#Bonus, output in below order
tables2 = [['g1', 'r2', 'y3'], ['g2', 'r3', 'y1'], ['g3', 'r1', 'y2']]


eggs = ['r2', 'g1', 'y2', 'r3', 'g3', 'r1', 'y1', 'g2', 'y3']

task1 = []

for i in range(1, 4):
    task1.append(sorted([n for n in eggs if str(i) in n]))

print(task1)


task2 = [[],[],[]]

for i in range(len(task1)):
    for j in range(3):
        task2[i].append(task1[(i+j)%3][j])

print(task2)