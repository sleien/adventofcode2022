# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        
        marker = 0
        chars = ['','','','','','','','','','','','','','']

        lines = list(lines[0])

        for i in range(len(lines)):
            for j in range(len(chars)-1):
                chars[j] = chars[j+1]
            chars[-1] = lines[i]
            if i >= 13:
                # check if values in char are unique
                if len(set(chars)) == 14:
                    marker = i + 1
                    break
        
        print(marker)

      

if __name__ == '__main__':
    main()
