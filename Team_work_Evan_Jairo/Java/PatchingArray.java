public class PatchinArray 
{
    public static void main(String[] args)
     {
        //test case for the code
        int[] array = {1, 3};
        int n = 6;
        patchesNeeded(array, n);
    }

    public static void patchesNeeded(int[] array, int n) 
    {
        long nextMissing = 1; 
        int index = 0;        
        int patches = 0;     

        while (nextMissing <= n) 
        {
            if (index < array.length && array[index] <= nextMissing) 
            {
                nextMissing += array[index];
                index++;
            } else 
            {
            patches++;
                nextMissing += nextMissing;
            }
        }
        System.out.println("Patches needed: " + patches);
    }
}

