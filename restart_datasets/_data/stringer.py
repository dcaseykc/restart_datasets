import os
import json
import pandas as pd

if __name__ == '__main__':
    files = os.listdir()

    datasets = {}
    dataset_info = {}
    local_datasets = {}
    stringy = ""
    for f in files:
        name = f.split('.')
        try:
            stringy += f"class {name[0]}(Dataset):\n  name = '{f}'\n  _pd_read_kwds = {{}}\n\n"
        except SyntaxError:
            pass

        # write to datasets.json
        datasets[name[0]] = []
        datasets[name[0]].append({
            "filename": f,
            "format": name[1]
        })

        # write to dataset_info.json
        dataset_info[name[0]] = []
        dataset_info[name[0]].append({
            "description": f"OES data for {name[0]}"
        })

        local_datasets[f"{name[0]}"] = f"_data/{f}"

"""
with open('datasets.json', 'w') as outfile:
    json.dump(datasets, outfile)

with open('dataset_info.json', 'w') as outfile:
    json.dump(dataset_info, outfile)
with open('local_datasets.json', 'w') as outfile:
    json.dump(local_datasets, outfile)
"""

with open('classes.txt', 'w') as outfile:
    outfile.write(stringy)
