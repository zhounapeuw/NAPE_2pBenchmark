# -*- coding: utf-8 -*-

"""

This script does not run any analysis/computations;
rather, here the user will specify each dataset to be analyzed along with
meta information, analysis parameters, and flags that indicate which processing steps to apply

User-defined input
------------------
Use the pre-written template in between the edit lines comment. To add additional files to analyze,
copy and paste the curly brackets (include the brackets!) and the contents within. Add a comma after
previous file's end curly bracket (if not there), and edit the dictionary values in the pasted text.

Here are descriptions of the editable values:

fname : string
    Raw data file name (can be h5, tif, tiff). Include the extension! Take care of if it is a .tif or .tiff!

fdir : string
    Path to the root directory of the raw file. For example: r'C:\Users\my_user\session1'
    NOTE: It is crucial to have the r in front of the string - this will make it a raw string and
        interpret the backslashes as such
    NOTE: there is no need for a last backslash

motion_correct: boolean
    Set to True if SIMA motion correction and bidirectional offset correction is desired; otherwise
    set to False

signal_extract: boolean
    Set to True if you want to perform average signal extraction from imageJ ROIs; otherwise set to False
    IMPORTANT: this step requires an "_mc.sima" folder (from sima motion correction) and imageJ ROI file(s)
        to run

npil_correct: boolean
    Set to True if you want to calculate and correct for each ROI's neuropil signal; Otherwise set to False.
    IMPORTANT: this step requires signal_extract to have been run or it set to True.

Optional Arguments
------------------

max_disp : list of two entries
    Each entry is an int. First entry is the y-axis maximum allowed displacement, second is the x-axis max allowed displacement.
    The number of pixel shift for each line cannot go above these values.
    Note: 50 pixels is approximately 10% of the FOV (512x512 pixels)

    Defaults to [30, 50]

save_displacement : boolean
    Whether or not to have SIMA save the calculated displacements over time. def: False; NOTE: if this is switched to True,
    it can double the time to perform motion correction.

    Defaults to False

fs : int or float
    Sampling rate of the input data

neuropil_radius : int
    This is the radius (in pixels) of the Gaussian weights for neuropil calculation (ie. the larger this value, the more
    of the surrounding space around the ROI will be included in the neuropil estimation
    Default will be 50 pixels

min_neuropil_radius : int
    This is the radius (in pixels) of a deadzone around an ROI that does not get counted towards the neuropil of any ROI.
    Note that this deadzone is applied to every ROI while calculating the neuropil for any ROI, not just the one
    whose neuropil is being calculated.
    Default will be 15 pixels

Output
------

fparams : list of dictionaries

    This is the iterable list of file information and parameters that gets passed to
    the preprocessing pipeline parallelizer function. Each list entry corresponds to a specific
    session.

For the fname, you will have to add the file extension to the string


"""

def define_fparams():
    fparams = {

        # ONLY EDIT LINES BELOW THIS COMMENT

        'general_params': {
            # parameters for stitching bruker ome-tiffs to h5/tiffstack
            'flag_make_h5_tiff': True,
            'save_type': 'h5',
            'number_frames': None,  # optional; number of frames to analyze; defaults to analyzing whole session (None)

            # flags for performing the main sub-analyses
            'flag_bruker_analog': True,  # set to true if analog/voltage input signals are present and are of interest
            'flag_bruker_stim': True,  # set to true if mark points SLM stim was performed

            'analog_names': ['stim', 'frames', 'licks', 'rewards'],
            # variables for plotting TTL pulses
            'flag_validation_plots': False,
            # set to true if want to plot traces of ttl pulses for visualizing and validating
            'valid_plot_channel': 'input_1',  # analog dataframe column names get cleaned up; AI's are "input_#"

            # variables for splitting analog channels encoding multiple conditions
            'flag_multicondition_analog': False,
            'ai_to_split': 2,
            # int, analog port number that contains TTLs of multiple conditions; events here will be split into individual conditions if flag_multicondition_analog is set to true
            'behav_id_of_interest': [101, 102, 103],

            'flag_bruker_stim': True,
            'flag_plot_stim_threshold': True
            # boolean to plot the 2p pixel-avg tseries with threshold for detecting stimmed blank frames
        },

        # Add files to analyze below (and additional file-specific parameters

        'individual_files': [

            {
                'fname': 'vj_ofc_imageactivate_001_20200828-003',
                'fdir': r'D:\bruker_data\vj_ofc_imageactivate_001_20200828\vj_ofc_imageactivate_001_20200828-003'

            },

            {
                'fname': 'vj_ofc_imageactivate_001_2020903-000',
                'fdir': r'D:\bruker_data\vj_ofc_imageactivate_001_20200903\vj_ofc_imageactivate_001_2020903-000',
                # flags for performing the main sub-analyses
                'flag_bruker_analog': False,  # set to true if analog/voltage input signals are present and are of interest
                'flag_bruker_stim': False,  # set to true if mark points SLM stim was performed
            }

            # ONLY EDIT LINES ABOVE THIS COMMENT
        ]
    }

    return fparams
