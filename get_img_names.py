import os

def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith('.jpg')):
		    name = name.split('.')[0]
                    file.write(name + "\n")
                    break

def Test():
  dir="/home/ghz/fast-rcnn/data/VOCdevkit/VOC2007/JPEGImages"
  outfile="allnames.txt"
  wildcard = ".txt .exe .dll .lib"
 
  file = open(outfile,"w")
  if not file:
    print ("cannot open the file %s for writing" % outfile)

  ListFilesToTxt(dir,file,wildcard, 1)
 
  file.close()

Test()
