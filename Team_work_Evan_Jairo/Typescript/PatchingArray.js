function patchesNeeded(array, n) {
    var nextMissing = 1;
    var index = 0;
    var patches = 0;
    while (nextMissing <= n) {
        if (index < array.length && array[index] <= nextMissing) {
            nextMissing += array[index];
            index++;
        }
        else {
            patches++;
            nextMissing += nextMissing;
            console.log("nextMissing: " + nextMissing);
        }
    }
    console.log("Patches needed: " + patches);
}
// Test case
var array = [1, 3];
var n = 6;
patchesNeeded(array, n);
