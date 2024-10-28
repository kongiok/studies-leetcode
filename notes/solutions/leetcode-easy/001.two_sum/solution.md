# Two Sum

> Return two indices of number that can be added to get the target number. The same element cannot be used twice.

# Test cases

### Test Case 1

Input :
`nums = [2,7,11,15], target = 9`

Output :
`[0,1]`

### Test Case 2

Input:
`nums = [3,2,4], target = 6`

Output:
`[1,2]`

### Test Case 3

Input:
`nums = [3,3], target = 6`

Output:
`[0,1]`

# Thought Process

```pseudo
fun two_sum(nums: List[int], target: int)-> List[int]:
  for i in 0..len(nums):
    for j in i+1..len(nums):
      if nums[i] + nums[j] != target:
        continue;
      return [i, j]
  return []
```

我們曾經提出一個想法，使用 Binary Search 來解決這個問題，但是這個方法的時間複雜度是 O(nlogn)，而且我們需要排序整個陣列，這樣會改變原本的 index，所以我們放棄這個方法。
