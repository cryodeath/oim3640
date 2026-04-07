# Read entire file
with open('data/s20.txt') as f:
    text = f.read() # returns the whole file as a single string
    #text = f.readline() # returns a single line as a string
    #text = f.readlines()  # returns a list of lines as strings
    print(text)

# Read line by line (best for large files)
# with open('data/s20.txt') as f:
#    for line in f:
#        print(line.strip())  # strip() removes \n

# Write to file ('w' = overwrite, 'a' = append)
with open('output/s20.txt', 'w') as f:
    f.write('Hello, World!\n')