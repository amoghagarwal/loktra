reference_string = "acdegilmnoprstuw"


def reverse_hash(h):

    index = []
    i = 0
    # dividing by 37 and storing remainders in list called index
    while h>37:
        index.append(h % 37)
        i += 1
        h /= 37

    word = ""
    for j in range(len(index) - 1, -1, -1):
        word += reference_string[index[j]]

    return word

print reverse_hash(680131659347)

0 1 2 3 4 5 6 7 8
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 1 0 0

current
maxi
mini