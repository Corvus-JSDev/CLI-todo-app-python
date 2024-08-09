def remove_first_word(s):
	""" Did you really need a doc string for this? """
	words = s.split()
	if len(words) > 1:
		return ' '.join(words[1:])
	return ''



def get_todo(file_path="user_todo.txt"):
	""" Grab all the todos in the file """
	# Context Managers are important to use because they not only take up less lines of code, but they will also use context to close any opened files if an errors are thrown
	with open(file_path, 'r') as text_file:
		text = text_file.readlines()
	return text



def write_todo(todo, filepath="user_todo.txt"):
	""" Write a new todo(s) to the file """
	with open(filepath, 'w') as text_file:
		text_file.writelines(todo)


# This will make it this code will only run if I specifically run this file
# __name__ will be __main__ if I specifically run this program, or it will be the name of the file if it is imported
if __name__ == "__main__":
	print("hello")
	print(get_todo())