rm(list = ls())
# Fibonacci sequence up to n-th term using recursive functions
fibonacci <- data.frame(n = c(0, 1), result = c(1, 1))
str(fibonacci)
recursive.fibonacci <- function(n) {
  if(n <= 1) {
    return(n)
  } else if (n %in% fibonacci$n) {
    # if already computed
    row_index <- which(fibonacci$n == n)
    return (fibonacci %>% select(result) %>% dplyr::filter(row_number() == row_index))
  } else {
    # save the result and return it
    new_result <- recursive.fibonacci(n-1) + recursive.fibonacci(n-2)
    fibonacci %>% add_row(n = n, result = new_result)
    fibonacci[nrow(fibonacci) + 1,] = c(n, new_result)
    return(new_result)
  }
}

recursive.fibonacci(3)
recursive.fibonacci(5)
