
import string

def main():

    numStudents = int(input())

    for i in range(numStudents):

        marks = input()
        numMarks = marks.count(' ')
        wordList = marks.split(' ')
        students = {}

        avg = 0
        for j in range(1, numMarks + 1):
            avg += float(wordList[j])

        avg = avg / numMarks
        students[wordList[0]] = avg
    
    name = input()

    print ("%.2f" % students[name])
    
    return None

if __name__ == "__main__":
    main()
