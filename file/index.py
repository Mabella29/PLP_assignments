with open('input.txt', 'r') as file:
    data = file.read()
    
# Modifications
uppercase_text = data.upper()
word_count = len(data.split())

with open('output.txt', 'w') as output_file:
    output_file.write(uppercase_text)
    output_file.write(f"\nNumber of words: {word_count}")

print("File 'output.txt' created successfully")


filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        data = file.read()

    uppercase_text = data.upper()
    word_count = len(data.split())
    
    output_filename = 'output.txt'
    with open(output_filename, 'w') as output_file:
        output_file.write(uppercase_text)
        output_file.write(f"\nNumber of words: {word_count}")

    print(f"File '{output_filename}' created successfully!")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")