
from collections import Counter

sentences = ['Mary read a story to Sam and Isla.', 'Isla pushed Sam.', 'Sam fell down.']

res = Counter('Mary Had a Little Lamb')
print("Count of all characters in sentences is :\n " + str(res))

test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4]

# printing original list
print("Original list : " + str(test_list))

# using max() + set() to
# get most frequent element
res = max(set(test_list), key=test_list.count)

# printing result
print("Most frequent number is : " + str(res))


def isPalindrome(s):
    # Using predefined function to
    # reverse to string print(s)
    #rev = ''.join(reversed(s))

    # Checking if both string are
    # equal or not
    if s == ''.join(reversed(s)):
        return True
    return False


# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")