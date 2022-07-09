fruit = 'Banana'  #this is from a long txt file titled "m-box"
length = len(fruit)
last = fruit[length - 1]
print(last)

fruit = 'banana'
index = 0
while index < len(fruit): #counts the length of the string
    letter = fruit[index]
    print(letter)
    index = index + 1

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
    print(count)

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.') #Here is the final output
