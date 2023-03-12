# make sure to execute this cell so that your function is defined
# you must re-run this cell any time you make a change to this function


def pizza(p):
    pizza_total = 0
    pepperoni = p.count("pepperoni")
    olive = p.count("olive")
    anchovy = p.count("anchovy")
    ham = p.count("ham")
    for orders in p:
            pizza_total += 13
            if "pepperoni" in p:
                pizza_total += pepperoni*1.00
            if "olive" in p:
                pizza_total += olive*0.50
            if "anchovy" in p:
                pizza_total += anchovy*2.00
            if "ham" in p:
                pizza_total += ham*1.50
    return pizza_total
def drinks(drink):
    drinks_total = 0
    small = drink.count("small")
    medium = drink.count("medium")
    large = drink.count("large")
    tub = drink.count("tub")
    for orders in drink:
        if "small" in drink:
            drinks_total += small*2.00
        if "medium" in drink:
            drinks_total += medium*3.00
        if "large" in drink:
            drinks_total += large*3.50
        if "tub" in drink:
            drinks_total += tub*3.75
    return drinks_total
def wings(wing):
    wings_total = 0
    for orders in wing:
        if 10 in wing:
            wings_total += 5.00
        if 20 in wing:
            wings_total += 9.00
        if 40 in wing:
            wings_total += 17.50
        if 100 in wing:
            wings_total += 48.00
    return wings_total
def cost_calculator(pizzas, drinks, wings, coupon):
 