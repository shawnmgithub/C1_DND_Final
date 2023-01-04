#import random and tkinter
from tkinter import *
from random import *
#create a TK class that will be the main information present on all frames.
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Shawn M: Final Project")
        self.geometry("500x500")
        #sets the state to A so the program knows to display the main menu screen
        self.state = "A"
        '''creates a label called Menu and adds it to the screen.'''
        self.lblA = Label(self, text = "Menu", font = 3000,)
        self.lblA.grid(row = 1, column = 0, sticky ="n")
                
        self.ctrB = frmDice(self)
        self.ctrC = frmCharacter(self)
        '''creates a button that calls the switchRoll method to switch to the dice rolling screen and add's the button to the grid.'''
        self.btnDice = Button(self, text = "Dice Roller", command = self.switchRoll)
        self.btnDice.grid(row = 6, column = 0)
        '''Creates a button that calls the switchCreator method to switch to the character creation screen and adds the button to the grid.'''
        self.btnCharacter = Button(self, text = "Character Creator", command = self.switchCreator)
        self.btnCharacter.grid(row = 7, column = 0)
        
        self.mainloop()
        '''switches the frame to state B, or the Dice Rolling Frame by removing the other 2 frames from the view.'''
    def switchRoll(self):
        self.state = "B"
        self.lblA.grid_remove()
        self.ctrC.grid_remove()
        self.ctrB.grid(row = 0, column = 0)
    #switches the frame to state C by removing the other 2 frames from the view
    def switchCreator(self):
            self.state = "C"
            self.ctrB.grid_remove()
            self.lblA.grid_remove()
            self.ctrC.grid(row = 0, column = 0)
    

'''' The frmDice class will display the Dice Rolling part of the application, this will inherit info from the App Class.'''

'''' The dice roller will prompt the user with a list of different dice they can roll, when the user presses one of the buttons, a random number is generated within the parameters of the dice they roll and is output at the top'''

