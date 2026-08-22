class Solution(object):
    def checkDivisibility(self, n):
        if n <= 9 :
            return False 
        num = n
        s = 0
        p = 1 
        while(num != 0):
            n1 = num%10
            num = num//10
            s += n1
            p = p*n1
        if  n % (s + p)  == 0 :
            return True
        return False

        