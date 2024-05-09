class p9e2:
    @staticmethod
    def methodTambah(x, y=None):
        if y is None:
            return x
        else:
            return x + y 
    
mynum1 = p9e2.methodTambah(8, 5)
mynum2 = p9e2.methodTambah(4.5, 6.5)

print("Int: ", mynum1)
print("Float: ", mynum2)