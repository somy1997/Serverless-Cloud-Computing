import matplotlib.pyplot as plt
import numpy as np


d1 = [70,48,78,55,23,30,60,41,44,28,65,44,35,53,53,57,66,36,139,18,62,25,85,24,42,55,61,33,22,48,59,66,56,37,42,48,48,51,52,35,50,61,39,51,73,67,33,41,45,74,74,45,55,73,56,29,52,45,76,53,35,56,54,47,41,58,43,41,44,26,41,34,72,17,52,42,19,26,74,76,60,42,75,149,48,52,39,42,41,46,41,68,34,60,38,39,31,38,46,40]
d2 = [246,112,99,67,106,115,150,101,368,140,104,118,116,232,330,97,151,103,77,87,102,120,104,137,93,104,129,96,88,97,137,101,104,79,70,125,91,141,104,126,119,86,75,105,129,109,107,107,115,111,144,129,122,124,99,160,89,115,264,66,56,91,82,120,133,121,99,104,95,106,83,72,133,122,92,90,84,127,102,117,98,93,157,105,122,105,173,146,93,71,97,91,141,186,77,111,108,108,116,196]
d3 = [522,207,410,142,153,143,105,138,128,129,164,255,176,142,147,159,193,184,148,145,154,181,180,139,429,179,159,159,150,151,169,182,378,207,157,169,140,129,162,139,148,162,169,123,160,139,193,141,180,145,152,111,115,205,129,161,175,133,169,111,178,166,148,174,235,207,191,181,330,125,157,152,123,140,175,145,160,109,147,159,156,265,124,147,174,144,135,159,199,168,134,152,202,160,149,125,139,145,162,201]
d4 = [329,215,201,230,202,195,187,169,227,234,199,233,202,192,196,186,187,196,201,200,210,186,258,158,185,196,179,187,219,206,217,235,319,270,218,182,232,162,270,181,256,199,219,228,234,204,196,238,196,218,188,188,278,214,277,188,197,203,222,249,199,204,214,232,191,262,218,267,214,185,168,212,385,217,281,191,242,362,249,243,160,191,199,200,267,193,345,225,186,195,183,207,202,212,222,198,211,200,181,304]
d5 = [601, 374, 423, 305, 454, 247, 228, 268, 320, 257, 236, 233, 262, 291, 361, 295, 306, 231, 261, 248, 300, 298, 334, 303, 288, 228, 222, 316, 261, 225, 307, 247, 279, 236, 242, 528, 267, 276, 316, 246, 262, 537, 364, 233, 275, 236, 207, 442, 446, 234, 429, 264, 329, 230, 220, 246, 277, 325, 228, 241, 346, 290, 272, 197, 234, 314, 285, 241, 268, 246, 221, 249, 354, 309, 294, 255, 319, 348, 290, 253, 248, 251, 228, 227, 273, 271, 268, 249, 207, 662, 280, 233, 211, 245, 239, 289, 636, 275, 265, 259]

data = [d1, d2, d3, d4, d5]

fig, ax = plt.subplots()
pos = np.array(range(len(data))) + 1

bp = ax.boxplot(data, positions=pos, notch=1)

ax.set_xlabel('Depth of the workflow')
ax.set_ylabel('Response Time (ms)')
plt.setp(bp['whiskers'], color='k', linestyle='-')
plt.setp(bp['fliers'], markersize=3.0)
plt.show()