

def FizzBuzz(collection):

    result = ""
    n_fizz = 0
    n_buzz = 0
    n_fizzbuzz = 0


    for n in collection:

        if (n % 3 == 0) and (n % 5 == 0):
            
            result += "FizzBuzz\n"
            n_fizzbuzz += 1

        elif n % 3 == 0:
            
            result += "Fizz\n"
            n_fizz += 1

        elif n % 5 == 0:

            result += "Buzz\n"
            n_buzz += 1

        else:

            result += "%i\n" % n

    result += "..............................................................\n"
    result += "Resumo\n"
    result += "%i Fizz\n" % n_fizz
    result += "%i Buzz\n" % n_buzz
    result += "%i FizzBuzz\n" % n_fizzbuzz
    result += "..............................................................\n"


    return result

if __name__ == "__main__":
    

    result = FizzBuzz(range(1, 1000))
    print(result)