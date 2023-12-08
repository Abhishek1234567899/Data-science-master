import os


path="notebooks/research.ipynb" # combination of file and folder 

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open(file,"w") as f:
    pass