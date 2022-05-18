# given a list1 = ['hello1.txt','data1.txt','data2.txt']
# process the list - they are file name. try to read the contents of the file
# if those files exists.
# find out totally how many lines you read from all the 3 files.

# lst=['hello2.txt','data3.txt','data4.txt']
# r=0
# for x in lst:
#      with open(x,'r') as file:
#             lines=file.readlines()
#             r+=len(lines)
# print("how many Lines are there in 3 files : ",r)


#  create file only if it does not exists
#  otherwise append text to the file
# keep inputting text till the user types QUIT to stop

# then read the file - in the form of string
# find how many times (say) word success appears in the file
# display the FIRST and the LAST line from the file

import os.path
while True:
    if os.path.exists('D:\may_17\demo1.txt'):
        with open('demo1.txt','a+') as file:
            while True:
                txt=input('enter a text :')
                if txt.upper()=='QUIT':
                    break
                else:
                    file.write(txt+'\n')
            file.seek(0)
            data=file.read()
            break
    else:
        f=open('demo.txt','a')
        f.close()
num=data.count('success')
print('The word SUCCESS apperad in the file :',num)
with open('D:\may_17\demo1.txt','r') as file1:
    fst=file1.readlines()
print('first line of the file is :',fst[0])
print('last line of the file is :',fst[-1])