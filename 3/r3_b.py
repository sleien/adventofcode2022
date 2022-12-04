# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        
        # init sum
        sum = 0
        sim = []
        sim2 = []
        # loop through lines
        for i in range(int(len(lines)/3)):
            line1 = lines[i*3]
            line2 = list(lines[i*3+1])
            line3 = lines[i*3+2]
            for char in line2:
                if char in line1 and not char in sim:
                    sim.append(char)
            for char in sim:
                if char in line3 and not char in sim2:
                    sim2.append(char)
            for char in sim2:
                if(ord(char)>96):
                    sum += ord(char)-96
                else:
                    sum += ord(char)-64+26
            sim = []
            sim2 = []
        print("Sum: " + str(sum))


if __name__ == '__main__':
    main()
