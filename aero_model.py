class AeroModel(object):
    def __init__(self):
        self.aero_file = ''
        self.zero_lift_alpha = 0
        self.dcl_dalpha = 0
        self.dcl_dalpha_stall = 0
        self.max_cl = 0
        self.min_cl = 0
        self.cl_increment_to_stall = 0
        self.min_cd = 0
        self.cl_at_min_cd = 0
        self.re = 0
    
