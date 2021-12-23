class Solution:
    def reverse(self, x: int) -> int:
        """
        from https://www.youtube.com/watch?v=Io9ujnnR4sI
        pop the last digit of the number, push it to the back of result (by pushing the result forward by one digit)
        repeat the process

        (In the process, to prevent overflow, check whether the result will be overflown if updated)
        """
        def divide(number,divider):
            return int(number*1.0/divider)
        def mod(number,m):
            if number<0:
                return number% -m
            return number%m
        MIN_INT=-2**31 #-2147483648
        MAX_INT=2**31-1 #2147483647
        
        result=0
        while x!=0:
            last=mod(x,10)
            x=divide(x,10)
            if result>divide(MAX_INT,10) or (result==divide(MAX_INT,10) and last>7):
                return 0
            if result<divide(MIN_INT,10) or (result==divide(MIN_INT,10) and last<-8):
                return 0
            result=result*10+last
                    
        return result
        
            