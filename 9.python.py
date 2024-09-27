import re

def find_file_name(input1, input2):
    if input2 == 0:
        return -1
    maxversion = -1
    pattern = r"File_(\d+)"
    for file in input1:
        match = re.match(pattern, file.strip())
        if match:
            version = int(match.group(1))
            maxversion = max(maxversion, version)
        return maxversion


input1 = input().split()
input2 = int(input())


result = find_file_name(input1, input2)
print(result)