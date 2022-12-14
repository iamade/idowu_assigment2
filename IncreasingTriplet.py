def increastingTriplet(nums):
    first_num = float('inf')
    second_num = float('inf')
    for n in nums:
        if n <= first_num:
            first_num = n
        elif n <= second_num:
            second_num = n 
        else:
            return True
    return False

# nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
print(increastingTriplet(nums))