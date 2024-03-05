import language_tool_python

def grammar_check(text):
    tool = language_tool_python.LanguageTool('en-US')

    matches = tool.check(text)
    return matches

def print_errors(matches):
    if not matches:
        print("No grammar errors found.")
    else:
        print("Grammar errors found:")
        for match in matches:
            print(f"Error at line {match['line']}, column {match['column']}: {match['message']}")

if __name__ == '__main__':
    text_to_check = input("Enter the text to check for grammar errors:\n")
    
    errors = grammar_check(text_to_check)
    print_errors(errors)
