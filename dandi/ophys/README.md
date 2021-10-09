# Two Photon Data -> Dandi Example

Demonstrates how to create 2p NWB formatted data, and then run
[Suite2p](https://github.com/MouseLand/suite2p) analysis to generate
processed data in NWB format.

This uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage
python virtual environments.

```sh
# Enter virtual environment
pipenv shell
pipenv install # Only needed once, to install required packages.

# Create test NWB data file.
# NOTE: suite2p NWB-input only supports single-plane recordings, so this
#       data only contains a single plane.
python create_2p_data.py

# Run suite2p with NWB output.
# NOTE: this script adds a missing `Subject` object in the Suite2p output.
python run_suite2p.py
```

Now use the [Dandi instructions](../README.md) to upload.
