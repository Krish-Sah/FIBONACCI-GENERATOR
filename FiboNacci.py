def fibo (n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input("Enter A Number Here:"))

if n <= 0:
    print ("Please Enter a Positive Number")

else:
    print ("Fibonacci Series")
    for i in range(n):
        print(fibo(i))
       
              
              