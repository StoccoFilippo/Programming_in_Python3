# This program compares the lines of two text files and writes the common lines to a new file.

common_lines = []

# Read lines from first file
with open("c:\\Users\\Filippo\\Desktop\\Python\\Data\\03_list1.txt") as file1:
    lines_file1 = file1.readlines()

# Read lines from second file
with open("c:\\Users\\Filippo\\Desktop\\Python\\Data\\03_list2.txt") as file2:
    lines_file2 = file2.readlines()

index = 1
print("The file {0} contains this list:\n".format(file2))
for line in lines_file2:
    print("{0}: {1}".format(index, line))
    index += 1

index = 1
print("The file {0} contains this list:\n".format(file1))
for line in lines_file1:
    print("{0}: {1}".format(index, line))
    index += 1

start = -1

# Find common lines
while start != -len(lines_file1):
    if lines_file1[start] in lines_file2:
        common_lines.append(lines_file1[start])
    start -= 1

# Write common lines to a new file
with open("c:\\Users\\Filippo\\Desktop\\Python\\Data\\03_list3.txt", "w") as file3:
    for common_line in common_lines:
        file3.write(common_line)
    file3.close()

# Read and print common lines from the new file
with open("c:\\Users\\Filippo\\Desktop\\Python\\Data\\03_list3.txt", "r") as file3:
    common_line = file3.readlines()

index = 1
print("The file {0} has been created and it contains this list:\n".format(file3))
for line in common_line:
    print("{0}: {1}".format(index, line))
    index += 1
