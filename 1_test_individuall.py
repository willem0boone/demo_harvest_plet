from datetime import date


start = date(2010, 1, 1)
end = date(2021, 1, 1)
wkt_polygon = "POLYGON ((-180 -90,-180 90,180 90,180 -90,-180 -90))"
dataset = "BE Flanders Marine Institute (VLIZ) - LW_VLIZ_zoo"

from harvest_plet.harvest_dataset import harvest_dataset
csv_data = harvest_dataset(start, end, wkt_polygon, dataset)
print(csv_data)

from harvest_plet.harvest_dataset import harvest_as_csv
from pathlib import Path
my_dir = Path.cwd() / "temp"

harvest_as_csv(start, end, wkt_polygon, dataset, out_dir=my_dir)
