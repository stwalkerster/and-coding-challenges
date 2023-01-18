import json


def process_message(input_message):
    i = 0
    clipboard = ""
    output_message = ""

    i = 0
    max_i = len(input_message)
    while i < max_i:
        if input_message[i:i+8] == "[CTRL+C]":
            clipboard = output_message
            i += 7
        elif input_message[i:i+8] == "[CTRL+X]":
            clipboard = output_message
            output_message = ""
            i += 7
        elif input_message[i:i+8] == "[CTRL+V]":
            output_message += clipboard
            i += 7
        else:
            output_message += input_message[i]

        i += 1

    return output_message


if __name__ == '__main__':
    input_data = json.load(open('challenge1.json', 'r'))

    for t in input_data:
        print(process_message(t))
