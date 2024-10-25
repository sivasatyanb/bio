def prefixSumArray(array, startIndex, endIndex, k):
    n = len(array)
    b = [0] * (n+1)

    b[startIndex] += k 
    b[endIndex + 1] -= k

    prefixSum = 0
    for i in range(n):
        prefixSum += b[i]
        array[i] += prefixSum

    return array

array = [1, 2, 3, 4, 5]
modifiedArray = prefixSumArray(array.copy(), startIndex=1, endIndex=3, k=10)
print(*modifiedArray)