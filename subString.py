def count_substring(string, substring):
    count = 0
    start = 0

    while start < len(string):
        index = string.find(substring, start)
        print(index)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break

    return count

# Get user input
input_string = input("Enter the main string: ")
input_substring = input("Enter the substring: ")

# Count and print the occurrences
occurrences = count_substring(input_string, input_substring)
print(f"The substring '{input_substring}' occurs {occurrences} times in the given string.")
