def sort(viborka):
    less = []
    equal = []
    greater = []

    if len(viborka) > 1:
        core = viborka[0][1]
        for x in range(len(viborka)):
            if viborka[x][1] < core:
                less.append(viborka[x])
            if viborka[x][1] == core:
                equal.append(viborka[x])
            if viborka[x][1] > core:
                greater.append(viborka[x])
        return sort(less) + equal + sort(greater)
    else:
        return viborka
