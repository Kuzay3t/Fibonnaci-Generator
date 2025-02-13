# Task 1
# A fibonnaci generator written in python

sequence = []
number = int(input("Enter a number: "))

def fibonacci_generator(n):
    sequence.append(0)
    sequence.append(1)
    for i in range(1, n):
        sequence.append(sequence[i] + sequence[i-1])
    print(f" The generated sequence is {sequence}")
        
fibonacci_generator(number)