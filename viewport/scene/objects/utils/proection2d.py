import math


def project_2d_coord(vcr, arad):
    # vcr = vector,
    # arad = angle radian
    return vcr[0] * math.cos(arad) - vcr[1] * math.sin(arad), vcr[1] * math.cos(arad) + vcr[0] * math.sin(arad)
