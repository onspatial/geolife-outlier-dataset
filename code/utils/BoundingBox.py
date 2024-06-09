import geopandas
import os 

for city in  os.listdir('data/maps'):
    # just directory
    if not os.path.isdir(f'data/maps/{city}'):
        continue
    map = geopandas.read_file(f'data/maps/{city}/map/buildings.shp')
    print(f'{city} bounding box {map.total_bounds}')
    print(f'{city} crs {map.crs}')
    map = map.to_crs(epsg=4326)
    print(f'{city} bounding box {map.total_bounds}')

# atl-metro crs EPSG:26916
# atl-metro bounding box [ 726963.64370556 3726077.56970387  751091.96204231 3752640.96802056]
# atl-metro bounding box [-84.5505285   33.64708314 -84.28945431  33.88663263]

# atl crs EPSG:26916
# atl bounding box [ 739753.1287531  3735138.94979865  744126.37599493 3738988.87861298]
# atl bounding box [-84.41213984  33.72878582 -84.36418537  33.76304255]

# bjng crs EPSG:26916
# bjng bounding box [-1530814.0466859  15287104.43689024 -1485442.08874541 15325111.97593248]
# bjng bounding box [116.1632651  39.7831364 116.6294095  40.039197 ]

# brln crs EPSG:26916
# brln bounding box [ 4910432.5903579  10873249.99566397  4914620.5780151  10877877.13977944]
# brln bounding box [13.3656432 52.5066516 13.4174008 52.5323714]

# gmu crs EPSG:32046
# gmu bounding box [2336457.26610402  424084.05071667 2342158.19053227  427917.38261183]
# gmu bounding box [-77.31851683  38.82516657 -77.29851636  38.83568792]

# nola crs EPSG:26782
# nola bounding box [2398574.84619401  468770.44186372 2407662.59702521  474692.2898364 ]
# nola bounding box [-90.0747321   29.94990921 -90.04599532  29.96606048]

# sfco crs EPSG:26910
# sfco bounding box [ 542780.10759459 4173570.61894116  556587.40211016 4184960.10238093]
# sfco bounding box [-122.51419799   37.70829506 -122.35784432   37.8108725 ]

