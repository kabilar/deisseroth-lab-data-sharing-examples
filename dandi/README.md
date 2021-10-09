# Dandi Archive

According to the [Dandi website](https://www.dandiarchive.org/), Dandi is a data repository
geared toward
_data from electrophysiology, optophysiology, and behavioral time-series,
and images from immunostaining experiments_.

The easiest and recommended way to upload data is to have your data available in the
[Neurodata Without Borders](https://www.nwb.org/) format. This is typically one or
more HDF5 files with data stored in a particular "NWB" configuration, usually with
a `.nwb` suffix to indicate the internal format. There are
both [python libraries](https://pynwb.readthedocs.io/en/stable/) and
[Matlab libraries](https://neurodatawithoutborders.github.io/matnwb/tutorials/html/intro.html).

With your data in NWB format, upload Dandi Archive is occurs in

1. Create an account on the DANDI website. Your account is given an API key that you will
   use to upload data.
1. Install the dandi python package.
1. Create a new dandiset on the website. At this point there is no data -- the dandiset
   initially contains some basic metadata.
1. Validate your data. This is imporant because Dandi will require certain metadata
   to be present in your NWB files, which you may not have initially included. For instance,
   Dandi requires a `subject_id` field for each dataset. Unfortunately, if you are using Suite2p,
   to analyze two-photon data, it's output does _not_ include this field and you will have to
   add this field prior to uploading.
1. Prepare a dataset for upload, which basically means it is duplicated from your data directory
   to a special directory with new names.
1. Upload your data. If the above steps are complete, this step should be straightforward.

These steps can be found in the
[create an account](https://www.dandiarchive.org/handbook/10_using_dandi/#create-an-account-on-dandi) and
[upload a dataset](https://www.dandiarchive.org/handbook/10_using_dandi/#uploading-a-dandiset)
sections of the Dandi handbook.

The final 3 steps are not formatted correctly in the handbook. The appropriate code to perform the prepration
and upload are below, where you subsitute the 6-digit `dataset_id` in the appropriate places:

```bash
# Validate data directory.
cd <source_folder>
dandi validate

# Initialize a new directory for this dandiset.
cd <dandi_folder>
dandi download https://dandiarchive.org/dandiset/<dataset_id>/draft

# Copy over your data in DANDI format.
cd <dataset_id>
dandi organize <source_folder> -f dry  # Do a dry-run to make sure there are no errors
dandi organize <source_folder>
dandi upload
```
