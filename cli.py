import argparse
from printing3d.core.analyze import analyze
from printing3d.reports.markdown import export
p=argparse.ArgumentParser()
p.add_argument("file")
args=p.parse_args()
print(export(analyze(args.file)))
