# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

def resample_area(area_id, description, proj_id, proj_dict, width, height, llx, lly, urx, ury, scn):
    """
    Resample the used projection to the defined parameters and returns a local scene.
    
    The resample parameters are setted and are used in the AreaDefinition function. After that a local scene is generated.
    
    Parameters
    ----------
    area_id     : String
                  Unique name of the local scene
    description : String
                  Describe the scene
    proj_id     : String
                  Describe the projection
    proj_dict   : Dictionary
                  A dictionary with the keys "proj" for projection, "lat_0" and "lon_0" for the latitude and longitude origin
    width       : number
                  The widht of the bounding box
    height      : number
                  The height of the bounding box
    llx         : number
                  Lower left x corner
    lly         : number
                  Lower left y corner
    urx         : number
                  Upper right x corner
    ury         : number
                  Upper right y corner
        
    Returns
    -------
    scene object
    
    """
    from pyresample.geometry import AreaDefinition
    
    #bounding box
    area_extent = (llx, lly, urx, ury)
    
    #resample the area
    area_def = AreaDefinition(area_id, proj_id, description, proj_dict, width, height, area_extent)
    local_scn = scn.resample(area_def)
    
    return local_scn