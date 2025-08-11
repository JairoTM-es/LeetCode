def patchesNeeded(array, n):

    valFaltantes = 1
    i = 0
    patches = 0

    while valFaltantes <= n:
        if i < len(array) and array[i] <= valFaltantes:
            valFaltantes += array[i]
            i += 1
        else:
            patches += 1
            valFaltantes += valFaltantes

    print("Patches needed: " + str(patches))

array = [1, 3]
n = 6
patchesNeeded(array, n)