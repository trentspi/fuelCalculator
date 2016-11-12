from tkinter import *
from fuelCalculator import *

class fuelVis(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Fuel Calculator 3.0")
        self.minsize(width = 610, height = 400)
        self.configure(background = "black") #black window background
        self.fuelFrame = Frame()
        self.fuelFrame.config(bg = "black") #black frame background
        self.fuelFrame.grid(row=0,column=0)
        self.cMPG = 0 #initialize calculated MPG variable
        self.fuelLabels() #draw the fuel labels and entry inputs
        self.fuelImage() #draw a fuel icon image
        self.calculateButton() #calculate mpg using fuelCalculator class
        self.mainloop() #call the mainloop


    def fuelLabels(self):
        #enter the date when gas was filled
        self.dateLabel = Label(self.fuelFrame, text = "Enter date when gas was filled: (optional)", fg="white", bg = "black")
        self.dateLabel.grid(row = 0, column = 0, padx= (20, 0), pady=(20,0))
        self.dateEntry = Entry(self.fuelFrame, bg = "black", fg= "white")
        self.dateEntry.grid(row = 0, column = 1, padx= (20, 0), pady=(20,0))

        #enter the total price spent on gas, used to determine price per gallon
        self.totalGasPriceLabel = Label(self.fuelFrame, text = "Total price spent on gas: ($)", fg="white", bg = "black")
        self.totalGasPriceLabel.grid(row = 2, column = 0, padx= (20, 0), pady=(20,0))
        self.totalGasPriceEntry = Entry(self.fuelFrame, bg = "black", fg= "white")
        self.totalGasPriceEntry.grid(row = 2, column = 1, padx= (20, 0), pady=(20,0))

        #enter the amount of gallons filled, used for calculating MPG
        self.gallonsFilledLabel = Label(self.fuelFrame, text = "Gallons of gas filled during fueling: ", fg="white", bg = "black")
        self.gallonsFilledLabel.grid(row = 4, column = 0, padx= (20, 0), pady=(20,0))
        self.gallonsFilledEntry = Entry(self.fuelFrame, fg="white", bg = "black")
        self.gallonsFilledEntry.grid(row = 4, column = 1, padx= (20, 0), pady=(20,0))

        #Odometer reading during the previous fill
        self.beforeMilesLabel = Label(self.fuelFrame, text = "Odometer reading when the car was previously fueled? ", fg="white", bg = "black")
        self.beforeMilesLabel.grid(row = 6, column = 0, padx= (20, 0), pady=(20,0))
        self.beforeMilesEntry = Entry(self.fuelFrame, bg = "black", fg= "white")
        self.beforeMilesEntry.grid(row = 6, column = 1, padx= (20, 0), pady=(20,0))

        #Odometer reading after the current fill
        self.afterMilesLabel = Label(self.fuelFrame, text = "Odometer reading when the car was most recently refueled? ", fg="white", bg = "black")
        self.afterMilesLabel.grid(row = 8, column = 0, padx= (20, 0), pady=(20,0))
        self.afterMilesEntry = Entry(self.fuelFrame, bg = "black", fg= "white")
        self.afterMilesEntry.grid(row = 8, column = 1, padx= (20, 0), pady=(20,0))

        #grid the output label which displays MPG calculation
        self.mpgOutputLabel = Label(self.fuelFrame, text = ("{} miles per gallon".format(self.cMPG)), font=("Helvetica", 32))
        self.mpgOutputLabel.grid(row = 10, column = 0, padx = (0,0), pady=(20,0))


    def calculateButton(self):
        self.calcButton = Button(self.fuelFrame, text = "Calculate MPG!", command = self.calcMPG) #create rectangle button
        #calls the self.createRect function for creating and drawing a rectangle
        self.calcButton.grid(row = 9, column = 1, padx=(20,0), pady=(20,0))

    def calcMPG(self):
        cFuel = fuelCalculator() #using fuelCalculator class
        try:
            cFuel.date = str(self.dateEntry) #set date
            cFuel.pricegas = float(self.totalGasPriceEntry.get()) #set price of gas
            cFuel.gallonsgas = float(self.gallonsFilledEntry.get()) #set gallons of gas filled
            cFuel.setMilesRange(int(self.beforeMilesEntry.get()), int(self.afterMilesEntry.get())) #miles range
            c = cFuel.mpg()
        except: #prevents float division by 0 error
            c = 0  #set mpg equal to 0, if calculation is null or out of bounds or even 0.
        self.mpgOutputLabel["text"] = ("{} miles per gallon".format(c))

    def fuelImage(self):
        self.g = PhotoImage(file = 'gasdrop.gif') #PhotoImage is limited on type of file support, gif is the most used / supported
        self.gasImage = Label(self.fuelFrame, image=self.g, bg = "black") #transparent image with black background
        self.gasImage.grid(row = 10, column = 1, sticky = "w", pady = (20,0))

def main():
    f = fuelVis()

if __name__ == "__main__": #if namespace is main, execute main
    main()
