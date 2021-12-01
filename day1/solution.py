

with open("input.txt") as f:
    lines_str = f.read().splitlines()
    
nums = [int(s) for s in lines_str]

# Part 1
def count_increases(nums):
    increase_count = 0
    for i, _ in enumerate(nums):
        if i == 0:
            continue
        
        if nums[i] > nums[i-1]:
            increase_count += 1
            
    return increase_count

print(count_increases(nums))

# Part 2
nums1 = nums[:-2]
nums2 = nums[1:-1]
nums3 = nums[2:]

triplets = [sum(z) for z in zip(nums1, nums2, nums3)]

print(count_increases(triplets))
