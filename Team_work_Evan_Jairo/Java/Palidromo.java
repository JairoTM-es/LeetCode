public class Solution {
    public String shortestPalindrome(String s) {
        if (s == null || s.isEmpty()) {
            return "";
        }

        if (new StringBuilder(s).reverse().toString().equals(s)) {
            return s;
        }

        int n = s.length();
        String aux2 = "";

        for (int i = 1; i < n; i++) {
            String aux = s.substring(n - i);
            String reversedAux = new StringBuilder(aux).reverse().toString();
            aux2 = reversedAux + s;

            String reversedAux2 = new StringBuilder(aux2).reverse().toString();
            if (aux2.equals(reversedAux2)) {
                break;
            }
        }

        return aux2;
    }
}
