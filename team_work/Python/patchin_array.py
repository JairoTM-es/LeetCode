def patchesNeeded(array, n):

    faltantes = 1
    i = 0
    patches = 0

    while faltantes <= n:
        if i < len(array) and array[i] <= faltantes:
            faltantes += array[i]
            print("missing atches: " + str(faltantes))
            i += 1
        else:
            patches += 1
            faltantes += faltantes

    print("Patches needed: " + str(patches))

array = [1, 3]
n = 6
patchesNeeded(array, n)