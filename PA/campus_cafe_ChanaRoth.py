# ==============================================================================
# Chana Roth
# Assignment: Module 2: PA 1: Campus Cafe
# Class: MCON 141
# Due Date: 9/24/26
#
# Psuedo code:
# 1. Define campus_cafe function
# 2. Set prices for items and set the tax rate
# 3. Write menu - formatted currency - include nice spacing and 2 decimal space.
# 4. create a try prompt for user inputs of qty/percent number.
# 5. Ask user (input) quantity for coffee, muffin, and bagel. Ask tip percent as well. write except here for try in 4.
# 6. Calculation: subtotal for each item and combine subtotals for that.
# 7, Calculation: tax and tip amount - based on what subtotal is.
# 8. Calculation: grand total (TOTAL) - add subtotal, tax, and tip.
# 9. print receipt title, items, subtotal, tax, tip, and total.
# 10. make all lines spaced out nicely
# 11. Print on bottom of recipeit thank you messages.
# ==============================================================================

def campus_cafe():
    coffee_price = 2.25
    muffin_price = 2.75
    bagel_price = 2.50
    tax_percent = 8.875

    print("== Campus Cafe Menu ==\n")
    print(f" - Coffee: ${coffee_price:.2f}\n")
    print(f" - Muffin: ${muffin_price:.2f}\n")
    print(f" - Bagel: ${bagel_price:.2f}\n")


    try:
        coffee_qty = int(input("How many coffees? "))
        print()
        muffin_qty = int(input("How many muffins? "))
        print()
        bagel_qty = int(input("How many bagels? "))
        print()
        tip_percent = float(input("Enter tip percent (e.g., 10 for 10%): "))
        print()
    except ValueError:
        print("Error: That was not a valid number.")

    coffee_subtotal = coffee_qty * coffee_price
    muffin_subtotal = muffin_qty * muffin_price
    bagel_subtotal = bagel_qty * bagel_price

    subtotal = coffee_subtotal + muffin_subtotal + bagel_subtotal
    tax = subtotal * (tax_percent/100)
    tip = subtotal * (tip_percent /100 )

    total = subtotal + tax + tip

    subtotal = f"{subtotal:.2f}"
    tax = f"{tax:.2f}"
    tip = f"{tip:.2f}"
    total = f"{total:.2f}"


    print ("--- Receipt ---\n")
    print (f"{coffee_qty} x Coffee @ ${coffee_price:.2f} = ${coffee_subtotal:.2f}\n")
    print (f"{muffin_qty} x Muffin @ ${muffin_price:.2f} = ${muffin_subtotal:.2f}\n")
    print (f"{bagel_qty} x Bagel @ ${bagel_price:.2f} = ${bagel_subtotal:.2f}\n")
    print (f"Subtotal:     ${subtotal}\n")
    print (f"Tax({tax_percent}%):     ${tax}\n")
    print (f"Tip({tip_percent}%):     ${tip}\n")
    print (f"TOTAL:     ${total}\n")

    print("Thank you!")
    print("Enjoy your day.")

campus_cafe()


