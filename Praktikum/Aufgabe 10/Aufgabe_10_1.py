dict_de_en = {}
dict_de_fr = {}

while True:
    print("\nDictionaries")
    print("========================")
    print("[1] Dictionary German–English")
    print("[2] Dictionary German–French")
    print("[3] Query English–French")
    print("[0] Exit program")
    choice = input("Choice: ")

    if choice == "0":
        print("\nDictionary query completed by Lennart Novak.")
        break

    elif choice == "1":
        print("\nDictionary Query:")
        print("========================")
        word = input("Word (German): ").strip()

        if word in dict_de_en:
            print(f"The English word for {word} is: {dict_de_en[word]}")
        else:
            print("No dictionary entry found!")
            add_entry = input("Would you like to add the word (Y/N)? ").strip().lower()
            if add_entry == "y":
                translation = input(f"The English word for {word} is: ").strip()
                dict_de_en[word] = translation
                print(f"Entry added: {word} -> {translation}")

    elif choice == "2":
        print("\nDictionary Query:")
        print("========================")
        word = input("Word (German): ").strip()

        if word in dict_de_fr:
            print(f"The French word for {word} is: {dict_de_fr[word]}")
        else:
            print("No dictionary entry found!")
            add_entry = input("Would you like to add the word (Y/N)? ").strip().lower()
            if add_entry == "y":
                translation = input(f"The French word for {word} is: ").strip()
                dict_de_fr[word] = translation
                print(f"Entry added: {word} -> {translation}")

    elif choice == "3":
        print("\nDictionary Query:")
        print("========================")
        word_en = input("Word (English): ").strip()

        word_de = None
        for de, en in dict_de_en.items():
            if en == word_en:
                word_de = de
                break

        if not word_de:
            print(f"The German word for {word_en} is not found in the English dictionary!")
            add_entry = input("Would you like to add the entry (Y/N)? ").strip().lower()
            if add_entry == "y":
                word_de = input(f"The German word for {word_en} is: ").strip()
                dict_de_en[word_de] = word_en
                print(f"Entry added: {word_de} -> {word_en}")
        else:
            if word_de in dict_de_fr:
                print(f"The French word for {word_de} is: {dict_de_fr[word_de]}")
            else:
                print(f"The French word for {word_de} is not found in the French dictionary!")
                add_entry = input("Would you like to add the entry (Y/N)? ").strip().lower()
                if add_entry == "y":
                    word_fr = input(f"The French word for {word_de} is: ").strip()
                    dict_de_fr[word_de] = word_fr
                    print(f"Entry added: {word_de} -> {word_fr}")
    else:
        print("Invalid choice. Please try again.")
