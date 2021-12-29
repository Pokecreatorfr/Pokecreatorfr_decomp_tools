import os
def palette_format(path_to_pal):
    palette = open(path_to_pal , encoding="UTF-8")
    lines = palette.readlines()
    palette_lines = []
    for line in lines:
        palette_lines.append(line)
    pal_txt_list = []
    for i in range(3 , 19):
        pal_txt_list.append(palette_lines[i].split())
    pal_int_list = [['' for a in range(3)] for x in range(16)]
    for i in range(len(pal_txt_list)):
        for x in range(3):
            pal_int_list[i][x] = int(pal_txt_list[i][x])

    for i in range(len(pal_int_list)):
        for x in range(len(pal_int_list[i])):
            if pal_int_list[i][x]%8 != 0 and pal_int_list[i][x] != 0:
                if pal_int_list[i][x] > 248:
                    pal_int_list[i][x] = 248
                elif pal_int_list[i][x]%8 < 4:
                    pal_int_list[i][x] = pal_int_list[i][x] - (pal_int_list[i][x]%8)
                else:
                    pal_int_list[i][x] = pal_int_list[i][x] + (8-(pal_int_list[i][x]%8))
        palette_lines[3 + i] = str(pal_int_list[i][0]) + ' ' + str(pal_int_list[i][1]) + ' ' + str(pal_int_list[i][2]) + '\n'

    fichier = open(path_to_pal , 'w' , encoding="UTF-8")
    for line in palette_lines:
        fichier.write((line ))
    fichier.close

files_in_directory = os.listdir()
for i in range(len(files_in_directory)):
    if files_in_directory[i][len(files_in_directory[i]) - 4 :] == '.pal':
        palette_format(files_in_directory[i])