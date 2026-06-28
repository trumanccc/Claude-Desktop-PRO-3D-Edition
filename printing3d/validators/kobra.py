BUILD=(400.0,400.0,450.0)
def fits(x,y,z):
    bx,by,bz=BUILD
    return x<=bx and y<=by and z<=bz
