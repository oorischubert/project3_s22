import numpy as np
import matplotlib.pyplot as mat
#used for text saving
color=['^r-','^g-','^b-','^y-']
fileName = 'game1.txt'
file=open(fileName,"r")
contents = file.read().split("\n")
lineList=[]

for line in contents:
  list = line.split()
  lineList.append(list)
for row in range(len(lineList[0])):
    columnList=[]
    timeList=[]
    for i in range(len(lineList)):
        columnList.append(float(lineList[i][row]))
        timeList.append(i)
    mat.plot(timeList,columnList,color[row],linewidth=2.0)

mat.legend(['red','green','blue','yellow'])
mat.ylabel('#Aliens shot')
mat.xlabel('Time steps')
mat.title('%s Statistics on Alien Killings'%(fileName))
mat.show()