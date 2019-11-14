import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import statistics as st


def getactualstats(loca, req):
    filename = '../statsServerMumbai/'+ loca + '_' + req + '.csv'
    print('Loading actual stats from',filename)
    f = open(filename, 'r')
    statslist1 = []
    statslist2 = []
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
        #round function returns type as int by default (decimal places to keep is 0) otherwise float
    f.close()
    print()
    return round(st.mean(statslist1)),round(st.mean(statslist2))

locas = ['mumbai', 'london', 'ncal', 'sidney', 'tokyo']
labels = ['India', 'Europe', 'USA', 'Australia', 'Japan']

req = 'post'

actual_means = []
billed_means = []

for loca in locas :
    meen = getactualstats(loca, req)
    actual_means.append(meen[0])
    billed_means.append(meen[1])


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
fig.suptitle('POST requests')
rects1 = ax.bar(x - width/2, actual_means, width, label='Actual Durations')
rects2 = ax.bar(x + width/2, billed_means, width, label='Billed Durations')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Database Latency (ms)')
# ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')


# autolabel(rects1)
# autolabel(rects2)

fig.tight_layout()

plt.show()