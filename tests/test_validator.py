from printing3d.validators.kobra import fits
assert fits(100,100,100)
assert not fits(500,100,100)
print("Validator OK")
