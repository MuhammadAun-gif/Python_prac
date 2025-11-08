from array import array

nums = array('i', [1, 2, 3, 4, 5])

def reverse_array(nums):
    return nums[::-1]

reversed_nums = reverse_array(nums)
print(reversed_nums)

print(nums[4:0:1]) 