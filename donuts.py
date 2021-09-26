import urllib.request
import json
import getopt, sys

class Donut:
    def __init__(self, itemName, itemTopping):
        self.itemName = itemName
        self.itemTopping = itemTopping
   
    
    def findTopping(self):
        #url = 'https://opensource.adobe.com/Spry/data/json/donuts.js'
        url = 'http://billingplus/sample1.json'
        with urllib.request.urlopen(url) as response:
            data_json = json.loads(response.read())
        flag = False    
        for x in list(data_json["items"]["item"]):
            if (x["name"]==self.itemName):
                for toppings in  (x["topping"]):
                    if (toppings["type"]==self.itemTopping):
                        #print ("%s topping is available in Item: %s" %(self.itemTopping,self.itemName))
                        print ("This topping is available")
                        flag=True
        if (flag==False):
            #print ("%s topping is not available in Item: %s" %(self.itemTopping,self.itemName))
            print ("This topping is not available")


argumentList = sys.argv[1:]
options = "n:t:"
long_options = ["name=", "topping="] 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    #for currentArgument, currentValue in arguments:
    for opt, arg in arguments:
        if opt in ('-n', '--name'):
            itemName = arg
        elif opt in ('-t', '--topping'):
            itemTopping = arg
    
    donutobj=Donut(itemName,itemTopping)
    donutobj.findTopping()
        
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))      
    
