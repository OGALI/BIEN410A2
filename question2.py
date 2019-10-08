import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.ticker as plticker

# Initial sequence; seq2 sequence is row, second seq1 is col
# seq1 = 'GAATACAGTTATGCTA'
# seq2 = 'GGATGCGTGATCTG'

seq1 = 'GATTACA'
seq2 = 'GATAGA'
#Matrix of zeros
LCSPlot = np.zeros([len(seq1), len(seq2)])

for row in range(len(seq1)):
    for col in range(len(seq2)):
        if seq1[row] == seq2[col]:
            if row == 0 or col == 0:
                LCSPlot[row, col] = 1
            else:
                LCSPlot[row, col] = LCSPlot[row -1, col-1] + 1
        else:
            LCSPlot[row, col] = 0

LCSPlot = LCSPlot.transpose()
print(LCSPlot)

fig, ax1 = plt.subplots(1,1)

imgplot = ax1.imshow(LCSPlot)

# why first label not showing
# loc = plticker.MultipleLocator(base=1) # this locator puts ticks at regular intervals
# ax1.xaxis.set_major_locator(loc)
# ax1.yaxis.set_major_locator(loc)
ax1.set_xticks(range(len(seq1)))
ax1.set_yticks(range(len(seq2)))
ax1.set_xticklabels(list(seq1))
ax1.set_yticklabels(list(seq2))
plt.show()

# gets the allignment
max = np.amax(LCSPlot)
max_index = np.where(LCSPlot == np.amax(LCSPlot))
allign = seq1[int(max_index[0]-max+1):int(max_index[0]+1)]
print('Best sequence allignment: ' + allign)