function maxProfit(prices: number[]): number {
    if (prices.length === 0) {
        return 0;
    }

    const n = prices.length;
    const der: number[] = new Array(n).fill(0);
    const izq: number[] = new Array(n).fill(0);

    let precioMin = prices[0];
    let profit = 0;

    for (let i = 1; i < n; i++) {
        precioMin = Math.min(precioMin, prices[i]);
        izq[i] = Math.max(izq[i - 1], prices[i] - precioMin);
    }

    let precioMax = prices[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        precioMax = Math.max(precioMax, prices[i]);
        der[i] = Math.max(der[i + 1], precioMax - prices[i]);
    }

    for (let i = 1; i < n; i++) {
        profit = Math.max(profit, der[i] + izq[i]);
    }

    return profit;
};
