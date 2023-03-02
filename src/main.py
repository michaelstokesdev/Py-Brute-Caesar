import sys

def encode(shiftVal: int, string: list) -> list:
    """Takes a list of words and performs rot ciphering with a given shift value"""
    newString = []
    for i in string:
        newWord = ""
        for x in i:
            xOrd = ord(x)
            newChar = xOrd + shiftVal % 26
            if xOrd in range(97,123) and newChar > 122:
                newChar -= 26
            if xOrd in range(65,91) and newChar > 90:
                newChar -=26
            newWord += chr(newChar)
        newString.append(newWord)
    return newString

def testShift(shiftVal: int, string: list, words: list) -> list:
    """
    Takes a ciphertext string, wordlist, and shift value and returns the
    likelihood of being a correct decipher along with the shifted text
    """
    newString = encode(shiftVal, string)
    numOfMatches = 0

    for i in newString:
        if i in words:
            numOfMatches += 1

    return [numOfMatches/len(newString)*100, newString]

def main():
    #initialise variables 
    vals = dict()
    text = sys.argv[1].split()
    highestVal = 0
    bestMatch = 0

    #load wordlist into memory
    with open("words.txt","r") as wordFile:
        words = wordFile.read().splitlines()
    words = [x.lower() for x in words]

    #run shift tests
    for i in range(0,27):
        vals[i] = testShift(i, text, words)
        if vals[i][0] > highestVal:
            bestMatch = i
            highestVal = vals[i][0]

    #print results and exit
    print("Confidence:", str(highestVal)+"%","Shift value:", bestMatch)
    print("Deciphered text:"," ".join(vals[bestMatch][1]))
    return


if __name__ == "__main__":
    main()