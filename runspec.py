#!/usr/bin/python3
import os
import sys
import time
import argparse
from datetime import datetime
from functools import reduce
from multiprocessing import Pool
# import shutil
import resource

parser = argparse.ArgumentParser(description = 'Run spec cpu with prefix(none, qemu, perf, pin, dynamorio, strace, time), get log or performance')
parser.add_argument('-i', '--size', default="test", choices=['test', 'train', 'ref', 'refrate'])
parser.add_argument('-s', '--spec', default="2006", choices=['2000', '2006', '2017'])
parser.add_argument('-T', '--tune', default="base", choices=['base', 'peak'])
parser.add_argument('-b', '--benchmark', default="all")
parser.add_argument('-t', '--threads', default=1, type=int)
parser.add_argument('-l', '--loose', action='store_true')
parser.add_argument('-p', '--print_cmd_only', action='store_true')
parser.add_argument('-c', '--cmd_prefix', default='')
parser.add_argument('--title', default="test_title")
parser.add_argument('--log_dir_prefix', default=os.path.expanduser('~') + '/spec')
parser.add_argument('--dir00', default=".")
parser.add_argument('--dir06', default=".")
parser.add_argument('--dir17', default=".")
parser.add_argument('--ext06', default="none")
parser.add_argument('--ext17', default="none")
parser.add_argument('--slimit', type=int, default=-1,help="The limit of the stack size, 0 ulimited, or a number(MB), default: not modified")
args = parser.parse_args()

print(args)

slimit = args.slimit
if slimit == 0:
    resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
elif slimit > 0:
    slimit <<= 20
    resource.setrlimit(resource.RLIMIT_STACK, (slimit, slimit))



# runspec config
SPEC = args.spec
SIZE = args.size
# only 2017
TUNE = args.tune # "base"/"peak"
# 0: max, 1: single_thread, other: other
THREADS = args.threads
ignore_error = args.loose
print_cmd_only = args.print_cmd_only

# prefix config
# cmd_prefix = "/home/lxy/instrument/pin-3.24/pin -t /home/lxy/instrument/x86_indirect_branch_analysis/TraceInsImm/obj-intel64/TraceInsImm.so -o %s -- "
# cmd_prefix = "/home/lxy/bt/qemu-6.2.0/build/qemu-x86_64 "
# cmd_prefix = "taskset -c " + cpu + " perf stat -o %s "
# cmd_prefix = "taskset -c 8 perf stat -e cycles,instructions,L1-dcache-loads,L1-dcache-load-misses,r2012,dTLB-load-misses -o %s "
# cmd_prefix = "/bin/qemu-aarch64 -plugin /home/lxy/bt/qemu-plugins_cpp/libbbv.so -d plugin -D %s "
cmd_prefix = args.cmd_prefix

title = args.title
log_dir_prefix = args.log_dir_prefix

#spec cpu diectory
SPEC2000_DIR = os.path.abspath(args.dir00)
SPEC2006_DIR = os.path.abspath(args.dir06)
SPEC2006_EXT = args.ext06
SPEC2017_DIR = os.path.abspath(args.dir17)
SPEC2017_EXT = args.ext17

log_dir = "%s/%s_%s_%s_%s" % (log_dir_prefix, title, SPEC, SIZE, datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))

print("log dir is %s" % log_dir)

# DO NOT EDIT FOLLOWING
os.makedirs(log_dir, exist_ok=True)

if not THREADS:
    # do not eat all the threads
    THREADS = (os.cpu_count() - 4) // 2

if SPEC == "2000":
    # AAAAA
    base_dir = SPEC2000_DIR+ "/benchspec"
    sub_dir = {"test": "run/00000001", "train":"run/00000002", "ref":"run/00000003"}[SIZE]

    speccmd_ignore_prefix = ["-u"]
    CINT = ["164.gzip", "175.vpr", "176.gcc", "181.mcf", "186.crafty", "197.parser", "252.eon", "253.perlbmk", "254.gap", "255.vortex", "256.bzip2", "300.twolf"]
    CFP = ["168.wupwise", "171.swim", "172.mgrid", "173.applu", "177.mesa", "178.galgel", "179.art", "183.equake", "187.facerec", "188.ammp", "189.lucas", "191.fma3d", "200.sixtrack", "301.apsi"]
