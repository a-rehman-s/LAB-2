with open("D:\\file.txt", "r") as file:
    content = file.read().split()
    longest_word = max(content, key=len)
    print("Longest Word:", longest_word)
