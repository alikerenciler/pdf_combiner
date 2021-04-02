from PyPDF2 import PdfFileMerger
import os 

print("be sure that your pdf and this script are same folder")

number = int(input("how many folder do you have for combine?: "))
file_list =[]

while number>0 :
    number-=1
    file = input("file name: ")
    file = file.replace(".pdf","")
    file = file+".pdf"
    file_list.append(file)

output = PdfFileMerger()

for i in file_list:
    output.append(i)

file_name = input("merged file name: ")
file_name = file_name.replace(".pdf","")
file_name= file_name +".pdf"

output.write(file_name)




