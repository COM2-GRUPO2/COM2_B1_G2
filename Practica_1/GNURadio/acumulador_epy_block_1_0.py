import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):  # Solo argumentos por defecto aquí
        gr.sync_block.__init__(
            self,
            name="e_Diff",  # Aparecerá en GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acum_anterior = 0  # Estado interno para acumulación

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]  # Señal de salida diferenciada
        
        diff = np.diff(np.insert(x, 0, self.acum_anterior))
        self.acum_anterior = x[-1]  # Guardar último valor para la siguiente iteración
        
        y0[:len(diff)] = diff  # Copiar resultado a la salida
        return len(diff)


