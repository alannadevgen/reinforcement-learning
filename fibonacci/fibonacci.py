from time import time


class Fibonacci:
    def __init__(
            self,
            fibonacci = {0: 0, 1: 1}
        ) -> None:
        self.fibonacci = fibonacci
    
    def compute(self, n:int):
        '''
        Return
        ------
        int
        '''
        if n in self.fibonacci.keys():
            return self.fibonacci[n]
        # compute the Fibonacci number and save it in the dictionnary
        self.fibonacci[n] = self.compute(n - 1) + self.compute(n - 2)
        return self.fibonacci[n]

    def output_result(self, n:int):
        return print(f"The result of the Fibonacci sequence for n={n} is {self.compute(n=n)}")
    
    def __str__(self) -> str:
        return f"Fibonacci sequence\n{self.fibonacci}"


if __name__ == "__main__":
    fibonacci = Fibonacci()
    fibonacci.output_result(n=10)
    fibonacci.output_result(n=15)
    print(fibonacci)
