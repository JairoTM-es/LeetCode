function patchesNeeded(array: number[], n: number): void {
    let nextMissing: number = 1;
    let index: number = 0;
    let patches: number = 0;

    while (nextMissing <= n) {
        if (index < array.length && array[index] <= nextMissing) {
            nextMissing += array[index];
            index++;
        } else {
            patches++;
            nextMissing += nextMissing;
            console.log("nextMissing: " + nextMissing);
        }
    }
    console.log("Patches needed: " + patches);
}

// Test case
const array: number[] = [1, 3];
const n: number = 6;
patchesNeeded(array, n);