import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# # Initial sequence; first sequence is row, second seq2 is col
# seq1 = 'GAATACAGTTATGCTA'
# seq2 = 'GGATGCGTGATCTG'
seq1 = 'GATTACA'
seq2 = 'GATAGA'

#Matrix of zeros
dotPlot = np.zeros([len(seq1), len(seq2)])

for row in range(len(seq1)):
    for col in range(len(seq2)):
        if seq1[row] == seq2[col]:
            dotPlot[row, col] = 1
        else:
            dotPlot[row, col] = 0

dotPlot = dotPlot.transpose()
print(dotPlot)

fig, ax1 = plt.subplots(1,1)
imgplot = ax1.imshow(dotPlot)
ax1.set_xticks(range(len(seq1)))
ax1.set_yticks(range(len(seq2)))
ax1.set_xticklabels(list(seq1))
ax1.set_yticklabels(list(seq2))

plt.show()


