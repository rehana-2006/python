# Given an array of positive integers find the GCD amongst them.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_gcd_of_array(arr):
    result = arr[0]     
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result


arr = [8, 12, 16]
print(find_gcd_of_array(arr))



# Input: [8, 12, 16]
# Output: 4
# Explanation: GCD(8, 12) = 4 → GCD(4, 16) = 4