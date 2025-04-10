def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """
    counts[n] += 1
    """
    in terms of what they are looking for:
    figure out if i am returning the total work as a sum of all and the list is how many times each is counted
    or if they want the final fib number 
    """
    ###TODO
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

    
def fib_top_down(n, fibs):
    ###TODO
    print(f"N = {n} fibs: {fibs}")
    if n == 0:
        fibs[0] = 0
        return 0
    if n == 1:
        fibs[1] = 1
        return 1
    if fibs[n] != -1:
        return fibs[n]
    else:
        left, right = fib_top_down(n-1, fibs) , fib_top_down(n-2, fibs)
        print("left: ",left)
        fibs[n] = left + right
        print(f"fibsN = {fibs[n]}")
        return fibs[n]

def fib_bottom_up(n):
    fibs = [0] * (n + 1)
    if n>= 1:
        fibs[1] = 1
    for i in range(2, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]

    return fibs[n]
