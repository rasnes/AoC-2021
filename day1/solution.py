

with open("input.txt") as f:
    lines_str = f.read().splitlines()
    
nums = [int(s) for s in lines_str]

def count_increases(nums):
    increase_count = 0
    for i, num in enumerate(nums):
        if i == 0:
            continue
        
        if nums[i] > nums[i-1]:
            increase_count += 1
            
    return increase_count

print(count_increases(nums))