def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def format_plain(text):
    return text

def format_bold(text):
    return f"**{text}**"

def format_italic(text):
    return f"*{text}*"

def format_inline_code(text):
    return f"`{text}`"

def format_header():
    try:
        level = int(input("Level: > "))
        if 1 <= level <= 6:
            text = input("Text: > ")
            return f"{'#' * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6.")
            return ""
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return ""

def format_link():
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"

def format_list(ordered=True):
    try:
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
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return ""

def main():
    result = []

    while True:
        command = input("Choose a formatter: > ")

        if command == "!help":
            print_help()
        elif command == "!done":
            with open("output.md", "w") as file:
                file.write("\n".join(result))
            print("Markdown saved to output.md")
            break
        elif command == "plain":
            text = input("Text: > ")
            result.append(format_plain(text))
        elif command == "bold":
            text = input("Text: > ")
            result.append(format_bold(text))
        elif command == "italic":
            text = input("Text: > ")
            result.append(format_italic(text))
        elif command == "inline-code":
            text = input("Text: > ")
            result.append(format_inline_code(text))
        elif command == "header":
            header_text = format_header()
            if header_text:
                result.append(header_text)
        elif command == "link":
            result.append(format_link())
        elif command == "ordered-list":
            list_text = format_list(ordered=True)
            if list_text:
                result.append(list_text)
        elif command == "unordered-list":
            list_text = format_list(ordered=False)
            if list_text:
                result.append(list_text)
        elif command == "new-line":
            result.append("\n")
        else:
            print("Unknown formatting type or command")

        print("\n".join(result))

if __name__ == "__main__":
    main()





