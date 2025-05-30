import harvest_plet
from harvest_plet import ospar_comp

print(help(harvest_plet))
print(harvest_plet.__version__)

comp_regions = ospar_comp.OSPARRegions()

# test id retrieval
id_list = comp_regions.get_all_ids()

for item in id_list:
    print(item)

# individual COMP area plot
comp_regions.plot_map("SNS")

# plot all COMP areas
comp_regions.plot_map()

# test WKT
my_wkt = comp_regions.get_wkt("SNS")
print(my_wkt)
