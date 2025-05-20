from harvest_plet.harvest_all import harvest_all_datasets

from pathlib import Path
my_dir = Path.cwd() / "temp"

results, failures = harvest_all_datasets(out_dir=my_dir)


