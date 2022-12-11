# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]

        monkey_lines = []
        monkeys: Monkey = []

        rounds = 20

        for idx, line in enumerate(lines):
            if idx == len(lines) - 1:
                monkey_lines.append(line)
                monkeys.append(Monkey(monkey_lines))
            elif line != '':
                monkey_lines.append(line)
            else:
                # create monkey object
                monkeys.append(Monkey(monkey_lines))
                # clear monkey lines
                monkey_lines = []


        for _ in range(rounds):
            # inspect items
            for monkey in monkeys:
                monkey.inspect()
                items = monkey.get_items().copy()
                for item in items:
                    monkeys[monkey.test(item)].catch(item)

        # print results get the two highest monkeys inspected count
        highest = 0
        second_highest = 0
        for monkey in monkeys:
            if monkey.inspected_count > highest:
                second_highest = highest
                highest = monkey.inspected_count
            elif monkey.inspected_count > second_highest:
                second_highest = monkey.inspected_count
        print(highest * second_highest)
        

# monkey class
class Monkey:
    def __init__(self, lines):
        self.name = lines[0].split(":")[0]
        self.items = [int(x.strip()) for x in lines[1].split(":")[1].split(",")]
        self.operation = lines[2].split(":")[1].strip().split(" ")[3]
        self.operation_num = lines[2].split(":")[1].strip().split(" ")[4]
        self.test_condition = int(lines[3].split("by")[1].strip())
        self.true = int(lines[4].split("monkey")[1].strip())
        self.false = int(lines[5].split("monkey")[1].strip())
        self.inspected_count = 0

    def inspect(self):
        for i in range(len(self.items)):
            if self.operation_num.isdigit():
                operation_num_t = int(self.operation_num)
            else:
                operation_num_t = self.items[i]
            if self.operation == "+":
                self.items[i] += operation_num_t
            elif self.operation == "-":
                self.items[i] -= operation_num_t
            elif self.operation == "*":
                self.items[i] *= operation_num_t
            elif self.operation == "/":
                self.items[i] /= operation_num_t
            self.items[i] = int(self.items[i]/3)
            self.inspected_count += 1
    
    def get_items(self):
        return self.items

    def test(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            # throw error
            raise Exception("Monkey misses this this item")

        if item % self.test_condition == 0:
            return self.true
        return self.false

    def catch(self, item):
        self.items.append(item)

if __name__ == '__main__':
    main()
