import pylab as plt
from blimpy import Waterfall
file_path = 'Voyager1.single_coarse.fine_res.h5'
obs = Waterfall(file_path)
obs.info()
print(obs.header)
obs.plot_waterfall(f_start=8419.2740, f_stop=8419.2750)