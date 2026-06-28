import argparse
from printing3d.analyzers import stl
from printing3d.reports.markdown import export

parser=argparse.ArgumentParser()
parser.add_argument("file")
args=parser.parse_args()
res=stl.analyze(args.file)
print(export(res))