elif SPEC == "2006":
    # AAAAA
    base_dir = SPEC2006_DIR + "/benchspec/CPU2006"
    sub_dir = "run/run_base_%s_%s.0000" % (SIZE, SPEC2006_EXT)

    speccmd_ignore_prefix = ["-C"]
    CINT = ["400.perlbench", "401.bzip2", "403.gcc", "429.mcf", "445.gobmk", "456.hmmer", "458.sjeng", "462.libquantum", "464.h264ref", "471.omnetpp", "473.astar", "483.xalancbmk"]
    CFP = ["410.bwaves", "416.gamess", "433.milc", "434.zeusmp", "435.gromacs", "436.cactusADM", "437.leslie3d", "444.namd", "447.dealII", "450.soplex", "453.povray", "454.calculix", "459.GemsFDTD", "465.tonto", "470.lbm", "481.wrf", "482.sphinx3"]
elif SPEC == "2017":
    # AAAAA
    SIZE = "refrate" if SIZE == "ref" else SIZE
    base_dir = SPEC2017_DIR + "/benchspec/CPU"
    sub_dir = "run/run_%s_%s_%s.0000" % (TUNE, SIZE, SPEC2017_EXT)

    speccmd_ignore_prefix = ["-E", "-r", "-N C", "-C"]
    CINT = ["500.perlbench_r", "502.gcc_r", "505.mcf_r", "520.omnetpp_r", "523.xalancbmk_r", "525.x264_r", "531.deepsjeng_r", "541.leela_r", "548.exchange2_r", "557.xz_r"]
    CFP = ["503.bwaves_r", "507.cactuBSSN_r", "508.namd_r", "510.parest_r", "511.povray_r", "519.lbm_r", "521.wrf_r", "526.blender_r", "527.cam4_r", "538.imagick_r", "544.nab_r", "549.fotonik3d_r", "554.roms_r"]
else:
    print(f"{SPEC} not exsited")
    exit(1)

# if "perf" in cmd_prefix or "pin" in cmd_prefix:
#     cmd = (cmd_prefix % ("/dev/null")) + " /bin/ls 1>/dev/null 2>/dev/null"
#     if os.system(cmd):
#         print("can not run prefix")
#         print(cmd)
#         exit(1)

if not os.path.exists(base_dir) :
    print(f"{base_dir} not existed")
    exit(1)

score_file = open(log_dir + ".csv", "w")

def get_reftime(reftime_filename, benchmark):
    f = open(reftime_filename)
    if SPEC == "2000" and SIZE == "test" and benchmark == "172.mgrid" :
        return 1.0
    first_line = f.readlines()[0 if SPEC == "2017" else 1].strip().split()
    if SPEC == "2017" and SIZE == "refrate":
        assert first_line[0] == "refrate"
    reftime = float(first_line[-1])
    f.close()
    return reftime

def get_command(benchmark, speccmds_filename):
    f = open(speccmds_filename)
    lines = f.readlines()
    f.close()
    cmds = []
    index = 0
    for line in lines:
        ignore = False
        for prefix in speccmd_ignore_prefix:
            if line.startswith(prefix):
                ignore = True
                break
        if ignore:
            continue
        index += 1
        args = line[:-1].split(" ")
        # print(args)
        i = 0
        stdin = ""
        stdout = ""
        stderr = ""
        while i < len(args) :
            if args[i] == "-i":
                stdin = args[i + 1]
                i += 1
            elif args[i] == "-o":
                stdout = args[i + 1]
                i += 1
            elif args[i] == "-e":
                stderr = args[i + 1]
                i += 1
            else :
                break
            i += 1
        cmd = " ".join(args[i:])
        if SPEC == "2017":
            for i in range(0, len(cmd)):
                # 2017 append < in > stdout 2>> stderr at end of command
                if cmd[i] in ['>', '<', '2>>'] :
                    cmd = cmd[:i]
                    break
        # print(stdin, stdout, stderr, cmd)
        if "%s" in cmd_prefix:
            cmd_full_prefix = cmd_prefix % (log_dir + "/" + benchmark + str(index))
        elif not cmd_prefix :
            cmd_full_prefix = ""
        else :
            cmd_full_prefix = cmd_prefix + " "
        cmd = " ".join([cmd_full_prefix, cmd, ("<"+stdin) if stdin else "", ("1>" +stdout) if stdout else "", ("2>" + stderr) if stderr else ""])
        cmds.append(cmd)
    # print(cmds)
    return cmds

