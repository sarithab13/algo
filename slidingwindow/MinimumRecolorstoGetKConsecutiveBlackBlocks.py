def minimumRecolors(self, blocks: str, k: int) -> int:
    i = 0
    j = 0
    nw = 0
    mn = float('inf')
    while (j < len(blocks)):
        if (blocks[j] == 'W'):
            nw += 1
        if (j - i + 1 < k):
            j += 1
        elif (j - i + 1 == k):
            mn = min(nw, mn)

            if (blocks[i] == 'W'):
                nw -= 1
            i += 1
            j += 1
    return mn