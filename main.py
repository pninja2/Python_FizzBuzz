# Print out numbers from 1 to 100 (including 100).
for i in range(1,101):
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)    
    # Instead of printing multiples of both 3 and 5, print "FizzBuzz".
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    # But, instead of printing multiples of 3, print "Fizz"
    elif i % 3 == 0:
        print("Fizz")
    # Instead of printing multiples of 5, print "Buzz"
    elif i % 5 == 0:
        print("Buzz")





