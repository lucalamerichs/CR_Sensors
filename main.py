from construction_site import ConstructionSite

# ConstructionSite('2021-04-03').progressAt('2021-04-13') -> [datetime.datetime<2021, 4, 3>, datetime.datetime<2021, 4, 4>, ..., datetime.datetime<2021, 4, 13>]
print(ConstructionSite('2021-04-04').progressAt('2021-04-13'))