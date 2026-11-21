def main(): 
  for i in numString:
    index = numString.index(i)
  
    if index != 1:
      i = int(i)
      nums.append(i)
  
  max = len(nums)

  match = find_match()
  print(match)

def find_match():
  while rounds < max:
    for i in nums:
      if nums[i] + nums[i + 1] == target:
        return f"{nums[i]}, {nums[i + 1]}"
    rounds += 1


main()