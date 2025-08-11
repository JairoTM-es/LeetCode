class Solution(object):
    def shortestPalindrome(self,s):
        if s == "":
            return ""

        if s == s[::-1]:
            return s
        
        n = len(s)
        for i in range(1,n):
            aux = s[n-i:n]
            aux2 = aux[::-1] + s

            if aux2 == aux2[::-1]:
                break

        return aux2
