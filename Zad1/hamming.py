def distance(first, second):
    difference = 0
    if len(first)==len(second):
        for i in range(len(first)):
            if first[i] != second[i]:
                difference += 1
        return difference
    else:
        raise ValueError('Genotypy są różnej długości')
