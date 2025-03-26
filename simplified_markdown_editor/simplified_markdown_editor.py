import sys

def format_plain(text):
    return text

def format_bold(text):
    return f"**{text}**"

def format_italic(text):
    return f"*{text}*"

def format_inline_code(text):
    return f"`{text}`"

def format_header():
    level = int(input("Level: > "))
    if 1 <= level <= 6:
        text = input("Text: > ")
        return f"{'#' * level} {text}\n"
    else:
        print("The level should be within the range of 1 to 6.")
        return ""

def format_link():
        label = input("Label: > ")
        url = input("URL: > ")
        return f"[{label}]({url})"

def format_list(ordered=True):
    num_rows = int(input("Number of rows: > "))
    if num_rows <= 0:
        print("The number of rows should be greater than zero")
        return ""

    result = []
    for i in range(1, num_rows + 1):
        row_text = input(f"Row #{i}: > ")
        prefix = f"{i}. " if ordered else "* "
        result.append(prefix + row_text)

    return "\n".join(result) + "\n"



def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def main():
    while True:
        command = input("Choose a formatter: > ")

        if command == "!help":
            print_help()
        elif command == "!done":
            break
        else:
            print("Unknown formatting type or command")



if __name__ == "__main__":
    main()