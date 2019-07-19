from __future__ import print_function, division
import time
from nilmtk import DataSet, TimeFrame, MeterGroup, HDFDataStore


def get_disaggregation(device, total_aggregate):
    devices = ["fridge", "air conditioner", "washing machine"]
    if device not in devices:
        return None

    test = DataSet('iawe.h5')
    test_elec = test.buildings[1].elec
    test_mains = test_elec.mains().all_meters()[0]
    test_meter = test_elec.submeters()[device]

    df = next(test_meter.load(ac_type='active', sample_period=2592000))
    prediction = df['power'].values[0]

    print(df.head()	)
    return prediction
