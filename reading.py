f = open('another_text.txt', 'w')
# file_data = f.read()
# f.write('We created and wrote to this file')

f.close()

# print(file_data)

# creating this with block will automatically close the file after you exit the block
with open('sample_text.txt', 'r') as f:
    file_data = f.read()
print(file_data)

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

# reading each individual line and appending it to a list
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
