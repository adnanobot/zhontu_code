
def display_info(name, age):
    print("Name: ", name)
    print("Age: ", age)

def take_user_info():
    print("Please enter the following information: ")
    name_1 = input("Name: ")
    age_1 = input("Age: ")

    name_2 = input("Name: ")
    age_2 = input("Age: ")

    search_query = input("\n\nPlease enter the search q: ")
    print("\nSearch result: \n")

    if search_query == name_1:
        display_info(name_1, age_1)
    elif search_query == name_2:
        display_info(name_2, age_2)


def print_stars(row, col):
    for i in range(row):
        string = ""
        for j in range(i+1):
            string = string + str(j)
            # print(j)
        print(string)


        # print(string)


def test():
    x = 4 # at this point, the value of the variable x = 1
    y = 1 # now, x = 1, y = 2

    x = x + y
    # now, x = 4 + 1
    # or x = 5
    # and y remains same, no change
    # so at this point print the value, then you will see that x = 5, y = 1
    print("x = ", x)
    print("y = ", y)

    x = x - y
    x = x - y
    x = x - y
    x = x - y
    x = x - y

    # So, now what will be the output of the following print statements?
    print("x = ", x)
    print("y = ", y)


def test_for_loop():
    # now, let's do it another way
    x = 5
    y = 1

    for i in range(5):
        x = x -y

    print("x = ", x, "y = ", y) # what do you think will be the output?
    # also can you find out that how many times the loop has run? ha ha, the answer is 5


def test_while_loop():
    x = 5
    y = 1

    while(x > 0):
        x = x - y

    print("x = ", x, "y = ", y)  # what do you think will be the output?

def area_finder():
    pass



if __name__ == '__main__':
    # take_user_info()

    # print_stars(3, 3)

    test()

    test_for_loop()

    test_while_loop()

    area_finder()

    

