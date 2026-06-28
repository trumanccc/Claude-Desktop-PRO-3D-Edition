import argparse
from printing3d.core.analyze import analyze
from printing3d.reports.json import save

p=argparse.ArgumentParser()
sub=p.add_subparsers(dest="cmd")
a=sub.add_parser("analyze")
a.add_argument("file")
a.add_argument("--json",dest="jsonfile")
args=p.parse_args()

if args.cmd=="analyze":
    result=analyze(args.file)
    print(result)
    if args.jsonfile:
        save(result,args.jsonfile)
        print("JSON report written:",args.jsonfile)
else:
    p.print_help()
