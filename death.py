import matplotlib.pyplot as plt
from matplotlib.pyplot import legend, xlim
from numpy.core.fromnumeric import sort
from numpy.lib.shape_base import column_stack
import pandas as pd
import numpy as np

df = pd.read_csv("month.csv", delimiter=";", index_col=("alter", "jahr"), header=0)
# [2016, 1017, 2018, 2019]
print(df)
df = df.loc[
    ("Insgesamt", [2016, 2017, 2018, 2019]),
    (
        "Januar",
        "Februar",
        "Marz",
        "April",
        "Mai",
        "Juni",
        "Juli",
        "August",
        "September",
        "Oktober",
        "November",
        "Dezember",
    ),
]

print(df)
df.plot(kind="bar", legend=None, ylim=(60000, 110000))
plt.savefig("test.png")
