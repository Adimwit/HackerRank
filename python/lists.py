
def main():

    numLines = int(input())
    arr = []

    for i in range(numLines):
        command = input()
        command = command.split()

        if command[0] == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == "append":
            arr.append(int(command[1]))
        elif command[0] == "remove":
            arr.remove(int(command[1]))
        elif command[0] == "pop":
            arr.pop()
        elif command[0] == "index":
            arr.index(int(command[1]))
        elif command[0] == "count":
            arr.count(int(command[1]))
        elif command[0] == "sort":
            arr.sort()
        elif command[0] == "reverse":
            arr.reverse()
        elif command[0] == "print":
            print (arr)


    return None

if __name__ == "__main__":
    main()
