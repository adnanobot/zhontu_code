def adder():
    sum = 0
    while True:
        # if number then take as operand
        # else if operator then select operation
        # else don't accept
        user_input = input()
        operators = ['+', '-', '*', '/']
        if user_input in operators:
            if user_input == '+':
                print("addition")
            elif user_input == '-':
                print("sub")
            elif user_input == '*':
                print("mul")
            elif user_input == '/':
                print("div")
            else:
                print("check if it is number")


        choice = input("continue? [y/n]")
        if choice == 'n':
            break



adder()