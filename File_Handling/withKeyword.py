#Dosyayı her sefer kapama zahmetinden kurtarır

#Dosya aç, oku, kapat
with open('File_Handling/example1.txt', "r") as file:
    line1 = file.readline() #readline cursoru bir sonraki satıra götürür ve okuma işlemi oradan devam eder
    line2 = file.readline()

with open('File_Handling/example1.txt', "r") as file:
    lines = file.readlines() #readlines tüm satırları okur ve bir listeye atar
    
print(line1)
print(line2)
print(lines)
for k in lines:
    print(k.strip())