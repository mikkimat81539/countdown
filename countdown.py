"""Create a countdown timer that counts down from a specified number of seconds,
using a for loop to decrement the time."""

nums = int(input("Input the number you want to countdown from. "))

for i in range(nums):
    countdown = nums - i
    print(countdown)
