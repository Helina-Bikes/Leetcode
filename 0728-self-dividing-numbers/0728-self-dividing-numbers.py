class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_div_number(num):  
            for digit in str(num):
                if digit=='0' or num % int(digit)!=0:
                    return False
            return True      



        result=[]
        for num in range(left,right+1):
           if self_div_number(num):
                 result.append(num)
        return result     