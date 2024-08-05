todo_list = []

while True:
	user_command = input("Write a command (add | show | quit): ").lower()

	match user_command:
		case "add":
			# .title() will capitalize the first letter of each word.
			# .strip() will remove any trailing or leading spaces
			todo = input("Enter a todo: ").title().strip()
			todo_list.append(todo)

		case "show" :
			for item in todo_list:
				print(item, end=", ")
			print(" ")

		case "quit":
			break

		case _:
			print(f'"{user_command}" is not a command.')

print("\n\nYou have ended the program... goodbye")












