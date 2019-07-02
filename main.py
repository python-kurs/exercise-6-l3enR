# Exercise 6
from pathlib import Path
from satpy import Scene, find_files_and_readers
import satpy as satpy


input_dir  = Path("data")
output_dir = Path("output")

# 1. Read the Scene that you downloaded from the data directory using SatPy. [2P]
files = find_files_and_readers(base_dir = input_dir, reader = "seviri_l1b_nc")
scn = Scene(filenames = files)

# 2. Load the composites "natural_color" and "convection" [2P]
scn.load(["natural_color"])
scn.load(["convection"])

# 3. Resample the fulldisk to the Dem. Rep. Kongo and its neighbours [4P] 
#    by defining your own area in Lambert Azimuthal Equal Area. 
#    Use the following settings:
#      - lat and lon of origin: -3/23
#      - width and height of the resulting domain: 500px
#      - projection x/y coordinates of lower left: -15E5
#      - projection x/y coordinates of upper right: 15E5
 
from utils import resample_area
local_scn = resample_area(area_id = "Democratic_Republic_Kongo", 
                          description = "Democratic Republic Kongo and its neighbors in Lambert Azimuthal Equal Area projection",
                          proj_id = "Democratic_Republic_Kongo",
                          proj_dict = {"proj":"laea", "lat_0": -3, "lon_0":23},
                          width = 500,
                          height = 500,
                          llx = -15E5,
                          lly = -15E5,
                          urx = 15E5,
                          ury = 15E5,
                          scn = scn)

# 4. Save both loaded composites of the resampled Scene as simple png images. [2P]
#construct output pathes
naturalCol = output_dir / "natural_color.png"
convect = output_dir / "convection.png"

local_scn.show("natural_color").save(naturalCol)
local_scn.show("convection").save(convect)
