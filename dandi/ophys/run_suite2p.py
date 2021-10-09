import os
import warnings

import numba
import suite2p
from pynwb.file import Subject

warnings.filterwarnings("ignore", category=numba.NumbaPendingDeprecationWarning)

params = {
    "nwb_file": "2p_raw_data.nwb",
    "nwb_series": "MySeries",
    "save_NWB": "save_NWB",
    "data_path": "Why must I include this variable?",
}

suite2p.run_s2p(params)

# Copy over Subject from original file.  Dandi datasets required a subject_id,
# but Suite2p does not copy over Subject from the input NWB file.  This is
# a bit of a hack.

from pynwb import NWBHDF5IO

in_path = params["nwb_file"]
out_path = os.path.join("suite2p", "ophys.nwb")

with NWBHDF5IO(in_path, "r") as in_io, NWBHDF5IO(out_path, "a") as out_io:
    out_file = out_io.read()
    subject = in_io.read().subject

    subject_fields = subject.__dict__["_AbstractContainer__field_values"]
    out_file.subject = Subject(**subject_fields)

    out_io.write(out_file)
