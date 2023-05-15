#!/bin/bash -x
DIR17=$(realpath .)
cd ${DIR17}/benchspec/CPU/500.perlbench_r/run/run_base_test_${EXT17}.0000 &&  ./perlbench_r_base.${EXT17} -I. -I./lib makerand.pl   1>makerand.out 2>makerand.err
cd ${DIR17}/benchspec/CPU/500.perlbench_r/run/run_base_test_${EXT17}.0000 &&  ./perlbench_r_base.${EXT17} -I. -I./lib test.pl   1>test.out 2>test.err
cd ${DIR17}/benchspec/CPU/502.gcc_r/run/run_base_test_${EXT17}.0000       &&  ./cpugcc_r_base.${EXT17} t1.c -O3 -finline-limit=50000 -o t1.opts-O3_-finline-limit_50000.s   1>t1.opts-O3_-finline-limit_50000.out 2>t1.opts-O3_-finline-limit_50000.err
cd ${DIR17}/benchspec/CPU/505.mcf_r/run/run_base_test_${EXT17}.0000       &&  ./mcf_r_base.${EXT17} inp.in    1>inp.out 2>inp.err
cd ${DIR17}/benchspec/CPU/520.omnetpp_r/run/run_base_test_${EXT17}.0000   &&  ./omnetpp_r_base.${EXT17} -c General -r 0   1>omnetpp.General-0.out 2>omnetpp.General-0.err
cd ${DIR17}/benchspec/CPU/523.xalancbmk_r/run/run_base_test_${EXT17}.0000 &&  ./cpuxalan_r_base.${EXT17} -v test.xml xalanc.xsl   1>test-test.out 2>test-test.err
cd ${DIR17}/benchspec/CPU/525.x264_r/run/run_base_test_${EXT17}.0000      &&  ./x264_r_base.${EXT17} --dumpyuv 50 --frames 156 -o BuckBunny_New.264 BuckBunny.yuv 1280x720   1>run_000-156_x264_r_base.mytest-m64_x264.out 2>run_000-156_x264_r_base.mytest-m64_x264.err
cd ${DIR17}/benchspec/CPU/531.deepsjeng_r/run/run_base_test_${EXT17}.0000 &&  ./deepsjeng_r_base.${EXT17} test.txt   1>test.out 2>test.err
cd ${DIR17}/benchspec/CPU/541.leela_r/run/run_base_test_${EXT17}.0000     &&  ./leela_r_base.${EXT17} test.sgf   1>test.out 2>test.err
cd ${DIR17}/benchspec/CPU/548.exchange2_r/run/run_base_test_${EXT17}.0000 &&  ./exchange2_r_base.${EXT17} 0   1>exchange2.txt 2>exchange2.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 4 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1548636 1555348 0   1>cpu2006docs.tar-4-0.out 2>cpu2006docs.tar-4-0.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 4 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1462248 -1 1   1>cpu2006docs.tar-4-1.out 2>cpu2006docs.tar-4-1.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 4 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1428548 -1 2   1>cpu2006docs.tar-4-2.out 2>cpu2006docs.tar-4-2.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 4 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1034828 -1 3e   1>cpu2006docs.tar-4-3e.out 2>cpu2006docs.tar-4-3e.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 4 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1061968 -1 4   1>cpu2006docs.tar-4-4.out 2>cpu2006docs.tar-4-4.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 4 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 1034588 -1 4e   1>cpu2006docs.tar-4-4e.out 2>cpu2006docs.tar-4-4e.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 1 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 650156 -1 0   1>cpu2006docs.tar-1-0.out 2>cpu2006docs.tar-1-0.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 1 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 639996 -1 1   1>cpu2006docs.tar-1-1.out 2>cpu2006docs.tar-1-1.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 1 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 637616 -1 2   1>cpu2006docs.tar-1-2.out 2>cpu2006docs.tar-1-2.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 1 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 628996 -1 3e   1>cpu2006docs.tar-1-3e.out 2>cpu2006docs.tar-1-3e.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 1 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 631912 -1 4   1>cpu2006docs.tar-1-4.out 2>cpu2006docs.tar-1-4.err
cd ${DIR17}/benchspec/CPU/557.xz_r/run/run_base_test_${EXT17}.0000        &&  ./xz_r_base.${EXT17} cpu2006docs.tar.xz 1 055ce243071129412e9dd0b3b69a21654033a9b723d874b2015c774fac1553d9713be561ca86f74e4f16f22e664fc17a79f30caa5ad2c04fbc447549c2810fae 629064 -1 4e   1>cpu2006docs.tar-1-4e.out 2>cpu2006docs.tar-1-4e.err
cd ${DIR17}/benchspec/CPU/503.bwaves_r/run/run_base_test_${EXT17}.0000    &&  ./bwaves_r_base.${EXT17} bwaves_1  <bwaves_1.in 1>bwaves_1.out 2>bwaves_1.err
cd ${DIR17}/benchspec/CPU/503.bwaves_r/run/run_base_test_${EXT17}.0000    &&  ./bwaves_r_base.${EXT17} bwaves_2  <bwaves_2.in 1>bwaves_2.out 2>bwaves_2.err
cd ${DIR17}/benchspec/CPU/507.cactuBSSN_r/run/run_base_test_${EXT17}.0000 &&  ./cactusBSSN_r_base.${EXT17} spec_test.par     1>spec_test.out 2>spec_test.err
cd ${DIR17}/benchspec/CPU/508.namd_r/run/run_base_test_${EXT17}.0000      &&  ./namd_r_base.${EXT17} --input apoa1.input --iterations 1 --output apoa1.test.output   1>namd.out 2>namd.err
cd ${DIR17}/benchspec/CPU/510.parest_r/run/run_base_test_${EXT17}.0000    &&  ./parest_r_base.${EXT17} test.prm   1>test.out 2>test.err
cd ${DIR17}/benchspec/CPU/511.povray_r/run/run_base_test_${EXT17}.0000    &&  ./povray_r_base.${EXT17} SPEC-benchmark-test.ini   1>SPEC-benchmark-test.stdout 2>SPEC-benchmark-test.stderr
cd ${DIR17}/benchspec/CPU/519.lbm_r/run/run_base_test_${EXT17}.0000       &&  ./lbm_r_base.${EXT17} 20 reference.dat 0 1 100_100_130_cf_a.of   1>lbm.out 2>lbm.err
cd ${DIR17}/benchspec/CPU/521.wrf_r/run/run_base_test_${EXT17}.0000       &&  ./wrf_r_base.${EXT17}   1>rsl.out.0000 2>wrf.err
cd ${DIR17}/benchspec/CPU/526.blender_r/run/run_base_test_${EXT17}.0000   &&  ./blender_r_base.${EXT17} cube.blend --render-output cube_ --threads 1 -b -F RAWTGA -s 1 -e 1 -a   1>cube.1.spec.out 2>cube.1.spec.err
cd ${DIR17}/benchspec/CPU/527.cam4_r/run/run_base_test_${EXT17}.0000      &&  ./cam4_r_base.${EXT17}   1>cam4_r_base.mytest-m64.txt 2>cam4_r_base.mytest-m64.err
cd ${DIR17}/benchspec/CPU/538.imagick_r/run/run_base_test_${EXT17}.0000   &&  ./imagick_r_base.${EXT17} -limit disk 0 test_input.tga -shear 25 -resize 640x480 -negate -alpha Off test_output.tga   1>test_convert.out 2>test_convert.err
cd ${DIR17}/benchspec/CPU/544.nab_r/run/run_base_test_${EXT17}.0000       &&  ./nab_r_base.${EXT17} hkrdenq 1930344093 1000   1>hkrdenq.out 2>hkrdenq.err
cd ${DIR17}/benchspec/CPU/549.fotonik3d_r/run/run_base_test_${EXT17}.0000 &&  ./fotonik3d_r_base.${EXT17}   1>fotonik3d_r.log 2>fotonik3d_r.err
cd ${DIR17}/benchspec/CPU/554.roms_r/run/run_base_test_${EXT17}.0000      &&  ./roms_r_base.${EXT17}  <ocean_benchmark0.in.x 1>ocean_benchmark0.log 2>ocean_benchmark0.err