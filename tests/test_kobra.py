
from printing3d.profiles.kobra_x import fits
assert fits(200,200,200)
assert not fits(500,200,200)
print("Kobra profile OK")
