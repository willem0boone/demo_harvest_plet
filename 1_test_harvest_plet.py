from harvest_plet.plet import PLETHarvester

plet_harvester = PLETHarvester()

# test dateset names
dataset_names = plet_harvester.get_dataset_names()

print(dataset_names)

from harvest_plet.ospar_comp import OSPARRegions
ospart_regions = OSPARRegions()
wkt_sns = ospart_regions.get_wkt('SNS', simplify=True)

from datetime import date
start_date = date(2017, 1, 1)
end_date = date(2020, 1, 1)

harvest = plet_harvester.harvest_dataset(
    start_date=start_date,
    end_date=end_date,
    wkt=wkt_sns,
    dataset_name="BE Flanders Marine Institute (VLIZ) - LW_VLIZ_phyto")


print(harvest)

