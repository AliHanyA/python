class Solution(object): 
    def sumOfMultiples(self, n):
        sum = 0  # Total results
        for i in range(1,n+1):  # for 1  ==>  n
            if i %3==0 or i%5==0 or i%7==0:  # cheek
                sum +=i   # to total results
        return(sum)    # out put
