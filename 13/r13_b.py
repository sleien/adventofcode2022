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

        #div_pack needs to be sorted
        div_packs = [
            {
                "idx": 1,
                "value": [[2]]
            },
            {
                "idx": 2,
                "value": [[6]]
            }
        ]

        for line in lines:
            if compare(line, div_packs[0]["value"]) < 0:
                div_packs[0]["idx"] += 1
                div_packs[1]["idx"] += 1
            elif compare(line, div_packs[1]["value"]) < 0:
                div_packs[1]["idx"] += 1
        print(div_packs[0]["idx"] * div_packs[1]["idx"])
        
if __name__ == '__main__':
    main()
