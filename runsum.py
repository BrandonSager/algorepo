#june 30

nums = [4,6,8,3]

def runningsum(nums):

	runsum = 0
	for i in nums:
		runsum += i
	return runsum

print(runningsum(nums))
