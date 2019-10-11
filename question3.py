import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.ticker as plticker


# Correct
def createPMatrix(dims):
    P = np.array(['    '])
    for i in range(dims[0] * dims[1]-1):
        P = np.append(P, '')
    P = np.reshape(P, dims)
    return P

# Correct
def initialFill(S, P):
    dims = S.shape
    for i in range(dims[1]):
        S[0, i] = -i
        P[0, i] = 'H'
    for i in range(dims[0]):
        S[i, 0] = -i
        P[i, 0] = 'V'
    P[0, 0] = ''


# TODO not adding multiple paths
# fills one grid of S and P; pos is the position to fill
def fillNext(pos):
    # initialize the score for each option; opt1 diag, opt2 horiz, opt3 verti
    x, y = pos

    # option
    opt1 = int(S[y - 1, x - 1] + scheme['miss'])
    opt2 = int(S[y, x - 1] + scheme['gap'])
    opt3 = int(S[y - 1, x] + scheme['gap'])
    if seq1[y] == seq2[x]:
        opt1 = int(S[y-1, x-1] + scheme['match'])


    opts = [opt1, opt2, opt3]
    newScore = max(opts)

    # check if this works
    indexOfBest = [i for i, x in enumerate(opts) if x == newScore]
    bestMove = ''
    for i in range(len(indexOfBest)):
        if indexOfBest[i] == 0:
            bestMove = bestMove + 'D'
        if indexOfBest[i] == 1:
            bestMove = bestMove + 'H'
        if indexOfBest[i] == 2:
            bestMove = bestMove + 'V'

    S[y, x] = newScore
    P[y, x] = bestMove



# Correct
# fills out the whole grids of S and P
def fillAll(dims):
    for x in range(1, dims[0]):
        for y in range(1, dims[1]):
            fillNext((x, y))


# # TODO multiple solutions fix
# # def tracer(dims):
# #     # remove 1 cuz length is mag
# #     dimY = dims[0]-1
# #     dimX = dims[1]-1
# #
# #     allign = str(seq1[dimY])
# #     print(dimY, dimX, P.shape)
# #     print(P[16, 14])
# #     while dimY > 0 and dimX > 0:
# #         if P[dimY, dimX] == 'D':
# #             dimX = dimX -1
# #             dimY = dimY -1
# #             allign = allign + str(seq2[dimX])
# #         elif P[dimY, dimX] == 'H':
# #             dimX = dimX - 1
# #             allign = allign + str(seq2[dimX])
# #         elif P[dimY, dimX] == 'V':
# #             dimY = dimY - 1
# #             allign = allign + str(seq2[dimX])
# #         # dimX = dimX - 1
# #         # dimY = dimY - 1
# #     print(allign[::-1])




# Initial sequence; seq2 sequence is row, second seq1 is col
# Given sequence to align

# seq1 = 'GAATACAGTTATGCTA'
# seq2 = 'GGATGCGTGATCTG'
seq1 = 'GATTACA'
seq2 = 'GATAGA'

seq1 = "-"+seq1
seq2 = "-"+seq2
# scheme = [1, 0, -1]
# scheme = [3, -1, 0]
scheme = {'match':1, 'miss':0, 'gap':-1}


dims = (len(seq1), len(seq2))
S = np.zeros(dims)
P = createPMatrix(dims)
initialFill(S, P)
# dims = (len(seq1)-1, len(seq2)-1)
fillAll(dims)
# fillNext((1,1))

# tracer(dims)
#
# S = S.transpose()
# P = P.transpose()
print(S)
print(P)

# Plot the figures
fig, ax1 = plt.subplots(1,1)
imgplot = ax1.imshow(S)
# ax1.set_xticks(range(len(seq1)))
# ax1.set_yticks(range(len(seq2)))
# ax1.set_xticklabels(list(seq1))
# ax1.set_yticklabels(list(seq2))
plt.show()
