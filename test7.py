def avale_dash(o):
        aval = True
        for p in range(2,o):
                if o%p ==0:
                        aval=False
        return aval


for l in range(1,20):
        print (l, avale_dash(2))


