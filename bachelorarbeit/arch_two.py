import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    
    to_ConvConvRelu( name='ccr1', s_filer=500, n_filer=(64,64), y="136", offset="(0,0,0)", to="(0,0,0)", width=(4,4), height=48, depth=48),
    to_Pool(name="pool1", offset="(0,0,0)", to="(ccr1-east)", width=1, height=40, depth=40, opacity=0.5),
    
    to_ConvConvRelu( name='ccr2', s_filer=500, n_filer=(64,64), offset="(4,0,0)", to="(pool1-east)", width=(4,4), height=32, depth=32  ),
    to_connection("pool1", "ccr2"),
    to_Pool(name="pool2", offset="(0,0,0)", to="(ccr2-east)", width=1, height=24, depth=24, opacity=0.5),
    
    to_ConvConvRelu( name='ccr3', s_filer=500, n_filer=(64,64), offset="(3,0,0)", to="(pool2-east)", width=(4,4), height=16, depth=16  ),
    to_connection("pool2", "ccr3"),
    to_Pool(name="pool3", offset="(0,0,0)", to="(ccr3-east)", width=1, height=8, depth=8, opacity=0.5),

    to_SoftMax("soft1", 4098, offset="(2,0,0)", to="(pool3-east)", depth=24),
    to_connection("pool3", "soft1"),
    
    to_SoftMax("soft2", 1024, offset="(4,0,0)", to="(pool3-east)", depth=16),
    to_connection("soft1", "soft2"),

    to_SoftMax("soft3", 10, offset="(6,0,0)", to="(pool3-east)", depth=8),
    to_connection("soft2", "soft3"),
    
    to_SoftMax("soft4", 10, offset="(8,0,0)", to="(pool3-east)", depth=8),
    to_connection("soft3", "soft4"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
