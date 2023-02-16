
def places():
    while True:
        name = input("Where do you want to go? ")

        if name == 'America':
            print("Sorry we don't go there.")
            break
        else:
            print("Sure! and then?")

def guess_game():
    while True:
        name = input("Where do you want to go? ")

        if name == 'America':
            print("Sorry we don't go there.")
            break
        else:
            print("Sure! and then?")

if __name__ == '__main__':
    # places()

    # guess_game()
    for i in range(3, 9):
        print(i)