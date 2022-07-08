food = ["Apple", "Avocado", "Apricots", "Asparagus",[
    "Banana", "Broccoli", "Bacon", "Barley",[
        "Carrot", "Cauliflower", "Capsicum",[
            "Duck", "Dragon Fruit", "Dates", [
                "Egg", "Egg Plant", "Edam"]]]]]

for a in food:
    if isinstance(a, list):
        for b in a:
            if isinstance(b, list):
                for c in b:
                    if isinstance(c, list):
                        for d in c:
                            if isinstance(d, list):
                                for e in d:
                                    print(e)
                            else:
                                print(d)
                    else:
                        print(c)
            else:
                print(b)
    else:
        print(a)


                
                                
                            