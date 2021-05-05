def check_distinct(nums):
    # Given an integer array nums
    # return true if any value appears at least twice in the array
    # and return false if every element is distinct
    return len(set(nums)) == len(nums)


def find_target(num, target):
    # Given an array of integers num and an integer target
    # return indices of the two numbers such that they add up to target.
    # You may assume that each input would have exactly one solution
    # and you may not use the same element twice.
    # You can return the answer in any order.
    x = None
    y = None
    for n in num:
        x = n
        for _n in num:
           y = _n 
           if x + y == target: 
               return x, y 
    return x, y


def reverse_string(s):
    # Write a function that reverses a string. 
    # The input string is given as an array of characters s
    return [_s for _s in reversed(s)]

def is_palindrome(s):
    # Given a string s, determine if it is apalindrome
    # considering only alphanumeric characters and ignoring cases
    ls = list(s)
    return ls == [_s for _s in reversed(s)]


def first_none_repeating(s):
    # Given a string s
    # return the first non-repeating character in it
    # and return its index. If it doesnot exist, return -1
    ls = list(s)
    for i, char in enumerate(ls):
        if ls.count(char) == 1:
            return i
    return -1


def fizzbuzz(n):
    # Given an integer n, return a string array answer (1-indexed) where:
    # - answer[i] == "FizzBuzz" if i is divisibleby 3 and 5.
    # - answer[i] == "Fizz" if i is divisible by 3.
    # - answer[i] == "Buzz" if i is divisible by 5.
    # - answer[i] == i if non of the above conditions are true.
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return None

def primes_less_than(n):
    # Count the number of prime numbers less than a non-negative number, n.
    c = 0
    for _n in range(0, n):
        # prime numbers are greater than 1
        if _n > 1:
            for i in range(2, _n):
                if (_n % i) == 0:
                    break
            else:
                c +=1 
    return c

def reverse_digits(x):
    # Given an integer x, return x with its digits reversed.
    x_str = reversed(list(str(x)))
    return int(''.join([s for s in x_str]))


def main():
    print("CHECK DISTINCT")
    print(check_distinct([1,2,3,4,5]))
    print(check_distinct([1,2,3,3,4,5]))
    print(check_distinct([1,2,3,3,4,5,6,9,9]))

    print("CHECK DISTINCT")
    print(find_target([1, 2, 3], 5))
    print(find_target([1, 3, 4, 6], 9))

    print("REVERSE STRING")
    print(reverse_string(['c', 'b', 'a']))
    print("IS PALINDROME")
    print(is_palindrome('anna'))

    print("FIRST NONE REPEATING")
    print(first_none_repeating('abc'))
    print(first_none_repeating('aabbc'))
    print(first_none_repeating('aabbcc'))

    print("FIZZBUZZ")
    print(fizzbuzz(15))
    print(fizzbuzz(9))
    print(fizzbuzz(20))
    print(fizzbuzz(7))

    print("PRIMES")
    print(primes_less_than(7))
    print("REVERSE DIGITS")
    print(reverse_digits('312'))
    print(reverse_digits('654'))

if __name__ == '__main__':
    main()
