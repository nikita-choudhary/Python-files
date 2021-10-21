import os
oldname="Files\sample.txt"
newname="Files\sample2.txt"
with open(oldname) as f:
    content=f.read()

with open(newname,"w") as f:
    f.write(content)

os.remove(oldname)