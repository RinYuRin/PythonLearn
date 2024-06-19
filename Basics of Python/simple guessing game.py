guessed_word = "anime"
guess = ""
guess_limit = 3
guess_count = 0
out_of_guess = False


while guess != guessed_word and not(out_of_guess):
	if guess_count < guess_limit:
			guess = input("enter you guess: ")
			
			guess_count += 1
	else:
		out_of_guess = True


if out_of_guess:
	print("Too bad (*_*)! Better luck next time!")

else:
	print("Congratulations! You Won!")