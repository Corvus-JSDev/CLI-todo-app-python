todo_list = []

while True:
	user_command = input("Write a command (add | show | quit): ").lower()

	match user_command:
		case "add":
			todo = input("Enter a todo: ").title()
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












