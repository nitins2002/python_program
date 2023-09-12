# ============================================
# 1#Concat Strings .
# ============================================
str1 = "abc"
str2 = "xyz"
str3 = "pqr"

res_str = str1 + str2 + str3
print(res_str)

##lets suppose we have list of string
Lst = [str1, str2, str3]
Res_str =””
For
item in Lst:
Res_str = res_str + item

# ============================================
# 2.Split String .
# ============================================

String
s1 = "Tejas,Prashant,Borse";
String[]
newString = s1.split(",");

for (String a: newString) {
    System.out.println(a);



Larger Number   int a =
# ============================================
# 3.larger number.
# ============================================


def larger_num(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif a == b:
        print(f"{a} is equal to {b}")
    else:
        print(f"{b} is greter than {a}")


# ====================================================
# 4./*Number of Upper And Lower Characters in a String.
# ====================================================

s2 = "nitinpankaj"
upper = 0
lower = 0

for ch in s2:
    if ch.isupper():
        upper += 1
    else:
        lower += 1

print("upper case:", upper)
print("lower case:", lower)

# ==============================================
# 5./*Factorial .
# ==============================================

n = int(input("Enter the number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} is {factorial}")

# ==============================================
# 6./*Reverse a No .
# ==============================================

print("Enter the number:")
n = int(input())

reverse = 0

while n != 0:
    reverse = reverse * 10 + n % 10
    n = n // 10

print("Reversed number:", reverse)

# ===================================
# 7./*Palindrome.
# ===================================

print("Enter the number:")
n = int(input())

rev = 0
a = n

while a != 0:
    rev = rev * 10 + a % 10
    a = a // 10

if rev == n:
    print("Number is Palindrome")
else:
    print("Number isn't Palindrome")

# ==========================================
# 8./*Armstrong .
# ==========================================

"""An Armstrong number (also known as a narcissistic number or pluperfect number)
is a number that is equal to the sum of its own digits each raised to the
power of the number of digits.
For example, let's take the number 153:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153"""


def Armstrong(a):
    # Casting
    num_str = str(a)

    # lenth function collection:str,list ,map ,tuple
    l = len(num_str)

    # list compresion
    digits = [int(n) for n in num_str]

    # iterate digits
    sum = 0
    for digit in digits:
        sum = sum + (digit ** l)

    if sum == a:
        return True
    else:
        return False


# ===========================================================
# 9./*Print the Armstrong number available between 0 to 1000.
# ===========================================================

for i in range(1, 1000):
    num = 1
    sum = 0
    num_digits = len(str(i))

    while num > 0:
        digit = num % 10
        sum += digit ** digits
        sum //= 10

    if sum == i:
        print(i)
# =======================================================
# 10./*To print the palindrome available between 0 to 100.
# =======================================================


for i in range(1, 100):
    num = i
    rev = 0
    num_digits = len(str(i))

    while num > 0:
        digit = num % 10
        rev += digit ** num_digits
        num //= 10

    if rev == i:
        print(i)

# ============================================================
# 11./* Print the count of the given number .
# ============================================================
n = int(input("Enter the number: "))
cnt = 0
while n != 0:
    n = n // 10
    cnt += 1
print("Number of digits in the given number is", cnt)


# ===================#
def count_digits(n):
    cnt = 0
    while n != 0:
        n = n // 10
        cnt += 1
    return cnt


n = int(input("Enter the number: "))
digit_count = count_digits(n)
print("Number of digits in the given number is", digit_count)

# ===============================================================
# 12./* Find the Sum of the digit.
# ===============================================================
n = int(input("Enter the no "))
sum = 0
while n != 0:
    sum += n % 10
    n = n // 10
print(sum)


# ======================
def sum_of_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum


n = int(input("Enter the number: "))
result = sum_of_digits(n)
print("The sum of the digits in the given number is", result)

# =================================================================
# 13.Fibonacci series:
# ====================================================================

n = int(input("Enter the number of Fibonacci terms to generate: "))
a, b = 0, 1
print("Fibonacci series up to", n, "terms:")
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1


# ========
def fibonacci_series(n):
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

    return count


n = int(input("Enter the number: "))
result = fibonacci_series(n)
print("\nFibonacci series up to", n, "terms:")
# =========================================================
# 14./*Fibonacci series: upto 100.
# =========================================================
a, b = 0, 1
print(a, b)

for _ in range(100):  # such like that the fibonacci_series number 0 1 1 2 3 5 8 13 21 so on...
    c = a + b

    if c > 100:
        break

    print(c)

    a, b = b, c
# ==========================================================
# 15./*Reverse a string.
# ==========================================================
print("Enter the String - ")
String
s = sc.nextLine()
String
rev = ""
for (int i=s.length() - 1; i >= 0; i--)
rev = rev + s.charAt(i)
print(rev)

s = "name "
rev = s[::-1]
print(rev)
# ============================================================
# 16./*Count a string.
# ============================================================
System.out.print("Enter the String - ");
String
s = sc.nextLine();
int
c = 0;
for (int i=0; i < s.length(); i++) {
c++;
}
System.out.println(c); * /

x = "nitin solunke"
c = 0
for char in x:
    c += 1
    print(c)
# ==================================================================
# 17.//Count of each Word in given string.
# =================================================================
s = "I am good and I am having good day"
s1 = s.split()
for i in range(len(s1)):
    cnt = 0
    a = s1[i]
    for j in range(len(s1)):
        b = s1[j]
        if j < i and b == a:
            break
        if b == a:
            cnt += 1
    print(f"{s1[i]}:-   {cnt} times")
# =================================================================
# 18.//Count the frequency of characters in a given String.
# =================================================================
s = "I am good and having good day"
s1 = s.split(" ")
for i in range(len(s1)):
    cnt = 0
for j in range(len(s1)):
    a = s1[i]
    b = s1[j]
    if j < i and b == a:
        break

    if b == a:
        cnt += 1

if j == len(s1) - 1:
    print(s1[i] + " is present " + str(cnt) + " numberof times")
# =================================================================
# 19.Count the frequency of characters in a given String.
# ==================================================================
s = "I am good and having good day"
s = s.replace(" ", "")
s1 = list(s)
for i in range(len(s1)):
    cnt = 0
for j in range(len(s1)):
    a = s1[i]
    b = s1[j]
if j < i and b == a:

break

if b == a:

cnt += 1
if j == len(s1) - 1
    print(s1[i] + " is present " + str(cnt) + " numberof times")
# =============================================================
# 20./Print the numbers in array in an ascending order in java.
# =============================================================
n = "Enter the no of elements you want in array "
arr = []
for i in range(n):
    element = "Enter the element No - {}:".format(n)
arr.append(element)

for i in range(n):
    for j in range(i + 1, n):
        if (arr[i] > arr[j])
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
for i in range(n):
    print(arr[i], end=" ")
# ============================================================
# 21./Print the numbers in array in a Descending order in java.
# ============================================================
n = "Enter the no of elements you want in array : "
arr = []
for i in range(n):
    element = "Enter the element No - {}:".format(n)
arr.append(element)

for i in range(n):
    for j in range(i + 1, n)
        if (arr[i] < arr[j])
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
for i in range(n):
    print(arr[i], end=" ")
# ==============================================================
# 22.//Print the prime numbers counts available between 1 to 100.
# ==============================================================

count = 0
for i in range(2, 101):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
        print(count)

# ===================================================================
# 23.//Biggest Number.
# ===================================================================
a = 50, b = 80, c = 20
if a > b and a > c:
    print(a)
else b > a and b > c:
    print(b)
else:
print(c)

# ==========================================================
# 24.//ThirdMax Number.
# ==========================================================
a = [-12, 45, -23, 64, -100, 24]
a.sort(reverse=True)
if len(a) >= 3:
    print("ThirdMax number is", a[2])
else:
    print("Array doesn't have a third maximum number")
# =============================================================
# 25.//Separate reverse of each word in the string.
# =============================================================
s = "Tejas Borse"
a = s.split(" ")
rev = ""
for word in a:
    temp = word
for j in range(len(temp) - 1, -1, -1):
    ch = temp(j)
    rev += ch
    rev += " "

print(rev)
# ===============================================================
# 26./*Find the duplicate count in an array.
# =================================================================


n = "Enter number of elements you want in the array: "
a = []

print("Enter all the numbers:")
for i in range(n):
    num = ()
    a.append(num)

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            count += 1

print(count)
# ======================================================
# 27./*Find the duplicate count in the string.
# =======================================================

str = "beautiful beach"
print("The string is:", str)
print("Duplicate Characters in the above string are:", end=' ')

char_list = list(str)
duplicates = set()
for i in range(len(char_list)):
    for j in range(i + 1, len(char_list)):
        if char_list[i] == char_list[j]:
            duplicates.add(char_list[i])

print(' '.join(duplicates))
# ==================================================================
# 28.//Count of the palindrome number.
# ==================================================================
c = 0
for i in range(1, 1001):
    a = i
    rev = 0
    while a != 0:
        rev = rev * 10 + (a % 10)
        a = a // 10
    if rev == i
        c += 1
    print(c)
# =====================================================================
# 29.// Count of the palindrome number.
# =====================================================================

c = 0
for i in range(1, 1001):
    a = i
num_of_digits = len(str(i))
sum = 0
while a != 0:
    n = a % 10
sum += n ** num_of_digits
a //= 10
if sum == i:
    c += 1
println(c)
# =====================================================
# 30.//Count frequency of words using Hashmap.
# =====================================================
cars = ["Volvo", "BMW", "Ford", "Mazda", "BMW", "Ford"]
print(cars)
car_dict = {}
for car in cars:
    if car in car_dict:
        car_dict[car] += 1
    else:
        car_dict[car] = 1
print(car_dict)
for car, count in car_dict.items():
    print(f"{car} occurs {count} times")
# ==============================================================
# 31./*Prime no or not.
# ==============================================================
tot = 0
for i in range(1, 101):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end=' ')
        tot += 1
print("\n", tot)
# ================================================================
# 32./*Fibonacci series upto 55.
# ================================================================
n = int(input("Enter the last no: "))
a, b = 0, 1
print(a, b, end=" ")
for i in range(98):  # Adjust the loop range as needed
    c = a + b
    print(c, end=" ")
    if c == n:
        break
    a, b = b, c
# ================================================================
# 33./*Fibonacci series with first 10 .
# ================================================================
a = 0
b = 1
n = 2

print(a, b, end=" ")

for i in range(99):
    c = a + b
    print(c, end=" ")
    n += 1
    if n == 10:
        break
    a, b = b, c


# ===================================================================
# 34./*Reverse a no without using variable.
# ===================================================================
def add_numbers(a, b):
    result = a + b
    return result


num1 = 5
num2 = 3
sum_result = add_numbers(num1, num2)
print("The sum is:", sum_result)
# ===================================================================
# 35./*Reverse two no's without using variable.
# ===================================================================
a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a, b)
# ====================================================================
# 36./*Write a Program to copy all elements of one array into another.
# ====================================================================
arr1 = [12, 10, 15, 8, 4]
arr2 = [0] * len(arr1)
for i in range(len(arr1)):
    arr2[i] = arr1[i]
for a in arr1:
    print(a, end=" ")
print("")
for i in range(len(arr2)):
    print(arr2[i], end=" ")
print("")
# =================================================================
# 37./*write a Program to print the duplicate elements of an array.
# =================================================================
arr = [0] * 8
for i in range(8):
    print("Enter the number:")
    arr[i] = int(input())
print("Duplicate elements are:")
for i in range(8):
    for j in range(i + 1, 8):
        if arr[i] == arr[j]:
            print(arr[j])
# ==================================================================
# 38./*write a program to find out smallest element in an array.
# ==================================================================
arr = [25, 11, 7, 75, 56]
min_val = arr[0]

for num in arr:
    if num < min_val:
        min_val = num

print("Smallest element present in the given array:", min_val)
# ===================================================================
# 39./*write a program to find out biggest element in an array.
# ===================================================================
arr = [25, 11, 7, 75, 56]
max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print("Biggest element present in the given array:", max_val)
# =====================================================================
# 40./*write a program to print the sum of all the items of the array.
# =====================================================================
arr = []

for i in range(5):
    num = int(input("Enter the number: "))
    arr.append(num)

sum_of_numbers = sum(arr)

print("Sum of numbers in the given list is:", sum_of_numbers)
# ========================================================================
# 41./*write a Program to count the total number of characters in a string.
# ========================================================================
str_value = "Tejas Prashant Borse"
cnt = 0

for char in str_value:
    if char != ' ':
        cnt += 1

print(cnt)
# =========================================================================
# 42./*write a Program to count the total number of vowels in a string.
# =========================================================================
str_value = "Tejas Prashant Borse"
cnt = 0

for char in str_value:
    if char.lower() in 'aeiou':
        cnt += 1

print("Number of vowels is", cnt)
# ==========================================================================
# 43./*write a Program to determine whether a given string is palindrome.
# ==========================================================================
str_value = input("Enter the string: ")
rev = str_value[::-1]

if str_value.lower() == rev.lower():
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")
# ============================================================================
# 44./*write a program to Reverse the string.
# ============================================================================
str_value = input("Enter the string: ")
rev = ""

for i in range(len(str_value) - 1, -1, -1):
    rev += str_value[i]

print("Reversed String is", rev)
# ==============================================================================
# 45./*"I want to be an software enginner and I am Nitin "output.
# ==============================================================================
in_str = "I am Nitin and I want to be an software engineer"
words = in_str.split()
output_words = words[1:] + words[:1]
output_str = " ".join(output_words)
print(output_str)
#=========================================================================
#46.
#=========================================================================

