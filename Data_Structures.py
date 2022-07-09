fruit = 'Banana'
length = len(fruit)
last = fruit[length - 1]
print(last)

fruit = 'banana'
index = 0
while index < len(fruit):
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
    print('All right, bananas.')