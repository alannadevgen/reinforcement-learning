from time import time


class Fibonacci:
    def __init__(
        self,
        fibonacci={0: 0, 1: 1}
    ) -> None:
        '''
        Create a Fibonacci sequence

        Attributes
        ----------
        fibonacci: dict
            pre-filled dictonnary with some initial values 
        '''
        self.fibonacci = fibonacci    

    def compute(self, n: int):
        '''
        Computes the Fibonacci sequence and returns the last element
        of the sequence given a integer.
        
        The Fibonacci sequence is given by:
            - F[0] = 0
            - F[1] = 1
            - F[i] = F[i-1] + F[i-2] for i >= 2

        Parameters
        ----------
        n: int
            number of iterations

        Returns
        ------
        int
            value of the last element of the sequence given n
        '''
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got {n}')
        elif n < len(self.fibonacci):
            return self.fibonacci[n]
        elif n in self.fibonacci.keys():
            return self.fibonacci[n]
        # compute the Fibonacci number and save it in the dictionnary
        self.fibonacci[n] = self.compute(n - 1) + self.compute(n - 2)
        return self.fibonacci[n]

    def output_result(self, n: int):
        '''
        Output the result as it should be displayed.

        Parameters
        ----------
        n: int
            number of iterations
        '''
        start_time = time()
        result = self.compute(n=n)
        execution_time = time() - start_time
        return print(f"The result of the Fibonacci sequence for n={n} is {result} (took {execution_time:.6f} seconds)")

    def __str__(self) -> str:
        '''
        Print the Fibonacci sequence created.
        '''
        return f"Fibonacci sequence\n{self.fibonacci}"


if __name__ == "__main__":
    fibonacci = Fibonacci()
    fibonacci.output_result(n=10)
    fibonacci.output_result(n=9)
    fibonacci.output_result(n=12)
    # results = [fibonacci.compute(n=number) for number in range(15)]
    # print(results)
    print(fibonacci)
