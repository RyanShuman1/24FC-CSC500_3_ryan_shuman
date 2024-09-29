
# psudocode part 1 
# fist get all total cost by adding consecutive costs until done 
# make sure consts are rounded and not less than 0 
# then multiply the food cost by .18 to find food tip
# multiply the food charge by .07 to find food tax
# add the tip, tax and food charge to find total 

#psudocode part 2
#l get the hours till the alarm goes off
# add that to the current time in hours
# take the modulo of the added time and 24 
# print

from datetime import datetime


def itemised_food_charge():
    total_food_charge = 0.0
    while True:
        try:
            food_charge = float(input(f"total: {str(total_food_charge)} enter the charge for the next food item or 0 if done: "))

            if food_charge == 0:

                return round(total_food_charge, 2)
            elif food_charge > 0:
                total_food_charge = food_charge + total_food_charge
            else:
                print("thats quite a deal on that food, i dont beleive you")
        except:
            print("invalid")

def part1(): 
    food_charge = itemised_food_charge()
   
    tip_percent = .18
    tax_percent =.07

    tip_amount = round(food_charge * tip_percent, 2)
    tax_amount = round(food_charge *  tax_percent, 2)

    total = round(tip_amount + tax_amount + food_charge, 2)

    print("the tip is: " + str(tip_amount))
    print("the tax is: "+ str(tax_amount))
    print("the total is: "+ str(total))



def part2(): 
    while True: 
        try: 
            hours = int(input("please enter a number of hours till the alarm goes off: " ))
            break 
        except KeyboardInterrupt: 
            exit() 
        except: 
            print("that not an integer or something")
    current_hour = datetime.now().hour
    alarm_hour = (current_hour + hours ) % 24
    print("the current hour is: " + str(current_hour))
    print("the alarm will go off at " + str(alarm_hour))

    
def main():
    part1()
    part2()

if __name__ == "__main__":
    main()