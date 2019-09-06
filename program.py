def main():
    print_header()
    process_input()


def print_header():
    print("-----------------------------")
    print("      Remove Vowels")
    print("      by JasonLABS")
    print("      Version 0.1")
    print("-----------------------------")
    print()


def remove_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    # Count the number of characters in the original string.
    chars_length = str(len(string))
    
    # Display original string to give a comparison later.
    pre_process = string
    
    # Reset number of vowels removed.
    count_removed_vowels = 0

    for chars in string:
        if chars.lower() in vowels:
            string = string.replace(chars, "")
            count_removed_vowels += 1
    
    # Display string without vowels.
    post_process = string
    
    # Count the length of the string after is has been processed.
    # Also change into string to print 
    no_vowels_length = str(len(string))
    
    # Turn into string to print
    count_removed_vowels = str(count_removed_vowels)
    
    no_vowels_dict = {"chars" : chars_length, "no_vowel_length" : no_vowels_length, "count_removed_vowels" : count_removed_vowels,"pre_process" : pre_process,"post_process" : post_process}

    return no_vowels_dict


def process_input():
    entry = input("Enter your sentence. \n")
    remove_vowels(entry)

    entry_without_vowels = remove_vowels(entry)

    entry_len = entry_without_vowels["chars"]
    entry_len_no_vowels = entry_without_vowels["no_vowel_length"]
    removed_vowels_count = entry_without_vowels["count_removed_vowels"]
    pre_process = entry_without_vowels["pre_process"] # Not needed in this example. Kept incase I want to expand functionality.
    post_process =  entry_without_vowels["post_process"]

    print("\nSTATS:")
    print("------")
    print("- The number of characters before removing vowels = " + entry_len + "\n")
    print("- The number of characters after removing vowels = " + entry_len_no_vowels + "\n")
    print("- The number of characters removed is = " + removed_vowels_count + "\n")

    print("---------------------------------------\n")
    print("Here is your sentence without vowels:\n" + post_process + "\n")


if __name__ == "__main__":
    main()
