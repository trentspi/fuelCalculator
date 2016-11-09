'''

date = input("What is the date? (mm/dd/yy) \n")
gallonsgas = float(input("How much gas was filled into the car? \n"))
pricegas = float(input("How much did it cost to fill the car? \n"))
bfmiles = int(input("How many miles did your car have during last recorded fill? \n"))
afmiles = int(input("How many miles did your car have after filling? \n"))

miles = afmiles - bfmiles
gas = round(pricegas / gallonsgas, 2)
mpg = round(miles / gallonsgas, 2)

print("On {date}, you filled up {gallonsgas} gallons, with a gas mileage of {mpg} MPG.".format(date = date, gallonsgas = gallonsgas, mpg = mpg) +
" Gas on {date} was approximately {gas} dollars per gallon.".format(date = date, gas = gas))

'''

class fuelCalculator(object):
    def __init__(self):
        self.__date = "mm/dd/yyyy"  #initialize date
        self.__pricegas = 0         #initialize price of gas
        self.__gallonsgas = 0       #initialize gallons of gas
        self.__miles = 0            #initialize miles

    @property #date property
    def date(self, date):
        self.__date = date
        return self.__date

    @property #price of gas property
    def pricegas(self, price):
        self.__pricegas = float(price)
        return self.__pricegas

    @property
    def gallonsgas(self, gallons):
        self.__gallonsgas = gallons
        return self.__gallonsgas 

    def miles(self, before, after):
        before = int(before)
        after = int(after)
        self.__miles = after - before
        return self.__miles

    def mpg(self, gallons, miles):
