import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 128, (16,44), offset="(0,0,0)", to="(0,0,0)", height=44, depth=16, width=2),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=22, depth=8),
    # to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2),
    # to_connection("pool1", "conv2"),
    # to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    # to_SoftMax("soft1", 10, "(3,0,0)", "(pool1-east)", caption="SOFT"),
    # to_connection("pool2", "soft1"),

    to_ConvConvRelu( name='ccr_b1', s_filer=500, n_filer=(64,64), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40  ),
    to_Pool(name="pool_b1", offset="(0,0,0)", to="(ccr_b1-east)", width=1, height=32, depth=32, opacity=0.5),
    
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
