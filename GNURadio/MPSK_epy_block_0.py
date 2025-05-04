import numpy as np
from gnuradio import gr

class blk(gr.sync_block):

    def __init__(self, example_param=1.0):  
        gr.sync_block.__init__(
            self,
            name="VCO complex", 
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        self.example_param = example_param

    def work(self, input_items, output_items):
        Q = input_items[0]
        A = input_items[1]
        Sec = output_items[0]
        Sec[:] = A * np.exp(1j * Q)
        return len(Sec)
