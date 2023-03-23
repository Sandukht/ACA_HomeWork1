
def Euclid_algorithm(x, y):
    if y==0:
        return x
    else:
        while y:
            x= y%x
            return abs(x)

def G_C_D( a, b, *args):

    if len(args)>0:
        euclid= Euclid_algorithm(a,b)
        for a_r_g in args:
            g_c_d = Euclid_algorithm(euclid,a_r_g)
            euclid= g_c_d
            return  euclid
    else:
        return Euclid_algorithm(a,b)


#print(G_C_D(24,36,16 ))
#print(G_C_D(24, 36))
#print(G_C_D(24 ))
#print(G_C_D())
