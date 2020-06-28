def add_tag(tag, body):
    tagged = f"<{tag}>{body}</{tag}>"
    return tagged


word = input("Enter a word to add tags: ")
tag = input("Enter the tag to add: ")
print(add_tag(tag, word))
