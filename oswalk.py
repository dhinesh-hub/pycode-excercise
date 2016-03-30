import os

def oswalk():
    for directory,sub_dir,files in os.walk("/home/dhinesh/pycode"):
        print directory
        for filename in files: 
            print filename
        print "-------------------------------"
oswalk()
