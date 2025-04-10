# CMPS 2200 Recitation 06
## Answers

**Name:**Michael Baron **Name:**Troy Freed

Place all written answers from recitation-07.md here for easier grading.

2)

Work Equation is W(n) = F(n-1) + F(n-2) + O(1) and O(1) for both base cases n = 1 and n = 1

this means the work grows exponentially with n, making it O(2^n) though more specifically O(1.618^n) as that is the golden ratio number

3) Span is the longest tree, meaning S(n) = F(n-1) +O(1) and O(1) for base cases

which also grows exponentially in the form of O(2^n-1)

so span can be shown as O(n)

4) the pattern that emerges is counts from index 1 to the final index if the reverse of the fib sequence (also misses the startign 0)

so for n = 10 there will be 11 elements in counts and counts[10] will = fib 1, counts[9] will = fib number 2, etc.

the caviot to this is counts[0] = counts[2]. the reason for this is becasue the first element of counts is how many times

base case zero is reached, and will be equal to the amount of times F(2) is called sicne it will only be reached on n=2 on f(n-2).

this shows how inefficient it is since the large numbers are being counted only a few times while the small ones our being counted an exponentially increasing amount

6)

while a value could be called twice while cascading up, but each value will only be computed once, after this, the given value i will be retrieved from the stored values.

this means that both the span and work are O(n)

8) the maximum times a value Fi will be read is two, one as F(n-1) and another time as F(n-2)

the sequential nature of this keeps work and span at O(n)
