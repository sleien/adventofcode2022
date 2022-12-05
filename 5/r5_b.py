# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        #lines = [line.strip() for line in lines]
        
        stacks = []
        stacksf = []
        stacksb = []
        instruction = []
        emptyLineSeen = False
        #lines until empty line are stacks after that are instructions
        for line in lines:
                if line.strip() == '':
                    emptyLineSeen = True
                elif emptyLineSeen:
                    instruction.append(line.strip())
                else:
                    stacks.append(line)
        for stack in stacks:
            stacksf.append([*stack.replace('    ', '-').strip().replace('[', '').replace(']', '').replace(' ','')])
        stacksf.pop()
        for i in range(len(stacksf)):
            for j in range(len(stacksf[0])):
                if len(stacksb) <= j:
                    stacksb.append([])
                if stacksf[len(stacksf)-i-1][j] != '-':
                    stacksb[j].append(stacksf[len(stacksf)-i-1][j])
        for inst in instruction:
            # get all numbers from inst into a list
            numbers = [int(s) for s in inst.split() if s.isdigit()]
            crate = stacksb[numbers[1]-1][-numbers[0]:]
            stacksb[numbers[2]-1].extend(crate)
            for i in range(numbers[0]):
                stacksb[numbers[1]-1].pop()
        for i in range(len(stacksb)):
            #print last element of stacksb
            print(stacksb[i][len(stacksb[i])-1], end='')
        # loop through lines
        

if __name__ == '__main__':
    main()
