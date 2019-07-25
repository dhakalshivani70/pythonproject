file1 = open("file.txt","r")
file2 = open("fileone.txt","r")
'''
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
print(file1.readline())
'''
for line in file1:
    print(line)
print(file2.readline())

