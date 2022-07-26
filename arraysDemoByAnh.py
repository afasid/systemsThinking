# square bracket mean array
numberArray = [10, 20, 30, 40, 50, 60]

print(numberArray[4])

# len() can tell us how big an array is
print(numberArray[len(numberArray)-1])

print("--------------------------------")

index = 0

# reading elements in an array
while(index < len(numberArray)):
  print(numberArray[index])
  index += 1

print("------------------------------")

# adding elements to an array
numberArray.append(100)
userInput = input("Enter a number")
numberArray.append(int(userInput))

# a newer way of reading array elements
# fun extra type() will give the data type of a variable

for num in numberArray:
  print(num, type(num))

# find the sum of an array
total = 0
for num in numberArray:
  total += num

print("total of numberArray is", total)

print("------------ Functions ------------------")

# ---------------- Functions --------------------------
def sayHello(name, surname):
  print("Hello", name, surname)

# a function won't execute until it is called
sayHello("Anh", "Nguyen")

  
# this function has parameters (inputs) and returns (output)
def getTotal(array):
  total = 0
  for num in array:
    total += num

  return total

newArray = [5, 5, 10]

print(getTotal(numberArray))
newTotal = getTotal(newArray)
print(newTotal)



