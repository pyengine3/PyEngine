def clamp(val, mini, maxi):
    if val < mini:
        return mini
    elif val > maxi:
        return maxi
    else:
        return val
