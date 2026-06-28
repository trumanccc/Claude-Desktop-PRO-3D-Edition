import argparse
from printing3d.analyzers import stl,obj,threemf
p=argparse.ArgumentParser()
p.add_argument('type',choices=['stl','obj','3mf'])
p.add_argument('file')
a=p.parse_args()
m={'stl':stl.analyze,'obj':obj.analyze,'3mf':threemf.analyze}
print(m[a.type](a.file))
