class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)
        der = [0] * n
        izq = [0] * n

        precioMin = prices[0]

        profit = 0

        for i in range(1,n):
            precioMin = min(precioMin,prices[i])
            izq[i] = max(izq[i-1],prices[i]-precioMin)

        
        precioMax = prices[n-1]
        for i in range(n-2,-1,-1):
            precioMax = max(precioMax,prices[i])
            der[i] = max(der[i+1],precioMax-prices[i])
            
        for i in range(1,n):
            profit = max(profit, der[i]+izq[i])
            
        return profit
