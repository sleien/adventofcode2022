# get all input from input.txt
# and sum all the numbers between empty lines

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        # sum lines between empty lines and get highest sum
        
        # init sum
        sum = 0
        # init highest sum
        highest_sum = 0
        snd_highest_sum = 0
        trd_highest_sum = 0
        # loop through lines
        for line in lines:
            # if line is empty
            if line == '':
                # if sum is higher than highest sum
                if sum > highest_sum:
                    # set highest sum to sum
                    trd_highest_sum = snd_highest_sum
                    snd_highest_sum = highest_sum
                    highest_sum = sum
                elif sum > snd_highest_sum:
                    trd_highest_sum = snd_highest_sum
                    snd_highest_sum = sum
                elif sum > trd_highest_sum:
                    trd_highest_sum = sum
                # reset sum
                sum = 0
            # if line is not empty
            else:
                # add line to sum
                sum += int(line)
        # print highest sum
        print(highest_sum)
        print(snd_highest_sum)
        print(trd_highest_sum)
        print(highest_sum + snd_highest_sum + trd_highest_sum)


if __name__ == '__main__':
    main()
