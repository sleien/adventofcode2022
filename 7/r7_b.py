import re
# get all input from input.txt

def main():
    # open file
    with open('input.txt', 'r') as f:
        # read all lines
        lines = f.readlines()
        # remove new line characters
        lines = [line.strip() for line in lines]
        dir_path = "/"
        system = []
        for line in lines:
            if line.startswith("$ cd"):
                # get the directory to change to
                dir = line.split(" ")[2]
                # if dir is a relative path
                if dir.startswith(".."):
                    # get the number of directories to go back
                    dir_path = dir_path[:dir_path.rfind("/")]
                    if dir_path == "":
                        dir_path = "/"
                # if dir is a relative path
                elif dir.startswith("/"):
                    # set the system to the root directory
                    dir_path = ""
                # if dir is a relative path
                else:
                    # add the directory to the system
                    if not dir_path.endswith("/"):
                        dir_path += "/"
                    dir_path += dir
            elif line[0].isdigit():
                # get the file name
                file = line.split(" ")
                # add the file to the system
                system.append(dir_path  + "/" + file[1] + "_" + file[0])

        dirs = []
        for line in system:
            # get all files in the same directory and remove them from the system
            # get path till last /
            path = line[:line.rfind("/")]
            files = [file for file in system if file.startswith(path) and file.count("/") == line.count("/")]
            system = [file for file in system if not file.startswith(path) or file.count("/") != line.count("/")]
            if files:
                dirs.append(files)

        dir = {}
        for files in dirs:
            sum = 0
            for line in files:
                # get the file size
                size = int(line.split("_")[1])
                # add the file size to the sum
                sum += size
            # add the sum to the directory
            path = files[0][:line.rfind("/")]
            dir[path] = sum
            for i in range(path.count("/")):
                path = path[:path.rfind("/")]
                if path in dir:
                    dir[path] += sum
                else:
                    dir[path] = sum    

        space = 70000000
        space_needed = 30000000
        # sum all in dir smaller than 100000
        sum = 0
        for key, value in dir.items():
            sum += value
        space_used = dir['']
        space_free = space - space_used
        space_del = space_needed - space_free
        
        dir_del = {"diff": space, "name": "", "size": 0}
        for key, value in dir.items():
            diff = value - space_del
            if diff > 0:
                if diff < dir_del['diff']:
                    dir_del['diff'] = diff
                    dir_del['name'] = key
                    dir_del['size'] = value
        print(dir_del)
      

if __name__ == '__main__':
    main()
