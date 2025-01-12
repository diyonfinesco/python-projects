import os


def print_file_content(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            print(file.read())

def write_content_to_file(file_name:str, content: list):
    with open(file_name, 'w') as file:
        file.write('\n'.join(content))
        print(f"{file_name} saved.")

def main():
    file_name = input("Enter the filename to open or create: ")

    try:
        print_file_content(file_name)

        print("Enter your text (type SAVE on a new line to save and exit)")
        
        content = []
        
        while True:            
            line = input()

            if line.lower() == "save": 
                break

            content.append(line)
        
        write_content_to_file(file_name, content)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()