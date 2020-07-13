import numpy as np

def covert_txt_to_array (file):
    board = np.zeros((9,9))
    count = 0
    i = 0
    j = 0
    haveNumber = False
    while count <81:
        content=file.readline()
        haveNumber = False
        for x in range(len(content)):
            try:
                if int(content[x]) > 0 and int(content[x]) < 10:
                    board[i,j]=int(content[x])
                    j = j + 1
                    count = count +1
                    haveNumber = True
            except ValueError:
                if content[x]=='_':
                    j = j + 1
                    count = count +1
                    haveNumber = True
                #else:
                    #print(content[x], 'is not regonized')
            if j == 9:
                j = 0
        if haveNumber:
            i = i + 1
    return board   
