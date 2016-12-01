class fuelCalculator(object):
    def __init__(self):
        self.__date = "mm/dd/yyyy"  #initialize date
        self.__pricegas = 0         #initialize price of gas
        self.__gallonsgas = 0       #initialize gallons of gas
        self.__miles = 0            #initialize miles
        self.__pricepg = 0.0          #initialize price per gallon

    @property #date property
    def date(self):
        return self.__date
    @date.setter#date setter
    def date(self, date):
        self.__date = date
        return self.__date

    @property #price of gas property
    def pricegas(self):
        return self.__pricegas
    @pricegas.setter
    def pricegas(self, price):
        self.__pricegas = float(price)
        return self.__pricegas

    @property
    def pricepg(self):
        return self.__pricepg

    @property #gallons of gas
    def gallonsgas(self):
        return self.__gallonsgas
    @gallonsgas.setter
    def gallonsgas(self, gallons):
        self.__gallonsgas = float(gallons)
        return self.__gallonsgas

    @property #property for setting miles (int)
    def miles(self):
        return self.__miles
    @miles.setter
    def miles(self, dist):
        self.__miles = int(miles)
        return self.__miles

    def pricepg(self, price, gallons):
        price = float(price)
        gallons = float(gallons)
        self.__pricepg = abs(price / gallons)
        return self.__pricepg

    def setMilesRange(self, before, after): #range method for calculating miles (int)
        before = int(before)
        after = int(after)
        self.__miles = abs(after - before)
        return self.__miles

    def mpg(self): #calculate MPG, assuming miles and gallons properties are already set
        mpgR = round(self.__miles / self.__gallonsgas, 2) #miles per gallon equates to > miles / gallons
        return ("{}".format(mpgR))

    def status(self): #status method
        try:
            print("On {date}, you filled up {gallonsgas} gallons of gas, with a gas mileage of {mpg}".format(date = self.date, gallonsgas = self.gallonsgas, mpg = self.mpg()))
            print("Gas on {date} was approximately {price} dollars per gallon.".format(date = self.date, price = self.pricegas))
        except: #incase any properties are missing an error will be thrown and handled.
            print("Missing required component(s). >> date, gallons of gas, price of gas, mpg")

def main():
    #testing the fuelCalculator class.
    f = fuelCalculator()
    f.date = "10/11/2016"
    f.pricegas = 2.15
    f.gallonsgas = 6
    f.setMilesRange(1,188)
    f.pricepg(2.15, 5)
    print(f.mpg())
    f.status()

if __name__ == "__main__":
    main()
