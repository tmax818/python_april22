# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)


# x = [99,4,2,5,-3]
# print(x[:])
# #the output would be [99,4,2,5,-3]
# print(x[1:])
# #the output would be [4,2,5,-3];
# print(x[:4])
# #the output would be [99,4,2,5]
# print(x[2:4])
# #the output would be [2,5];

nums = [0,1,2,3,4,5,6,7,8,9]
start = 0
stop = 10
step =1

print(nums[start:stop:step])

nums = [0,1,2,3,4,5,6,7,8,9]
nums.append(10)
print(nums)

dog = ("Canis Familiaris", "dog", "carnivore", 12)
print(id(dog))
dog = dog + ("domestic",)
print(id(dog))
