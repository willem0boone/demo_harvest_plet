import harvest_plet
from harvest_plet import list_datasets

print(harvest_plet.__version__)

datasets = list_datasets.get_dataset_names()
for i, name in enumerate(datasets):
    print(i, name)

