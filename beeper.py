import winsound
from math import sin, radians
from time import sleep

frequency = 500
duration = 100

# winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

def wave():
	for a in range(-180, 180, 10):
		s = round( float( "{:.02f}".format( sin( radians(a) ) * 100 ) ) ) // 2
		print(f"{a} degrees:", end="\t")
		print( (s + 50) * " ", end="*\n" )
		sleep(0.01)

# while True:
#     wave()

# print a box
# take name and information
name_list = []
age = []
vaccine_status = []

while True:
	while True:
		name = input("Please enter you name:\t")
		if name != "":
			name_list.append(name)
			break
		else:
			print("Please enter a valid name.")

	# detect invalid input
	age.append(input("Please enter you age:\t"))

	while True:
		answer = input("Vaccinated? [y / n]:\t")
		if answer == 'y' or answer == 'n':
			vaccine_status.append(answer)
			break

		print("please enter 'y' or 'n'")

	exit = input("Enter <n> to exit, <y> to continue: \t")

	if exit == "n":
		break



# mistake: keep answer outside loop
# handle blank input
# handle invalid input - name, age
