import fs
import numpy as np
def gen_chunk_section(seed, chunk_x, section_y, chunk_z):
    out = []
    rand_gen = np.random.RandomState(seed)
    for x in range(16):
        for y in range(0,5):
            for z in range(16):
                if(rand_gen.randint(0, 8)>=y):
                    out += [[x,y,z]]
    return out
def to_obj_string(arr):
    out = ""
    for e in arr:
        out += f"v {e[0]} {e[1]} {e[2]}\n"

        out += f"v {e[0]+1} {e[1]} {e[2]}\n"

        out += f"v {e[0]} {e[1]+1} {e[2]}\n"

        out += f"v {e[0]} {e[1]} {e[2]+1}\n"

        out += f"v {e[0]+1} {e[1]+1} {e[2]}\n"

        out += f"v {e[0]} {e[1]+1} {e[2]+1}\n"

        out += f"v {e[0]+1} {e[1]} {e[2]+1}\n"

        out += f"v {e[0]+1} {e[1]+1} {e[2]+1}\n"

    for f in range(len(arr)):
        e = f*8+1
        out += f"f {e} {e+1} {e+6} {e+3}\n"
        out += f"f {e} {e+1} {e+4} {e+2}\n"
        # out += f"f {e+3} {e+6} {e+7} {e+5}\n"
        # out += f"f {} {} {} {}\n"
        # out += f"f {} {} {} {}\n"
        # out += f"f {} {} {} {}\n"
    return out
from fs.osfs import OSFS
home_fs = OSFS("")
home_fs.writetext('out.obj', to_obj_string(gen_chunk_section(1, 0, 0, 0)))
home_fs.close()
print(len(gen_chunk_section(1, 0, 0, 0)))
