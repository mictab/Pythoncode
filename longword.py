#Find the longest word in a string and return the length, WITHOUT using .split()

def long(sentence):
    alist = []
    length = 0
    for letter in sentence:
        #print(letter)
        
        if letter != " ":
            length += 1

        else:
            alist.append(length)
            length = 0
    alist.append(length)

    return alist
