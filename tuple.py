nums = (1, 4, 9, 16, 26, 36, 49, 64, 81, 100)
x = 49

i = 0 
while i < len(nums):
    if (nums[i] == x):
        print("FOUND at idx", i)
    i += 1