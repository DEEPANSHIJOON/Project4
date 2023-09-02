# Driver Code
arr = [10, 324, 42225, 90, 9808]
n = len(arr)
max = arr[0]
for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
print("Largest in given array ", max)
