from tokenize import String


def pal(num):
     x1 = num[::-1]
     if x1 == num:
       print('palindrome')
     else:
       print('not a palindrome')
       print(x1)
    

print("enter word")
words = input()
pal(words)
