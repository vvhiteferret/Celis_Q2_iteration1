while True:
    n = int(input("Enter number: "))
    if n > 0:
        break 
    print("Invalid input. Please enter a number greater than 0.")

s = n * (n + 1) // 2 
print("Expected sum is", s)
def getSum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print("After calling the function getSum, the sum of all numbers from 1 to", n, "is:", getSum(n))
if getSum(n) == s:
    print("Output Verified.")