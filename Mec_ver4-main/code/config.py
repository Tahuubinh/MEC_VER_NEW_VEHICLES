import os
from pathlib import Path

LINK_PROJECT = Path(os.path.abspath(__file__))
LINK_PROJECT = LINK_PROJECT.parent.parent
#print(LINK_PROJECT)
DATA_LOCATION = "data_task/data2"
DATA_DIR = os.path.join(LINK_PROJECT, "data")
RESULT_DIR = os.path.join(LINK_PROJECT, "result/result3/")
DATA_TASK = os.path.join(LINK_PROJECT, DATA_LOCATION)
COMPUTATIONAL_CAPACITY_900 = 1 # Ghz
COMPUTATIONAL_CAPACITY_901 = 1.2 # Ghz
COMPUTATIONAL_CAPACITY_902 = 1 # Ghz
COMPUTATIONAL_CAPACITY_903 = 1
COMPUTATIONAL_CAPACITY_904 = 1
COMPUTATIONAL_CAPACITY_905 = 1
COMPUTATIONAL_CAPACITY_906 = 1
COMPUTATIONAL_CAPACITY_907 = 1
COMPUTATIONAL_CAPACITY_LOCAL = 3 # Ghz
CHANNEL_BANDWIDTH = 200 # MHz
List_COMPUTATION = [COMPUTATIONAL_CAPACITY_900, COMPUTATIONAL_CAPACITY_901, COMPUTATIONAL_CAPACITY_902, 
                    COMPUTATIONAL_CAPACITY_903, COMPUTATIONAL_CAPACITY_904, COMPUTATIONAL_CAPACITY_905,
                    COMPUTATIONAL_CAPACITY_906, COMPUTATIONAL_CAPACITY_907, COMPUTATIONAL_CAPACITY_LOCAL]
# Pr = 46 # dBm
Pr = 46
P = 39.810 # mW
SIGMASquare = 100 # dBm   background noise power
PATH_LOSS_EXPONENT = 4  # alpha
NUM_ACTION = 4 # a server + vehicles
NUM_STATE = NUM_ACTION * 2 + 2
SCAILING_CO_EFFICIENT = 1
FILE_NAME = "Not change"
class Config:
    Pr = 46
    Pr2 = 24
    Wm = 10
    length_hidden_layer=4
    n_unit_in_layer=[16, 32, 32, 8]
