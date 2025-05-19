def sort_1(word_list):
    reversed_words = [word[::-1] for word in word_list]
    reversed_words.sort()
    sorted_list = [word[::-1] for word in reversed_words]
    return sorted_list

def sort_2(word_list):
    rearranged = [word[-2:] + word[:-2] for word in word_list]
    rearranged.sort()
    sorted_list = []
    for word in rearranged:
        rearranged_back = word[2:] + word[:2]
        sorted_list.append(rearranged_back)
    return sorted_list

print("Input and special sorting of a word list:")
print("-" * 50)

word_list = []

while True:
    word = input("New word list entry: ").strip()
    if word == "":
        break
    word_list.append(word.upper())

print("\nEnd of list input!")

print("\nUnsorted word list:")
print(word_list)

word_list_sort_1 = sort_1(word_list)
print("\nWord list - Sorting 1:")
print(word_list_sort_1)

word_list_sort_2 = sort_2(word_list)
print("\nWord list - Sorting 2:")
print(word_list_sort_2)

print("\nThe program was executed by Lennart Novak.")