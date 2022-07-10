names = ["Abishek", "Adam", "Andy", "Ajay", ["Barshana", "Brijesh", "Bishal", "Bunu", ["Chadani", "Chandan", "Chandu", 
                                                                                       ["Deepak", "Dinesh", "Dibyansh", "Dibesh", ["Elon", "Erik", "Eriksen", 
                                                                                        ["Fred", "Freddie", ]]]]]]

"""This is a module created 
in order to process a 
highly nested list"""

def process_list( name_list):
    """The function "process_list" is a 
    function created to process the List"""
    for names in name_list:
        if isinstance(names, list):
            process_list(names)
        else:
            print(names)
process_list(names)

#Use triple quotes to comment multiline. 
