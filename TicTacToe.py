class TicTacToe:
    
    def __init__(self):
        self.gameArea = ['1','2','3' , '4','5','6' , '7','8','9' ]        
        self.gameAreaUpdated = [' ',' ',' ' , ' ',' ',' ' , ' ',' ',' ' ]
        self.occupiedIndexes = []
        self.playerIndexes1 = []
        self.playerIndexes2 = []
        self.playerStatus = 0                

    def start(self):
        print('\n\t\t!!! Welcome !!!\n')
        
        self.player1 = input('Enter Name of First Player : ')
        self.player2 = input('Enter Name of Second Player : ')
    
    def isFinshed(self):
                
        winStates = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

        for state in winStates:
            if all (value in self.playerIndexes1 for value in state):
                print('\n\t!! Player 1 Wins, HURRAH !!\n')
                print('\n\t\tGAME OVER\n')
                return False

            elif all (value in self.playerIndexes2 for value in state):
                print('\n\t!! Player 2 Wins, HURRAH !!\n')
                print('\n\t\tGAME OVER\n')                                
                return False        

        if len(self.occupiedIndexes) == 9:
            print('\n\t!! MATCH TIE, WELL PLAYED !!')
            print('\n\t\tGAME OVER\n')
            return False
        
        return True        


    def showGameArea(self):

        print('\n   Map               Your Game')
        print('\n'+self.gameArea[0] + ' | ' + self.gameArea[1] + ' | ' + self.gameArea[2] + '            ' + self.gameAreaUpdated[0] + ' | ' + self.gameAreaUpdated[1] + ' | ' + self.gameAreaUpdated[2])        
        print('--+---+--            --+---+--')
        print(self.gameArea[3] + ' | ' + self.gameArea[4] + ' | ' + self.gameArea[5] + '            ' + self.gameAreaUpdated[3] + ' | ' + self.gameAreaUpdated[4] + ' | ' + self.gameAreaUpdated[5])
        print('--+---+--            --+---+--')
        print(self.gameArea[6] + ' | ' + self.gameArea[7] + ' | ' + self.gameArea[8] + '            ' + self.gameAreaUpdated[6] + ' | ' + self.gameAreaUpdated[7] + ' | ' + self.gameAreaUpdated[8]+'\n')
                

    def turn(self):
        
        if self.playerStatus == 0:
            print(f"\n\t{self.player1}'s turn\n")
        else:
            print(f"\n\t{self.player2}'s turn\n")

        try:
            userInput = int(input('Enter Block Number from Map : '))
        
        
            if userInput < 1 or userInput > 9:
                pass
            
            else:
                
                if userInput not in self.occupiedIndexes:

                    self.occupiedIndexes.append(userInput)

                    if self.playerStatus == 0:
                        self.gameAreaUpdated[userInput-1] = 'O'
                        self.playerIndexes1.append(userInput)
                        self.playerStatus = 1
                    else:
                        self.gameAreaUpdated[userInput-1] = 'X'
                        self.playerIndexes2.append(userInput)
                        self.playerStatus = 0

                else:

                    print('\n## This Place is already taken ##')
        
        except Exception as e:
            print('\n\tWrong Input')


if __name__ == '__main__':
    inst = TicTacToe()
    
    inst.start()
    inst.showGameArea()
    
    while inst.isFinshed():        
        inst.turn()
        inst.showGameArea()

