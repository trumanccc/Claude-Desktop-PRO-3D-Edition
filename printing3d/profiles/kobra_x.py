
BUILD_VOLUME=(400,400,450)

def fits(x,y,z):
    bx,by,bz=BUILD_VOLUME
    return x<=bx and y<=by and z<=bz
