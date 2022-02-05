read_txt = open("captions_text.vtt", 'r')   # Reading the input file
# write_txt = open("captions_text.vtt", 'w')
new_txt = ""    # Assigning a str variable in which the formatted text will be stored
pos = 0 # positioning Variable
for i in read_txt.read():   # for loop which check
    # print(i)
    if i.isdigit() or i == ':' or i == '-' or i == '>':
        continue
    elif i.isalpha() or i == ' ' or i == "'":
        # print("yes")
        new_txt = new_txt + i
    pos = pos + 1

with open('new_txt.txt', 'w') as f:
    f.write(new_txt)

read_txt = open('new_txt.txt', 'r')
str_text = str(read_txt.read())
split_str = str_text.split(' ')
pos = 0
str_text = ''
for i in split_str:
    if len(i) == 4:
        st = i[0] + "***"
        split_str[pos] = st
    str_text = str_text + " " + split_str[pos]
    pos = pos + 1
with open('new_txt.txt', 'w') as f:
    f.write(str_text)
