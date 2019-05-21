class Fibonacci:
    def findFibonacci(self, num):
        fibo_list = []
        if num == 0:
            fibo_list.append(0)
        elif num == 1:
            fibo_list.append(0)
            fibo_list.append(1)
        elif num >= 2 and isinstance(num, int):
            fibo_list.append(0)
            fibo_list.append(1)
            for i in range(2,num+1):
                fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
        else:
            return "The given number is not a index"
        return fibo_list[num]
        
fibo = Fibonacci()
print(fibo.findFibonacci(8.5))
            