def run_single(benchmark, get_cmd_only=False):
    DIR_PREFIX = ""
    if SPEC == "2000" :
        DIR_PREFIX = 'CINT2000' if benchmark in CINT else 'CFP2000'
    work_dir = os.path.join(base_dir, DIR_PREFIX,  benchmark, sub_dir)
    if not os.path.exists(work_dir):
        print(f"{work_dir} not existed")
        exit(1)
    cmds = get_command(benchmark, os.path.join(work_dir, "speccmds.cmd"))
    if get_cmd_only :
        return ["cd %s && %s" % (work_dir, cmd) for cmd in cmds]

    reftime = get_reftime(os.path.join(base_dir, DIR_PREFIX, benchmark, "data/%s/reftime" % (SIZE)), benchmark)
    os.chdir(work_dir)
    begin = time.time()
    for cmd in cmds:
        if print_cmd_only:
            print("cd %s && %s" % (work_dir, cmd))

        if not print_cmd_only:
            r = os.system(cmd)
            if r:
                print("error %s, return value:%d" % (benchmark, r))
                print("work_dir %s" % (work_dir))
                print("cmd %s" % (cmd))
                if not ignore_error :
                    exit(r)
    end = time.time()
    runtime = end - begin
    return reftime, runtime, reftime / runtime

def cd_exec(work_dir, cmd):
    os.chdir(work_dir)
    return os.system(cmd)

def RUN(benchmarks):
    scores = []
    for benchmark in benchmarks:
        reftime, runtime, ratio = run_single(benchmark)
        if not print_cmd_only:
            print("%20s\t%.1f\t%.3f\t%.3f" % (benchmark, reftime, runtime, ratio))
            score_file.write('%s,%f,%f,%f\n' % (benchmark, reftime, runtime, ratio))
        scores.append(ratio)
    if not print_cmd_only:
        geo_mean = reduce(lambda x, y: x*y, scores)**(1.0/len(scores))
        print("score : %.3f" % geo_mean)
        score_file.write("score,,,%s\n" % geo_mean)


# def RUN_MT(benchmarks):
#     scores = []
#     with Pool(THREADS) as p:
#         r = p.map(run_single, benchmarks)
#         for index in range(len(benchmarks)):
#             reftime, runtime, ratio = r[index]
#             if not print_cmd_only:
#                 print("%20s\t%.1f\t%.3f\t%.3f" % (benchmarks[index], reftime, runtime, ratio))
#             scores.append(ratio)
#     if not print_cmd_only:
#         print("score : %.3f" % reduce(lambda x, y: x*y, scores)**(1.0/len(scores)))

def RUN_MT2(benchmarks):
    cmds = []
    for i in benchmarks:
        cmds += run_single(i, True)
    with Pool(THREADS) as p:
        r = p.map(os.system, cmds)
        for index in range(len(cmds)):
            print("FAIL:", end='') if r[index] else print("SUCCESS:", end='')
            print(cmds[index].split("&&")[1])

if not print_cmd_only:
    print("begin : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def canonical_list(raw_name, canonical_name):
    r = []
    for raw in raw_name:
        for item in canonical_name:
            if raw in item:
                r.append(item)
    return r

benchmark = args.benchmark.split(",")
b_int = canonical_list(benchmark, CINT)
b_fp = canonical_list(benchmark, CFP)

if THREADS == 1:
    if "int" in benchmark or "all" in benchmark:
        RUN(CINT)
    if "fp" in benchmark or "all" in benchmark:
        RUN(CFP)
    if b_int:
        RUN(b_int)
    if b_fp:
        RUN(b_fp)
else:
    if "int" in benchmark:
        RUN_MT2(CINT)
    if "fp" in benchmark:
        RUN_MT2(CFP)
    if "all" in benchmark:
        RUN_MT2(CINT + CFP)

if not print_cmd_only:
    print("end   : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

score_file.close()
