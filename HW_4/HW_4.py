# Декоратор для обробки помилок.
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter name and phone number please"
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "Contact not found."

    return inner


# Парсинг вводу користувача
def parse_input(user_input):

    # Перевірка на порожній ввід
    if not user_input.strip(): 
        return ("",)
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


# додавання нового контакту
@input_error
def add_contact(args, contacts):

    name, phone = args
    name = name.lower()
    contacts[name] = phone

    return "Contact added."


# зміна номера телефону існуючого контакту
@input_error
def change_contact(args, contacts):

    name, phone = args
    name = name.lower()

    if name not in contacts:
        raise KeyError
    
    contacts[name] = phone
    
    return "Contact updated."


# відображення номера телефону контакту 
@input_error
def show_phone(args, contacts):
    
    name = args[0]
    name = name.lower()

    phone = contacts[name]
    return phone


# відображення всіх контактів
@input_error
def show_all(contacts):

    if contacts:
        result = []

        for name, phone in contacts.items():
            name = name.capitalize()
            result.append(f"{name}: {phone}")

        return "\n".join(result)
    
    else:
        return "No contacts found."
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)   

        if not command:
            print("Please enter a command.")
            continue 

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command in ["hello", "hi", "hey"]:
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()