def fnr(var):
    f=open("help.txt","r")
    # var="User"

    for l in f:
        if var.lower() in l:
            x=l.split()
            return x[2]

    f.close() 

