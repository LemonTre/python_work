file_path = "G:\python_work\Chap10\guest_book.txt"

while True:
	message = input("\nEnter your name(choose 'q' to quit):")
	if message == 'q':
		break
	else:
		print("Hello, " + message.title())
		with open(file_path, 'a') as file:
			message += " had a look!"
			file.write(message + "\n")
