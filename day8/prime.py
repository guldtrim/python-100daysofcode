def prime_checker(number):
    dividors = [2, 3, 5, 7, 11, 13]
    is_prime = True

    for i in dividors:
        if number % i == 0:
            is_prime = False 
    if is_prime == True:
        print("Primer in the chat boys")
    else:
        print("No primes for you")

n = int(input("Check this number: "))
prime_checker(number=n)



