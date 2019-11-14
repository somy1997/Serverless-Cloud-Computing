import matplotlib.pyplot as plt
import numpy as np
import statistics as st


def getactualstats():
    filename = '../nested.csv'
    print('Loading actual stats from',filename)
    f = open(filename, 'r')
    statslist1 = []
    statslist2 = []
    statslist3 = []
    i = 1
    for line in f:
        if i == 1 :
            i+=1
            continue
        #print(line.strip())
        #print(line)
        line = line.split(',')
        statslist1 += [int(line[0])]
        statslist2 += [int(line[1])]
        statslist3 += [int(line[2])]
        #round function returns type as int by default (decimal places to keep is 0) otherwise float
    f.close()
    print()
    return statslist1, statslist2, statslist3

st1, st2, st3 = getactualstats()

data = [st1, st2, st3]
labels = ["Billed Duration of \nInner Function", "Actual Duration of \nFunction Call", "Billed Duration of \nOuter Function"]
fig, ax = plt.subplots()
pos = np.array(range(len(data))) + 1

bp = ax.boxplot(data, positions=pos,
                notch=1,
                labels = labels)

# ax.set_xlabel('Depth of the workflow')
ax.set_ylabel('Time (ms)')
plt.setp(bp['whiskers'], color='k', linestyle='-')
plt.setp(bp['fliers'], markersize=3.0)
axes = plt.gca()
axes.set_ylim([-25,250])
plt.show()