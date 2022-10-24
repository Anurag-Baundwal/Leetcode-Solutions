class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        lst = [" "] * n
        for i in range(0, n):
            if (i+1)%3 == 0:
                if (i+1)%5 == 0: lst[i] = "FizzBuzz"
                else: lst[i] = "Fizz"
            elif (i+1)%5 == 0: lst[i] = "Buzz"
            else: lst[i] = str(i+1)

        return lst 

sol = Solution()
print(sol.fizzBuzz(3))
print(sol.fizzBuzz(5))
print(sol.fizzBuzz(15))