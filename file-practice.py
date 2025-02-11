

def save_message():
    message = input("Enter a message: ")
    try:
        with open('messages.txt', 'w') as f:
            f.write(message)
    except FileNotFoundError as e:
        print(e)

def print_message():
    with open('messages.txt', 'r') as f:
        content = f.read()
        print('File contents:', content)

save_message()
print_message()
