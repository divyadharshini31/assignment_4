#to read the content of the text file  
f = open("file.txt", "r")
for i in f:
    print(i.strip())

#to count the number of lines, words, and characters in a text file
file="file.txt"
with open("file.txt","r") as filename:
    read=filename.readlines()
    no_lines=len(read)
    no_word=sum(len(i.split())for i in read )
    no_chara=sum(len(i)for i in read)
print("lines: ",str(no_lines))
print("words: ",str(no_word))
print("characters",str(no_chara))

#copy the contents of one text file into another file.
with open("file.txt","r") as copy:
    c=copy.read()
with open("copy_file.txt","w") as copied:
    copied.write(c)
print("copied !")


#to search for a specific word in a text file and display the line numbers where it appears.
word=input("enter the word to search: ")
with open("file.txt","r") as f:
    read=f.readlines()
linenumber=[]
for i,j in enumerate(read,start=1):
    if word in j:
        linenumber.append(i)
if linenumber:
    print("line number - ", str(linenumber))
else:
    print("not found")