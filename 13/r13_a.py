import json
# get all input from input.txt

def compare(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    elif type(a) == int:
        a = [a]
    elif type(b) == int:
        b = [b]

    for x, y in zip(a,b):
        res = compare(x, y)
        if res:
            return res
    
    return len(a) - len(b)


def main():

    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        lines = [json.loads(line) for line in lines if line != '']

        correct = 0
        incorrect = 0

        for i in range(int(len(lines)/2)):
            res = compare(lines[i*2], lines[i*2+1])
            if res < 0:
                correct += i + 1
            else:
                incorrect += i + 1

        print("Correct: " + str(correct))
        print("Incorrect: " + str(incorrect))
        
if __name__ == '__main__':
    main()
