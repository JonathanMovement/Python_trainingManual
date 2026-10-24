**Functions** let you wrap up code into reusable pieces.

For example, instead of writing the same logic multiple times, you can define it once and just call it.



def greet(name):

&nbsp;   print("Hello,", name)



greet("Oleg")

greet("Echo")



Output:



Hello, Oleg

Hello, Echo



**What is return?**



When you **call a function**, it can either do something immediately (like print) or it can give something back that you can use later. That “give something back” is what return does.

-------------------------------------------------------------------------------------------------------------------------------------

Example with print:



def add(a, b):

&nbsp;   print(a + b)



result = add(3, 4)

print("Result is:", result)



Output:



7

Result is: None

-------------------------------------------------------------------------------------------------------------------------------------

Example with return:



def add(a, b):

&nbsp;   return a + b



result = add(3, 4)

print("Result is:", result)



Output:



Result is: 7

-------------------------------------------------------------------------------------------------------------------------------------