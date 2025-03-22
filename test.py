def F(*args):
    
    db = []
    for i in range(len(args)):
        db.append((i,args[i]))

    return db

print(F(2134,6,3,2,54,67,67,3,35))