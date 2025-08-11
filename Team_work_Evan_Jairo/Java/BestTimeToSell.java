class Solution {
    public int maxProfit(int[] prices) {
        if(prices == null){
            return 0;
        }

        int n = prices.length;
        int[] der = new int[n];
        int[] izq = new int[n];

        int precioMin = prices[0];
        int profit = 0;

        for(int i=1;i<n;i++){
            if(precioMin>prices[i]){
                precioMin = prices[i];
            }

            if(izq[i-1] > (prices[i]-precioMin)){
                izq[i] = izq[i-1];
            }else{
                izq[i] = prices[i]-precioMin;
            }
        }

        
        int precioMax = prices[n-1];
        for(int i=n-2;i>=0;i--){
            if(precioMax<prices[i]){
                precioMax = prices[i];
            }

            if(der[i+1] > (precioMax-prices[i])){
                der[i] = der[i+1];
            }else{
                der[i] = precioMax-prices[i];
            }
        }

        for(int i=0;i<n;i++){
            if(profit<(der[i]+izq[i])){
                profit = der[i]+izq[i];
            }
        }
            
        return profit;
    }
}
