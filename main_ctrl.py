# need to run this as sudo, or admin.
# working on a work around for that.
# -> VERY IMPORTANT!!!!! Make sure all scripts located within the ctrl file are executable, chmod a+x 
try:
    import sys
    import subprocess
    import os
except ImportError as e:
    print("[!!] Something did not import: %s [!!]" % str(e))


def run_ctrl(afile):
    the_file = open(afile, "r")
    aline = the_file.readlines()
    try:
        for line in aline:
            lone ="python3 "+line.rstrip('\n')
            lone.join()
            os.system(lone)
    except Exception as e:
        print("[~] Something went wrong: %s" % str(e))
        return False
    return "[!!] Complete, all processes are running. [!!]"

while True:
    read = str(input("[~] Where is the ctrl file? (ex: somedirectory/ctrl) [~]\n->"))
    direct = './'+read
    run_ctrl(read)
    if False:
        continue
