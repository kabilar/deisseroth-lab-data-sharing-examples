"""An example file showing how to store 2p data in NWB format."""
from datetime import datetime
import tifffile

from dateutil.tz import tzlocal
from pynwb import NWBHDF5IO, NWBFile
from pynwb.file import Subject
from pynwb.ophys import OpticalChannel, TwoPhotonSeries

data = tifffile.imread(
    "/oak/stanford/groups/deissero/demos/data_sharing/2p/slm-001/slm-001_Cycle00001_Ch3_000001.ome.fixed.tif"
)
# Read demo data into single-plane, since Suite2p only supports single-plane NWB-input.
# Also truncate since this is just for demonstration purposes.
data = data[:1000, 0]

subject = Subject(subject_id="8675309")

nwbfile = NWBFile(
    session_description="my first synthetic recording",
    identifier="foo-bar",
    session_start_time=datetime.now(tzlocal()),
    subject=subject,
    experimenter="bilbo",
    lab="Deisseroth",
    institution="Stanford University",
    experiment_description="Test of dandi upload.",
    session_id="2000-01-01 00:00:00",
)

device = nwbfile.create_device(
    name="Microscope",
    description="My two-photon microscope",
    manufacturer="The best microscope manufacturer",
)
optical_channel = OpticalChannel(
    name="OpticalChannel", description="an optical channel", emission_lambda=500.0
)
imaging_plane = nwbfile.create_imaging_plane(
    name="ImagingPlane",
    description="a very interesting part of the brain",
    optical_channel=optical_channel,
    device=device,
    excitation_lambda=600.0,
    indicator="GFP",
    location="V1",
)

image_series = TwoPhotonSeries(
    name="MySeries", data=data, imaging_plane=imaging_plane, rate=10.0, unit="raw"
)

nwbfile.add_acquisition(image_series)

with NWBHDF5IO("2p_raw_data.nwb", "w") as io:
    io.write(nwbfile)
