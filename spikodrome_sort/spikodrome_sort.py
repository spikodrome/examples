#!/usr/bin/env python

import os
import sys
import argparse
import time
import ephys_viz as ev
import kachery as ka
import spiketoolkit as st
import spikesorters as ss

def main():
    parser = argparse.ArgumentParser(description='Run spike sorting.')
    parser.add_argument('recording_path', help='Path (or kachery-path) to the file or directory defining the sorting')
    parser.add_argument('--output', help='The output directory', required=True)

    args = parser.parse_args()
    recording_path = args.recording_path
    output_dir = args.output

    ka.set_config(fr='default_readonly')

    recording = ev.AutoRecordingExtractor(dict(path=recording_path), download=True)

    # Preprocessing
    recording = st.preprocessing.bandpass_filter(recording, freq_min=300, freq_max=6000)
    recording = st.preprocessing.common_reference(recording, reference='median')

    # Sorting
    sorting_ms4 = ss.run_mountainsort4(recording, delete_output_folder=True)

    print(recording.get_num_channels())

if __name__ == "__main__":
    main()
