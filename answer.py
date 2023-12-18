import math


def answer(number):
    mylist = []
    list_to_check = []
    prime = []

    num = math.sqrt(number)
    num = int(num)
    for i in range(2, num + 1):
        if number % i == 0:
            mylist.append(i)

    for i in mylist:
        new_fact = number / i
        new_fact = int(new_fact)
        list_to_check.append(new_fact)

    main_list = mylist + list_to_check

    for i in main_list:
        count = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i % j) == 0:
                count += 1
                break
        if count == 0:
            prime.append(i)

    prime.sort()
    return prime[-1]

if __name__ == "__main__": 
    print(answer(600851475143))
