def mix_strings(string1, string2):
    result = ""
    len1, len2 = len(string1), len(string2)
    max_length = max(len1, len2)
    for i in range(2 * max_length):
        if i % 2 == 0:
            result += string2[-((i // 2) % len2 + 1)]
        else:
            result += string1[(i // 2) % len1]
    return result


mix_count = 0
while True:
    string1 = input("Enter the first string (or press Enter to stop): ")
    if string1 == "":
        break
    string2 = input("Enter the second string: ")
    mixed_string = mix_strings(string1, string2)
    print(f"Mixed string from \"{string1}\" and \"{string2}\" is:", mixed_string)
    mix_count += 1
print(f"Number of mix operations: {mix_count} (from Lennart Novak)", )

