from __future__ import print_function, division
import time

# from matplotlib import rcParams
# import matplotlib.pyplot as plt

from nilmtk import DataSet, TimeFrame, MeterGroup, HDFDataStore
from .shortseq2pointdisaggregator import ShortSeq2PointDisaggregator

from datetime import datetime
import h5py
import tables
import numpy as np


def get_disaggregation(device, total_aggregate):

	here = os.path.dirname(os.path.abspath(__file__))
    dataset_file = os.path.join(here, "dataset/iawe2.h5")


    devices = ["fridge", "air conditioner", "washing machine"]
    if device not in devices:
        return None

    total_seconds = 30*24*60*60
    val_per_second = float(total_aggregate)/total_seconds

    start = 0
    end = 0

    with h5py.File(dataset_file, "r+") as f1:
        table = f1["building1/elec/meter1/table"].value

        start = int(str(table[0][0])[:10])
        end = int(str(table[total_seconds-1][0])[:10])
        print(start, end)

        # for i in range(total_seconds):
        # 	for j in range(7):
        # 		print("Progress {:2.1%}".format(i / total_seconds), end="\r")
        # 		table[i][1][j] = val_per_second + np.random.uniform(-1e-17,
        #  1e-17, 1)

        # f1["building1/elec/meter1/table"][...] = table

    start = datetime.fromtimestamp(start)
    end = datetime.fromtimestamp(end)

    start = start.isoformat(' ', 'seconds')
    end = end.isoformat(' ', 'seconds')

    test = DataSet(dataset_file)
    test.set_window(start=start, end=end)
    test_elec = test.buildings[1].elec
    test_mains = test_elec.mains()[1]
    test_meter = test_elec.submeters()[device]

    disag_filename = 'disag-out.h5'  # The filename of the resulting datastore
    output = HDFDataStore(disag_filename, 'w')

    disaggregator = ShortSeq2PointDisaggregator()
    model_file = os.path.join(here,"disag15/IAWE-RNN-h{}-{}-{}epochs.h5".format(1, device,10))
    disaggregator.import_model(model_file)

    # anykey = input()
    # test_mains: The aggregated signal meter
    # output: The output datastore
    # train_meter: This is used in order to copy the metadata of the train
    # meter into the datastore
    disaggregator.disaggregate(test_mains, output, test_meter, sample_period=1)
    output.close()

    result = DataSet(disag_filename)
    res_elec = result.buildings[1].elec

    prediction = res_elec[device]

    return prediction
