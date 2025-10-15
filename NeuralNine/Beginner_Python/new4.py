
## Reading a File

#with open('file.txt','r') as f:
#   content = f.read()

#file = open('file.txt', 'r')

#content = file.read()

#ile.close()

#print(content)

## Writinf in a File

#file = open('file.txt','w')
#file.write("Hello Everyone!, Welcome to my Program")
#file.close()


## Appending a File

try:
    file = open('file.txt','a')
    file.write("\nHello World")
except:
    print("Couldn't append the file")
finally:
    file.close()
