from zipfile import ZipFile
def analyze(path):
 z=ZipFile(path)
 return {'entries':len(z.namelist()),'model_files':[n for n in z.namelist() if n.endswith('.model')]}
