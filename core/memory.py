chat_history = []

def add_message(role, content):

    chat_history.append(
        {
            "role": role,
            "content": content
        }
    )


def get_history():

    history = ""

    for msg in chat_history:

        history += f"{msg['role']} : {msg['content']}\n"

    return history