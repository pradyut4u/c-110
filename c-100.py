import pandas as pd
import csv
import plotly.figure_factory as pff
import statistics
import random

df = pd.read_csv(r"D:/python/py/c-110.csv")
fig = pff.create_distplot([df["average"].tolist()],["AVG"])
#fig.show()

Avglist = df["average"].tolist()
Avgl = len(Avglist) - 1
print(Avgl)

pmean = statistics.mean(Avglist)
psd = statistics.stdev(Avglist)

print(pmean)
print(psd)

def samplespace():

    newlist = []

    for i in range(0,10000):
        a = Avglist[random.randint(0,Avgl)]
        newlist.append(a)

    #l = len(newlist)
    #print(l)

    smean = statistics.mean(newlist)
    #ssd = statistics.stdev(newlist)
    return(smean)
    print(smean)
    #print(ssd)

def repeat():
    newlist2 = []

    for q in range(0,10):
        w = samplespace()
        newlist2.append(w)

    dig = pff.create_distplot([newlist2],["Mean"])
    dig.show()

    n2mean = statistics.mean(newlist2)
    n2sd = statistics.stdev(newlist2)
    print(n2mean)
    print(n2sd)

e = repeat()