
import argparse
from printing3d.profiles.kobra_x import fits
from printing3d.analyzers.estimate import estimate

p=argparse.ArgumentParser()
sub=p.add_subparsers(dest='cmd')

f=sub.add_parser('fits')
f.add_argument('x',type=float);f.add_argument('y',type=float);f.add_argument('z',type=float)

e=sub.add_parser('estimate')
e.add_argument('volume',type=float)
e.add_argument('--material',default='PLA')
e.add_argument('--price',type=float,default=20)

a=p.parse_args()

if a.cmd=='fits':
    print({'fits_kobra_x':fits(a.x,a.y,a.z)})
elif a.cmd=='estimate':
    print(estimate(a.volume,a.material,a.price))
else:
    p.print_help()
