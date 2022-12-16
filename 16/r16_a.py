from collections import deque

# get all input from input.txt


def main():

    queue = deque()
    t_max = 30
    start_valve = "AA"
    ways_dict = {}

    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]

        for i in range(len(lines)):
            lines[i] = lines[i].replace(",", "").replace(";","").split(" ")
            lines[i] = ({"name": lines[i][1], "rate": int(lines[i]
                        [4].split("=")[1]), "ways": lines[i][9:]})
        start = next((obj for obj in lines if obj["name"] == start_valve),None)

        queue.append({"valve": start, "time": 0,
                     "released": 0, "releasing": 0, "opened": [], "last": [start_valve], "way": []})

        while True:
            if queue[0].get("time") >= t_max:
                break
            option = queue.popleft()
            if option.get("valve").get("name") not in option.get("opened") and option.get("valve").get("rate") != 0:
                queue.append({"valve": option.get("valve"), "time": option.get("time") + 1, "released": option.get("released") +
                              option.get("releasing"), "releasing": option.get("releasing") + option.get("valve").get("rate"), "opened": option.get("opened") + [option.get("valve").get("name")], "last": [option.get("last")[-1]], "way": option.get("way").copy()})
            for valve in option.get("valve").get("ways"):
                if valve in option.get("last") and len(option.get("valve").get("ways")) != 1:
                    continue
                valve = next((next_valve for next_valve in lines if next_valve["name"] == valve), None)
                if valve.get("name") in option.get("way"):
                    new_way = option.get("way").copy()
                else:
                    new_way = option.get("way") + [valve.get("name")]
                    new_way.sort()
                key = ''.join(new_way)
                if key in ways_dict and ways_dict[key] >= option.get("released") + option.get("releasing"):
                    continue
                ways_dict[''.join(new_way)] = option.get("released") + option.get("releasing")
                queue.append({"valve": valve, "time": option.get("time") + 1, "released": option.get("released") +
                               option.get("releasing"), "releasing": option.get("releasing"), "opened": option.get("opened"), "last": option.get("last") + [valve.get("name")], "way": new_way})

        highest = 0
        for way in queue:
            if way.get("released") > highest:
                highest = way.get("released")
        print(highest)


if __name__ == '__main__':
    main()
