# create a new file
file = open('list_1.txt', 'w')
# write number (1-10) and the user's input, then a new line
for x in range(10):
    file.write( str(x+1) + '. '+ input(str(x+1) + '. ') + '\n')
# close file
file.close()
