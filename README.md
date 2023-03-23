# ACA_HomeWork1

Problem 1 ~ Find the Duplicates
Given an unsorted list of numbers (integers) n, find and print all the duplicates in the list.
#############################################################################################################################################
Problem 2 ~ Two Sum
You are given a list nums and an integer target. Return the indeces of the elements from n that sum to target.
Explanation:
If we take the element at index 1, which is 5 and the element at index 3 which is 7, it sums to 12. nums[1] + nums[3] == 5 + 7 == 12
#############################################################################################################################################
Problem 3 ~ Greatest Common Divisor
Create a function that takes an arbitrary number of integers (2 or more) and uses the Euclidean Algorithm to compute the greatest common divisor (GCD) for those numbers.
Explanation:
GCD(24, 36, 16) = GCD(GCD(24, 36), 16) = GCD(12, 16) = 4)
#############################################################################################################################################
Problem 4 ~ Profiling Decorator
Profiling is a way to measure the performance of the software application by measuring the resources used (time, memory, etc.) for the particular parts of it.

We want to create a decorator @profile that we can use to analyze the functions.

The decorator should write all the logs to a file, separate from the application output.

Each time a function is called in the application, it should write to the file the time, name of the function and how long it took to run it.

Example 1
from time import sleep

@profile
def foo(x):
    sleep(2)
    return x**2
   

foo(2)
sleep(60)
foo(42)
Output: (In performance.log file)
2023-03-11 21:07:51.998617 - foo(2) - 0:00:02.000984
2023-03-11 21:08:54.013414 - foo(42) - 0:00:02.001023
