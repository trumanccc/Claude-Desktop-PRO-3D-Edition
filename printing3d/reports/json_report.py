import json
def export(data,outfile):
 with open(outfile,'w',encoding='utf8') as f: json.dump(data,f,indent=2)
