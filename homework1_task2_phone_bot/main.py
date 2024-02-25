def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact is added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact is updated"
    else:
        return "Contact is not found"


def show_contact(args, contacts):
    name = args[0]
    if name in contacts.keys():
        return str(contacts[name])
    else:
        return "Contact is not found"


def show_all_contacts(contacts):
    users = ''
    for username, phone in contacts.items():
        users += f"{username} {phone}\n"
    return users


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts), end='')
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
