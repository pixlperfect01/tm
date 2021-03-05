import anvil
import numpy as np
import time
stone = anvil.Block("minecraft", "stone")
bedrock = anvil.Block("minecraft", "bedrock")
def generate_chunk(seed: int, dimension: str, chunk_x: int, chunk_z: int):
    chunk = anvil.EmptyRegion(chunk_x, chunk_z)
    

    rand_gen = np.random.RandomState(seed)
    for x in range(16):
        for z in range(16):
            chunk.set_block(bedrock, x, 0, z)
    for x in range(16):
        for z in range(16):
            if not rand_gen.randint(0,8)<1:
                chunk.set_block(bedrock, x, 1, z)
    for x in range(16):
        for z in range(16):
            if not rand_gen.randint(0,8)<2:
                chunk.set_block(bedrock, x, 2, z)
    for x in range(16):
        for z in range(16):
            if not rand_gen.randint(0,8)<3:
                chunk.set_block(bedrock, x, 3, z)
    for x in range(16):
        for z in range(16):
            if not rand_gen.randint(0,8)<4:
                chunk.set_block(bedrock, x, 4, z)

    return chunk
generate_chunk(100, "", 0, 0).save("r.0.0.mca")