class frmDice(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.lblOut = Label(self, text = "Click Which dice type you want to roll", width = 30)
        '''adds the label to the top of the screen, this label is the output of the rollD(x) methods'''
        self.lblOut.grid(sticky = "we")
        #Creates buttons with the corresponding dice that will roll
        self.btnOne = Button(self, text = "d4", command = self.rollD4)
        self.btnOne.grid(sticky = "we")
        
        self.btnTwo = Button(self, text = "d6",  command = self.rollD6)
        self.btnTwo.grid(sticky = "we")
        
        self.btnThree = Button(self, text = "d8", command = self.rollD8)
        self.btnThree.grid(sticky = "we")

        self.btnFour = Button(self, text = "d10", command = self.rollD10)
        self.btnFour.grid(sticky = "we")
        
        self.btnFive = Button(self, text = "d12", command = self.rollD12)
        self.btnFive.grid(sticky = "we")

        self.btnSix = Button(self, text = "d20", command = self.rollD20)
        self.btnSix.grid(sticky = "we")
        
        '''these methods roll a random number based on what type of dice they are rolling and outputs the value.'''
    def rollD4(self):
        x = randint(1,4)
        x = str(x)
        self.lblOut["text"] = x
        
    def rollD6(self):
        x = randint(1,6)
        x = str(x)
        self.lblOut["text"] = x
        
    def rollD8(self):
        x = randint(1,8)
        x = str(x)
        self.lblOut["text"] = x

    def rollD10(self):
        x = randint(1,10)
        x = str(x)
        self.lblOut["text"] = x

    def rollD12(self):
        x = randint(1,12)
        x = str(x)
        self.lblOut["text"] = x

    def rollD20(self):
        x = randint(1,20)
        x = str(x)
        self.lblOut["text"] = x


#The frmDice class will display the character creator part of the application, along with being responsible for prompting the final result window
  
 #the character creator will prompt the user to input all of the specific information needed to build a DnD character. After all the information is recived it calculates all of the final stat values and outputs a new screen with this information for the user to copy down to their character sheet   
class frmCharacter(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.lblOut = Label(self, text = "Character Creator", width = 30)

        '''' Taking in the entries for all of the needed data, this will store them as strings. '''
        self.txtName = Entry(self)
        self.txtStr = Entry(self)
        self.txtDex = Entry(self)
        self.txtCon = Entry(self)
        self.txtWis = Entry(self)
        self.txtChar = Entry(self)
        self.txtInt = Entry(self)
        ''' These two are spinbox menus to ensure the program will be able to "understand" the user's input and apply proper class and race bonuses'''
        self.spinRace=Spinbox(self,values=("Dragonborn","Dwarf","Elf","Gnome","Halfling","Half-Orc","Human","Tiefling" )) 
        self.spinClass=Spinbox(self,values=("Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rouge","Sorcerer","Warlock","Wizard" ))
        #creates the label that appears on the side to tell the user how to roll stats if they want to do it manually
        self.lblInfo = Label(self,text = "to roll stats please roll 4 D6 and add the highest 3 values, or leave blank to have your stats rolled automatically. Please use arrows on menu, do not type in your own race/class",wraplength = 300 )
        
        # The submit button will do all of the calculations required to output a complete character and then display it all on a new pop out window
        self.btnSubmit = Button(self,text="Submit", command = self.submitWindow)
        #creates labels for all of the names next to the user entry boxes
        self.lblName = Label(self, text = "Name", width = 30)
        self.lblRace = Label(self, text = "Race", width = 30)
        self.lblClass = Label(self, text = "Class", width = 30)
        self.lblStr = Label(self, text = "Strength", width = 30)
        self.lblDex = Label(self, text = "Dexterity", width = 30)
        self.lblCon = Label(self, text = "Constitution", width = 30)
        self.lblWis = Label(self, text = "Wisdom", width = 30)
        self.lblChar = Label(self, text = "Charisma", width = 30)
        self.lblInt = Label(self, text = "intelligence", width = 30)

        #puts both the labels and the user entry boxes onto the screen
        self.lblName.grid(row = 0, column = 0)
        self.lblRace.grid(row = 1, column = 0)
        self.lblClass.grid(row = 2, column = 0)
        self.lblStr.grid(row = 3, column = 0)
        self.lblDex.grid(row = 4, column = 0)
        self.lblCon.grid(row = 5, column = 0)
        self.lblWis.grid(row = 6, column = 0)
        self.lblChar.grid(row = 7, column = 0)
        self.lblInt.grid(row = 8, column = 0)
        self.lblInfo.grid(row = 14)
        self.btnSubmit.grid(row=9, column = 1)
        self.txtName.grid(row = 0, column = 1)
        self.spinRace.grid(row = 1, column = 1)
        self.spinClass.grid(row = 2, column = 1)
        self.txtStr.grid(row = 3, column = 1)
        self.txtDex.grid(row = 4, column = 1)
        self.txtCon.grid(row = 5, column = 1)
        self.txtWis.grid(row = 6, column = 1)
        self.txtChar.grid(row = 7, column = 1)
        self.txtInt.grid(row = 8, column = 1)
    
    # these get methods is how the data is being collected and stored into a usable form.
    def getName(self):
        x = self.txtName.get()
        return x
    def getStr(self):
        x = self.txtStr.get()
        return x
    def getDex(self):
        x = self.txtDex.get()
        return x
    def getCon(self):
        x = self.txtCon.get()
        return x
    def getWis(self): 
        x = self.txtWis.get()
        return x 
    def getCharisma(self):
        x = self.txtChar.get()
        return x   
    def getRace(self):
        x = self.spinRace.get()
        return x
    def getCharClass(self):
        x = self.spinClass.get()  
        return x
    def getInt(self):
        x=self.txtInt.get()
        return x

     ##the CheckStat methods take in a given stat and the user's selected race to apply any and all stat bonuses that the characters will have, this also rolls fresh stats for the user if they chose to leave the entries blank to have the stats automatically rolled for them.This is done by taking 4 random numbers between 1 and 6, then putting them into a list and sorting them to only add the largest 3 values together 
    def checkStr(self,strength,race):
        if strength == "":
            strength = 0
            D6One = randint(1,6)
            D6Two = randint(1,6)
            D6Three = randint(1,6)
            D6Four =  randint(1,6)
            dicePool = [D6One, D6Two, D6Three, D6Four]
            dicePool = sorted(dicePool)
            dicePool = dicePool[1:]
            total = 0
            for i in range(0, len(dicePool)):
                total = total + dicePool[i]
                strength = total     
        if race == "Dragonborn":
            strength = int(strength)
            strength = strength + 2
        if race == "Half-Orc":
            strength = int(strength)
            strength = strength + 2
        if race == "Human":
            strength = int(strength)
            strength = strength + 1
        return strength
    def checkDex(self,dexterity,race):
        if dexterity == "":
            dexterity = 0
            D6One = randint(1,6)
            D6Two = randint(1,6)
            D6Three = randint(1,6)
            D6Four =  randint(1,6)
            dicePool = [D6One, D6Two, D6Three, D6Four]
            dicePool = sorted(dicePool)
            dicePool = dicePool[1:]
            total = 0
            for i in range(0, len(dicePool)):
                total = total + dicePool[i]
                dexterity = total
        if race =="Elf":
            dexterity = int(dexterity)
            dexterity = dexterity + 2
        if race =="Halfling":
            dexterity = int(dexterity)
            dexterity = dexterity + 2
        if race == "Human":
            dexterity = int(dexterity)
            dexterity = dexterity + 1
        return dexterity
    def checkCon(self,constitution,race):
        if constitution == "":
            constitution = 0
            D6One = randint(1,6)
            D6Two = randint(1,6)
            D6Three = randint(1,6)
            D6Four =  randint(1,6)
            dicePool = [D6One, D6Two, D6Three, D6Four]
            dicePool = sorted(dicePool)
            dicePool = dicePool[1:]
            total = 0
            for i in range(0, len(dicePool)):
                total = total + dicePool[i]
                constitution = total
        if race == "Dwarf":
            constitution = int(constitution)
            constitution = constitution + 2
        if race == "Half-Orc":
            constitution = int(constitution)
            constitution = constitution + 1
        if race == "Human":
            constitution = int(constitution)
            constitution = constitution + 1
        return constitution
    def checkWis(self,wisdom,race):
        if wisdom == "":
            wisdom = 0
            D6One = randint(1,6)
            D6Two = randint(1,6)
            D6Three = randint(1,6)
            D6Four =  randint(1,6)
            dicePool = [D6One, D6Two, D6Three, D6Four]
            dicePool = sorted(dicePool)
            dicePool = dicePool[1:]
            total = 0
            for i in range(0, len(dicePool)):
                total = total + dicePool[i]
                wisdom = total
            if race == "Human":
                wisdom = int(wisdom)
                wisdom = wisdom + 1
        return wisdom
    def checkCharisma(self,charisma,race):
        if charisma == "":
            charisma = 0
            D6One = randint(1,6)
            D6Two = randint(1,6)
            D6Three = randint(1,6)
            D6Four =  randint(1,6)
            dicePool = [D6One, D6Two, D6Three, D6Four]
            dicePool = sorted(dicePool)
            dicePool = dicePool[1:]
            total = 0
            for i in range(0, len(dicePool)):
                total = total + dicePool[i]
                charisma = total
        if race == "Dragonborn":
            charisma = int(charisma)
            charisma = charisma + 1
        if race == "Human":
            charisma = int(charisma)
            charisma = charisma + 1
        if race =="Tiefling":
            charisma = int(charisma)
            charisma = charisma + 2
        return charisma

    def checkInt(self,intelligence,race):
        if intelligence == "":
            intelligence = 0
            D6One = randint(1,6)
            D6Two = randint(1,6)
            D6Three = randint(1,6)
            D6Four =  randint(1,6)
            dicePool = [D6One, D6Two, D6Three, D6Four]
            dicePool = sorted(dicePool)
            dicePool = dicePool[1:]
            total = 0
            for i in range(0, len(dicePool)):
                total = total + dicePool[i]
                intelligence = total
        if race == "Gnome":
            intelligence = int(intelligence)
            intelligence = intelligence + 2
        if race == "Human":
            intelligence = int(intelligence)
            intelligence = intelligence + 1
        if race =="Tiefling":
            intelligence = int(intelligence)
            intelligence = intelligence + 1
        return intelligence   
    #check speed only changes your speed from 30 if you are a Gnome,Dwarf,or Halfling
    def checkSpeed(self,race):
        speed = 30
        if race == "Gnome":
            speed =25
        if race == "Dwarf":
            speed = 25
        if race == "Halfling":
            speed = 25
        return speed
    # these methods will take in the given stat, then subrat 10 from it then divide by 2, rounding down to get the player's given roll bonuses for all 6 of the stats.
    def checkStrRoll(self,strength):
        strength = int(strength)
        strRoll = strength - 10
        strRoll = strRoll //2
        return strRoll
    def checkDexRoll(self,dexterity):
        dexterity = int(dexterity)
        dexRoll = dexterity - 10
        dexRoll = dexRoll //2
        return dexRoll
    def checkConRoll(self,constitution):
        constitution = int(constitution)
        conRoll = constitution - 10
        conRoll = conRoll //2
        return conRoll
    def checkWisRoll(self,wisdom):
        wisdom = int(wisdom)
        wisRoll = wisdom - 10
        wisRoll = wisRoll //2
        return wisRoll
    def checkCharismaRoll(self,charisma):
        charisma = int(charisma)
        charismaRoll = charisma - 10
        charismaRoll = charismaRoll //2
        return charismaRoll
    def checkIntRoll(self,intelligence):
        intelligence = int(intelligence)
        intRoll = intelligence - 10
        intRoll = intRoll //2
        return intRoll
    #opens a new window and calls all of the methods to do the proper calculations to manipulate the stats, find the roll bonuses, and find your speed,AC,and initiative
    def submitWindow(self):
        #calls all of the methods to get the user's data from the previous screen.
        name = self.getName()
        characterClass=self.getCharClass()
        race = self.getRace()
        strength = self.getStr()
        dexterity = self.getDex()
        constitution = self.getCon()
        wisdom = self.getWis()
        charisma = self.getCharisma()
        intelligence = self.getInt()    
        #the check methods all ensure the user has inputed somthing for their stat and then applys any race bonus  
        strength = self.checkStr(strength,race)
        dexterity = self.checkDex(dexterity,race)
        constitution = self.checkCon(constitution,race)
        wisdom = self.checkWis(wisdom,race)
        charisma = self.checkCharisma(charisma,race)
        intelligence = self.checkInt(intelligence,race)       
        strRoll = self.checkStrRoll(strength)
        dexRoll = self.checkDexRoll(dexterity)
        conRoll = self.checkConRoll(constitution)
        wisRoll = self.checkWisRoll(wisdom)
        charismaRoll = self.checkCharismaRoll(charisma)
        intRoll = self.checkIntRoll(intelligence)
        armorClass = (dexRoll+10)
        strRoll=str(strRoll)
        dexRoll=str(dexRoll)
        conRoll=str(conRoll)
        wisRoll=str(wisRoll)
        charismaRoll=str(charismaRoll)
        intRoll=str(intRoll)
        initiative = dexRoll
        speed = self.checkSpeed(race)

        #creates a new window and sets the size to 500 x 500 to be even with the rest of the windows
        newWindow = Toplevel(self)
        newWindow.geometry("500x500")

        #creates more labels to be outputting on the final screen
        self.labelName = Label(newWindow, text = "Name", width = 30)
        self.labelRace = Label(newWindow, text = "Race", width = 30)
        self.labelClass = Label(newWindow, text = "Class", width = 30)
        self.labelStr = Label(newWindow, text = "Strength", width = 30)
        self.labelDex = Label(newWindow, text = "Dexterity", width = 30)
        self.labelCon = Label(newWindow, text = "Constitution", width = 30)
        self.labelWis = Label(newWindow, text = "Wisdom", width = 30)
        self.labelCharisma = Label(newWindow, text = "Charisma", width = 30)
        self.labelInt = Label(newWindow,text = "Intelligence",width = 30)
        self.labelSpeed = Label(newWindow,text = "Speed",width= 30)
        self.labelArmorclass = Label(newWindow,text = "AC",width = 30)
        self.labelInitiative = Label(newWindow, text ="initiative", width = 30)
        self.labelInfo = Label(newWindow, text = "roll bonuses:", width = 20)
        self.LabelEnd = Label(newWindow,text = "The hard part is over! Make sure to copy all of this information on to your character sheet. All you need to get from your DM/yourself is your spells, skills, and all of the creative aspects of your character",wraplength = 170,font=("Courier", 10))
        #creates labels with the actual information the user was looking to generate.
        self.charName = Label(newWindow, text = name)
        self.charClass = Label(newWindow, text = characterClass)
        self.charRace = Label(newWindow, text = race)
        self.charStr = Label(newWindow, text = strength)
        self.charDex = Label(newWindow, text = dexterity)
        self.charCon = Label(newWindow, text = constitution)
        self.charWis = Label(newWindow, text = wisdom)
        self.charCharisma = Label(newWindow, text = charisma)
        self.charInt = Label(newWindow, text = intelligence)
        self.charSpeed = Label(newWindow,text = speed)
        self.charInitiative = Label(newWindow,text = "+"+"("+ initiative+")")
        self.charArmorClass = Label(newWindow,text = armorClass)
        
        #making the labels with roll bonuses, added a () around each to ensure the user knows when the values are negative.
        self.labelRollStr = Label(newWindow, text = "+"+"("+strRoll+")", width = 30)
        self.labelRollDex = Label(newWindow, text = "+"+"("+ dexRoll+")", width = 30)
        self.labelRollCon = Label(newWindow, text = "+"+"("+ conRoll+")", width = 30)
        self.labelRollWis = Label(newWindow, text = "+"+"("+ wisRoll+")", width = 30)
        self.labelRollCharisma = Label(newWindow, text = "+"+"("+ charismaRoll+")", width = 30)
        self.labelRollInt = Label(newWindow, text = "+"+"("+ intRoll+")", width = 30)


        
        
        #adds all of the labels to the screen.
        self.labelName.grid(row = 0, column = 0)
        self.labelRace.grid(row = 1, column = 0)
        self.labelClass.grid(row = 2, column = 0)
        self.labelStr.grid(row = 3, column = 0)
        self.labelDex.grid(row = 4, column = 0)
        self.labelCon.grid(row = 5, column = 0)
        self.labelWis.grid(row = 6, column = 0)
        self.labelCharisma.grid(row = 7, column = 0)
        self.labelInt.grid(row = 8, column = 0)
        self.labelSpeed.grid(row=9,column=0)
        self.labelInitiative.grid(row=10,column=0)
        self.labelArmorclass.grid(row=11,column=0)
        self.labelInfo.grid(row = 2, column = 5)

        self.charName.grid(row = 0, column = 2)
        self.charRace.grid(row = 1, column = 2)
        self.charClass.grid(row = 2, column = 2)
        self.charStr.grid(row = 3, column = 2)
        self.charDex.grid(row = 4, column = 2)
        self.charCon.grid(row = 5, column = 2)
        self.charWis.grid(row = 6, column = 2)
        self.charCharisma.grid(row = 7, column = 2)
        self.charInt.grid(row = 8, column = 2)
        self.charSpeed.grid(row=9,column=2)
        self.charArmorClass.grid(row=11,column=2)
        self.charInitiative.grid(row=10,column=2)
        
        self.LabelEnd.grid(row = 15,column = 0,columnspan = 6,rowspan=6)

        self.labelRollStr.grid(row=3,column=3)
        self.labelRollDex.grid(row=4,column=3)
        self.labelRollCon.grid(row=5,column=3)
        self.labelRollWis.grid(row=6,column=3)
        self.labelRollCharisma.grid(row=7,column=3)
        self.labelRollInt.grid(row=8,column=3)


       
           



def main():
    app = App()
    
if __name__ == "__main__":
    main()
