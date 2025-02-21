#Append ile write farkı biri override ederken diğeri hazırda olan dosyayı bozmadan ekleme yapar

file = open('File_Handling/example1.txt', "a") 

content = "\nThis is fourth line"
file.write(content)

file.close()