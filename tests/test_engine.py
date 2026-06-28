from printing3d.validators.kobra import fits
assert fits(200,200,200)
assert not fits(401,200,200)
print("Engine tests OK")
