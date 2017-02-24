#!/usr/bin/env python

import argparse
import sys
import os
from subprocess import Popen, PIPE

sim_sizes = {'test':'./evaluation/evaluation --kpvm-dram 1 4 128 1024 8 8 7 1000 1', 
            'small': './evaluation/evaluation --kpvm-dram 2 8 128 1024 8 8 7 20000 2',
            'medium': './evaluation/evaluation --kpvm-dram 2 16 128 1024 8 8 7 100000 4',
            'large' : './evaluation/evaluation --kpvm-dram 4 16 128 1024 8 8 7 200000 4'}

def runCmd(cmd, err, out, display = False):
    """
    Takes two strings, command and error, runs it in the shell
    and then if error string is found in stdout, exits.
    For no output = no error, use err=""
    """
    print cmd
    (stdout, stderr) = Popen(cmd, shell=True, stdout=PIPE).communicate()
    if display:
        print stdout
        if stderr:
            print stderr
    else:        
        if err is None:
            if stdout != "":
                print "Error: %s" %(out,)
            print "Truncated stdout below:"
            print '... ', stdout[-500:]
            sys.exit(2)
        else:
            if err in stdout:
                print "Error: %s" %(out,)
                print "Truncated stdout below:"
                print '... ', stdout[-500:]
                sys.exit(2)

def main(argv): 
    """
    Parses the arguments and cleans and/or builds the specified
    workloads of the whisper suite
    """
    parser = argparse.ArgumentParser(description='Builds echo from the whisper suite#.')
    parser.add_argument('benchmarks', metavar='workload', type=str, nargs=1,
               help='workloads to be run: tpcc/ycsb')
    parser.add_argument('--sim_size', dest='sim_size', action='store', 
            default='test', help='Simulation size: test, small, medium, large')

    args = parser.parse_args()
    print 'Running a ' + str(args.sim_size) + ' simulation for echo' 
    
    os.chdir('echo/src/')
    if args.sim_size in sim_sizes:
        os.environ['LD_LIBRARY_PATH'] = "./malloc/lib/:../lib/:$LD_LIBRARY_PATH"
        deleteCmd = 'rm -rf /dev/shm/efile'
        runCmd(deleteCmd, "Error", "Error deleting previous memory pool!")
        runCmd(sim_sizes[args.sim_size], "no free memory", "Simulation failed", True)
    os.chdir('../../')

if __name__ == "__main__":
    main(sys.argv[1:])
