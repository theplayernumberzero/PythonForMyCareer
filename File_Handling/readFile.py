#File object
file = open('File_Handling/example1.txt', "r")    #It takes 2 parameter, file path and operation

#read file
content = file.read()   #You can specify memory (bytes)
content2 = file.readline()  #reads first line

#When your work finish you need to close the file
print(content)

file.close()