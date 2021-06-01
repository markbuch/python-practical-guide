#f = open('demo.txt', mode='r')
#f.write('Add this content!\n')
with open('demo.txt', mode='r') as f:

    #file_content = f.read() #Reads the entire file
    #file_content = f.readlines() #Read each line of the file into a list.
    #f.close() # Close file to save changes and release resources

    #for line in file_content:
    #    print(line[:-1])

    # print(file_content)

    line = f.readline() # read one line at a time.
    while line:
        print(line)
        line = f.readline()
    print('Done')

    #f.close() When using with block, file close is not needed.