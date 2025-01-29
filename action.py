from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            # apply the action (and insert to the table) if possible
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            activator_id = int(splittedline[2])
            date = splittedline[3]
            if quantity > 0 :
                repo.activities.insert(Activitie(product_id, quantity, activator_id, date))
                repo.products.find(id = product_id)[0].quantity += quantity
            elif repo.products.find(id = product_id)[0].quantity + quantity >= 0:
                repo.activities.insert(Activitie(product_id, quantity, activator_id, date))
                repo.products.find(id = product_id)[0].quantity += quantity
                
                

if __name__ == '__main__':
    main(sys.argv)