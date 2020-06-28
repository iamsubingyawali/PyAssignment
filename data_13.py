def modify_seq(comma_words):
    separated_list = comma_words.split(",")
    modified_string = ",".join(sorted(set(separated_list)))
    return modified_string


comma_string = input("Enter words separated by comma (NO SPACES): ")
print(modify_seq(comma_string))


