import os
#si, smax, t, d, sc, tr, sr, na
f = open(os.getcwd()+"\\00-example.txt")

line = f.readline().split()

s_i = int(line[0])
s_max = int(line[1])
t = int(line[2])
d = int(line[3])

demons=[]

line=f.readline().split()
print(line[4:])
while line:
    demons.append([line[0], line[1], line[2], line[3], [line[4:]]])
    line=f.readline().split()

print("Parsing Done!")   