class Board:
    def __init__(self , size = None , from_strings = None):
        self.size = size
        if size == None:
            self.size = 19
        else: 
            self.size = size
            assert size<=26 , "Illegal board size: must be between 2 and 26."
            assert size>=2 , "Illegal board size: must be between 2 and 26."
        self.board = [ [ None for j in range(self.size) ] for i in range(self.size) ]
        self.R = [-1 , 0 , 0 , 1]
        self.C = [0 , -1 , 1 , 0]
        for i in range (self.size):
            for j in range(self.size):
                self.board[i][j] = '.'
        if from_strings != None:
            assert type(from_strings)==list , "input is not a list"
            assert len(from_strings)==self.size , "length of input list does not match size"
            cnt = 0
            for element in from_strings:
                assert type(element)==str , "row "+str(cnt)+" is not a string"
                assert len(element)==self.size , "length of row "+str(cnt)+" does not match size"
                b = True
                for cha in element:

                    if(cha!='@' and cha!='.' and cha!='o'):
                        b=False
                    assert b==True , "invalid character in row "+str(cnt)
                cnt = cnt+1
            
    def get_size(self):
        return self.size
    
    def __str__(self):
        print('  ' , end='')
        for i in range(self.size):
            print(chr(i+97)+" " , end='')
        print()
        for i in range (self.size):
            print(chr(i+97) , end=' ')
            for j in range(self.size):
                print(self.board[i][j] , end=' ')
            print()

    def set_colour(self , coords , colour_name):
        x = ord(coords[0])-97  
        y = ord(coords[1])-97
        assert len(coords)==2 , "invalid coordinates"
        assert x<self.size , "column out of range"
        assert y<self.size , "raw out of range"
        if(colour_name == 'empty'):
            self.board[x][y] = '.'
        elif(colour_name == 'black'):
            self.board[x][y] = '@'
        else:
            self.board[x][y] = 'o'

    def get_colour(self , coords):
        x = ord(coords[0])-65  
        y = ord(coords[1])-65
        print(self.board[x][y])
    
    def to_strings(self):
        ret = []
        boardPos = ""
        for i in range(self.size):
            for j in range(self.size):
                boardPos = boardPos + ( ''.join(map(str,self.board[i][j])) ) 
            ret.append(boardPos)
            boardPos = ""
        return ret
    
    def to_integer(self):
        ret = list()
        for i in range(self.size):
            for j in range(self.size):
                if(self.board[i][j] == '.'):
                    ret.append(0)
                elif(self.board[i][j] == '@'):
                    ret.append(1)
                else:
                    ret.append(2)
        return ret
    
    def set_from_integer(self , integer_encodig):        
        cnt = 0
        for i in integer_encodig:
            if(i == 0):
                self.board[i%self.size][cnt] = '.'
            elif(i==1):
                self.board[i%self.size][cnt] = '@'
            else:
                self.board[i%self.size][cnt] = 'o'
            if(i%self.size == 0 and i!=0):
                cnt+=1
    
    def fill_reaching(self , reach_name , colour_name , visited , r , c):
        if self.board[r][c] == reach_name:
            return True
        colour_name_char = ''
        if(colour_name == 'black'):
            colour_name_char = '@'
        elif(colour_name == 'white'):
            colour_name_char = 'o'
        else:
            colour_name_char = '.'
        for i in range(4):
            if (r+self.R[i]>=0 and r+self.R[i]<self.size and c+self.C[i]>=0 and c+self.C[i]<self.size):
                if(visited[r+self.R[i]][c+self.C[i]] != True and self.board[r+self.R[i]][c+self.C[i]] == colour_name_char):
                    visited[r+self.R[i]][c+self.C[i]] = True
                    print(str(r+self.R[i])+" "+str(c+self.C[i]))
                    print(visited[r+self.R[i]][c+self.C[i]])
                    self.fill_reaching(reach_name , colour_name , visited , r+self.R[i] , c+self.C[i])
            
    def reaching_empty_matrix(self):
        mat = [ [ None for j in range(self.size) ] for i in range(self.size) ]
        for i in range(self.size):
            for j in range(self.size):
                visi = [ [ None for j in range(self.size) ] for i in range(self.size) ]
                if (self.board[i][j] == '.'):
                    mat[i][j] = True
                elif (self.board[i][j] == '@'):
                    mat[i][j] = self.fill_reaching(self , 'empty' , 'black' , visi , i , j)
                else:
                    mat[i][j] = self.fill_reaching(self , 'empty' , 'white' , visi , i , j)
        return mat            
                
def load_board(filename):
    with open(filename,'r') as data_file: # "position.txt"
        boardPos = data_file.read().split();
    board = Board(size = len(boardPos))
    for i in range (board.size):
        for j in range(board.size):
            board.board[i][j] = boardPos[i][j]
    return board

def save_board(filename, board: Board):
    boardPos = ""
    for i in range (board.size):
        boardPos = boardPos + ( ''.join(map(str,board.board[i])) ) + "\n"
    with open(filename,'w') as data_file: # "position.txt"
        data_file.write(boardPos)


B1 = load_board("position.txt")    
# B1.__str__()
# B1.set_colour('aa','white')
# B1.set_colour('ab','black')
# B1.set_colour('ac','white')
# B1.set_colour('ad','white')
# save_board("position.txt",B1)
B1.__str__()
visited = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
B1.fill_reaching('black' , 'black' , visited , 0 , 1)

# print(B1.to_integer())
# B1.set_from_integer(B1.to_integer())
# B1.__str__()
# print(B1.to_strings())
# B2 = Board(size = 4, from_strings = B1.to_strings())
# B2.__str__()

# b = Board(size = 4)
# b.__str__()