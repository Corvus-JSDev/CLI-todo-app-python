todo_list = []

while True:
	todo = input("Enter a todo (q to quit): ")

	if todo == "q" or todo == "Q":
		break
	else:
		todo_list.append(todo.title())  # .title() will capitalize the first letter of each word

print(todo_list)













