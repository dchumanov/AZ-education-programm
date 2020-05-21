def cesar(sentence, k):
    cipher=""
    for i in range(len(sentence)):
        cipher += chr(ord(sentence[i])+k)
    return cipher

k = int(input("Input k value: "))

decision = input("You want: 1. Encrypt a phrase; 2. Encrypt a file? (1/2): ")
if decision == "1":
    while True:
        phrase = input("Type your sentence, ENOUGH will terminate this programm: ")
        if phrase == "ENOUGH":
            break
        print(cesar(phrase,k))
        input()
if decision == "2":
    filename = input("Input the path to the file: ")
    f = open(filename, "r+")
    data = f.read()
    f.seek(0)
    f.write(cesar(data,k))
    f.close()



