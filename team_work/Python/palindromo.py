class Solution(object):
    def shortestPalindrome(self, s):
        if len(s)==0:
            return ("")
        if s == s[::-1]:
            return (s)
        palindromo = True
        n = len(s)
        for i in range(1,n):
            aux = s[n-i:n]
            print(aux)
            aux2 = aux[::-1] + s
            
            print(aux2)
            if aux2 == aux2[::-1]:
                break
                
        return aux2
s="aaeceaaa"


