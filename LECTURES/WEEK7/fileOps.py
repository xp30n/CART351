# rainbowFile = open('files/rainbow.txt', "r")
# out = rainbowFile.read(4)
# # print(out)
# # read all
# outAll = rainbowFile.read()
# # print(outAll)
# rainbowFile.seek(0)
# # out_all_again = rainbowFile.readLine()
# allLines = rainbowFile.readlines()
# print(allLines)

# sampleFile = open("files/sample_text_rev.txt", "w")
# for i in range(3): 
#     a_name = input("Enter the name of the animal: ") 
#     sampleFile.write(a_name) 
#     sampleFile.write("\n") 
# sampleFile.close() 
# # if you don't close it, the file will not have updated properly.
# # to make sure that everything is written properly, make sure to close the file
# print("Data is written into the file.") 

# colorList = [] 
# for i in range(3): 
#     a_name = input("Enter the name of a color: ") 
#     colorList.append(a_name + '\n') 
# sampleFile.writelines(colorList) 
# sampleFile.close() 
# print("Data is written into the file.") 

sampleFile_a = open("files/sample_text.txt", "a")
nameList = [] 
for i in range(3): 
    a_name = input("Enter the name of someone in your class: ") 
    nameList.append(a_name + '\n') 
sampleFile_a.writelines(nameList) 
sampleFile_a.close() 
print("Data is written into the file.") 