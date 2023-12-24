# opening the file in read mode 
my_file = open("/home/yoshl/Documents/Scripting/wordlist.lst", "r") 
data = my_file.readlines()

# iterating over lines
for line in data:
    # Remove leading and trailing whitespaces from each line
    line = line.strip()
    
    # Execute the lin

    # Print the result or take any other actions as needed
    print(f"Command: {line}")