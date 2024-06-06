# name = input("Enter yo nam: ")

# print( "yo ", name)

# total_apples = 100
# num_of_apple = input("Enter no. of apples: ")

# # x = total_apples - num_of_apple #### input takes the value as an STRING

# rem_apples = total_apples - int(num_of_apple)

# print("Remmainning appless :: " , rem_apples)


#string as an array of characters
# fruit="banana"
fruit = input("Enter fruit name: ")
first_letter = fruit[0]
first_index = fruit[1]


print("First letter ",first_letter, "\nFirst index(not same as letter): ", first_index)

len_of_fruit = len(fruit)
index = 0
count_vowels = 0 
# print ("index  letter")

# while index < len_of_fruit:
#     letter = fruit[index]
#     print(index , "\t" , letter)
#     index = index+1

#above can be done in shorter way as
print("Frist 3 letters: ", fruit[0:3])
for letter in fruit:
    if letter == 'a':
        print("found an a")
        
    if letter in ['a','e','i','o','u']:
        count_vowels = count_vowels + 1

    print(letter)

print("total vowels: ", count_vowels)

