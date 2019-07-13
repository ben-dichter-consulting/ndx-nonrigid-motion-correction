import numpy as np
from datetime import datetime

from ndx_nonrigid_motion_correction import NonrigidMotionCorrection

from pynwb import NWBHDF5IO, NWBFile

print(NonrigidMotionCorrection.__init__.__doc__)

nmc = NonrigidMotionCorrection(name='demo', data=np.ones((3, 3)), pixel_map=np.ones((3, 3), dtype='int'),
                               interpolation_type='local interpolation', spatial_dimensions=[4, 4, 4],
                               nblocks=10)

session_start_time = datetime.now().astimezone()
nwb = NWBFile('session_description', 'identifier', session_start_time)
ophys_mod = nwb.create_processing_module('ophys', 'desc')
ophys_mod.add(nmc)

with NWBHDF5IO('test_motion_correction.nwb', 'w') as io:
    io.write(nwb)

with NWBHDF5IO('test_motion_correction.nwb', 'r') as io:
    io.read()
