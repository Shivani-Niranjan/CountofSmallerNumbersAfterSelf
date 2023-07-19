'''
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

Input: nums = [5,2,6,1]
Output: [2,1,1,0]

Input: nums = [-1]
Output: [0]

Input: nums = [-1,-1]
Output: [0,0]
'''

def countOfSmall(array):
    result = []
    for i in range(len(array)):
        count = 0
        for j in range(i, len(array)):
            if array[i] > array[j]:
                count += 1
        result.append(count)
    return result

array=list(map(int,input().split()))
print(countOfSmall(array))