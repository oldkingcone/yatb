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
            subprocess.call(line)
    except Exception as e:
        print("[~] Something went wrong: %s" % str(e))
        return False
    return "[!!] Complete, all processes are running. [!!]"

while True:
    read = str(input("[~] Where is the ctrl file? (full path only please) [~]\n->"))
    run_ctrl(read)
    if False:
        continue
