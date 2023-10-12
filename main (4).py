#implementation of the player class
class player:
    def player(self):
        print("The player is playing cricket.")

class Batsman(player):
    def play(self):
        print("The batsman is batting.")

class Bowler(player):
    def play(self):
        print ("The bowler is bowling.")

  #create objects of Batsman and Bowler class and call the play() method for each object
if __name__=="__main__":
    batsman = Batsman()
    bowler = Bowler()

    batsman.play()
    bowler.play()