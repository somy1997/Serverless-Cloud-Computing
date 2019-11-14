import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Mumbai', 'London', 'California', 'Canada central', 'Singapore']
dynamodb_means = [61,69,93,81,81]
mongo_means = [5.5, 5.86, 5.78, 5.209, 5.41]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, dynamodb_means, width, label='Lambda - DynamoDB')
rects2 = ax.bar(x + width/2, mongo_means, width, label='EC2 MongoDB')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Database Latency')
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