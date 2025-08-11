function shortestPalindrome(s: string): string {
    if (s === "") {
        return "";
    }

    const reverse = (str: string): string => str.split("").reverse().join("");

    if (reverse(s) === s) {
        return s;
    }

    const n = s.length;
    let aux2 = "";

    for (let i = 1; i < n; i++) {
        const aux = s.slice(n - i);
        aux2 = reverse(aux) + s;

        if (aux2 === reverse(aux2)) {
            break;
        }
    }

    return aux2;
}
