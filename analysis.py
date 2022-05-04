import numpy as np
import matplotlib.pyplot as mat
#used for text saving
color=['^-r','^-g','^-b','^-y']
fileName = 'game2.txt'
file=open(fileName,"r")
contents = file.read().split("\n")
#yRange = 
for line in contents:
  lineList = line.split()
  for a in range(len(lineList)):
   if lineList[a] != 0:
    mat.plot([contents.index(line)],[lineList[a]],color[a])
mat.legend(['red','green','blue','yellow'])
mat.ylabel('#Aliens shot')
mat.xlabel('Time steps')
mat.title('%s Statistics on Alien Killings'%(fileName))
mat.show()