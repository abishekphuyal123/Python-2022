names = ["Abi", "Aryan", "Anubhav", "Aarya", "Abhaya", ["Barshana", "Bishal", "Bibek", ["Chandra", "Chandan", ["Dinesh", "David", "Deepak", "Diwash", ["Erica", "Eleanor", ["Farahan"]]]]]]

for A in names:
    if isinstance(A, list):
        for B in A:
            if isinstance(B, list):
                for C in B:
                    if isinstance(C, list):
                        for D in C:
                            if isinstance(D, list):
                                for E in D:
                                    if isinstance(E, list):
                                        for F in E:
                                            print(F)
                                    else:
                                        print(E)
                            else:
                                print(D)
                    else:
                        print(C)
            else:
                print(B)
    else:
        print(A)            
    
