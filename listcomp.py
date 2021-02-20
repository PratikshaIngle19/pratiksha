program using for loop
# nums = [1,2,3,4]
# doubled_num = []
# for num in nums:
#     x = num * 2
#     doubled_num.append(x)
# print(doubled_num)

#program using for loop in list comprehension
# num = [1,2,3,4,5]
# x = [x*2 for x in num]
# print(x)

# name = ["colt"]
# channame = [char[0].upper() for char in name]
# print(channame)

# name = ["colt"]
# channame = [char.title() for char in name]
# print(channame)



# names = ["radha", "sham"]
# names[0], names[1] = names[1], names[0]
# print(names)





# names = ["radha", "sharda", "ram", "sham"]
# caps = [x[0].upper() for x in names]
# print(caps)


# name = "colt"
# change = [char.upper() for char in name]
# print(change)


# name = ["colt", "prateek", "pratiksha"]
# channame = [char.title() for char in name]
# print(channame)


# numbers = [1,2,3,4,5,6]
# even = [x for x in numbers if x % 2 == 0]
# odd = [x for x in numbers if x % 2 != 0]
# print(even)
# print(odd)

# numbers = range(0,10)
# num = [ 1+(x*2) for x in numbers]
# print(num)


nums = [(x * 2)+1 for x in range(0,10)]
print(nums)

numbers = range(0,10,2)
num = [ 1+(x*2) for x in numbers]
print(num)


# number = [1,2,3,4,5,6]
# seq_num = [num*2 if num %2 == 0 else num/2 for num in number]
# print(seq_num)

# with_vowel = "this is so much fun"
# without_vowel = [char for char in with_vowel if char not in "aeiou"]
# print(without_vowel)

# with_vowel = "this is so much fun"
# without_vowel = ''.join(char for char in with_vowel if char not in "aeiou")
# print(without_vowel)


