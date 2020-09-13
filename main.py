def main():
    get = input("enter a plain test: ")
    if get.isdigit() == True:
        main()
    words = 1
    letters = 0
    sentences = 0
    l = len(get)
    for i in range(l):
        if (get[i].isalpha() == True):
            letters += 1
        elif (get[i] == " "):
            words += 1
        elif (get[i] == "." or get[i] == "!" or get[i] == "?"):
            sentences += 1
    newL = letters / (float(words)) * 100
    newS = sentences / (float(words)) * 100
    index = (.0588 * newL) - (.296 * newS) - 15.8
    nIndex = int(round(index))
    if nIndex < 1:
        print("Before Grade 1")
    elif nIndex > 1 and nIndex <= 16:
        print("Grade:", nIndex)
    else:
        print("Grade 16+")


main()