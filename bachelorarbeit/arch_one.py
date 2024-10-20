import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 369, 16, "136", offset="(0,0,0)", to="(0,0,0)", height=48, depth=48, width=4),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=40,depth=40),

    to_Conv("conv2", 178, 32, offset="(4,0,0)", to="(pool1-east)", height=40, depth=40, width=4),
    to_connection("pool1", "conv2"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=32, depth=32),

    to_Conv("conv3", 74, 64, offset="(3,0,0)", to="(pool2-east)", height=32, depth=32, width=4),
    to_connection("pool2", "conv3"),
    to_Pool("pool3", offset="(0,0,0)", to="(conv3-east)", height=24, depth=24),

    to_Conv("conv4", 32, 128, offset="(2,0,0)", to="(pool3-east)", height=24, depth=24, width=4),
    to_connection("pool3", "conv4"),
    to_Pool("pool4", offset="(0,0,0)", to="(conv4-east)", height=16, depth=16),

    to_SoftMax("soft1", 13340, offset="(2,0,0)", to="(pool4-east)", depth=24),
    to_connection("pool4", "soft1"),
    
    to_SoftMax("soft2", 4096, offset="(4,0,0)", to="(pool4-east)", depth=20),
    to_connection("soft1", "soft2"),

    to_SoftMax("soft3", 1024, offset="(6,0,0)", to="(pool4-east)", depth=16),
    to_connection("soft2", "soft3"),

    to_SoftMax("soft4", 6, offset="(8,0,0)", to="(pool4-east)", depth=12),
    to_connection("soft3", "soft4"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
