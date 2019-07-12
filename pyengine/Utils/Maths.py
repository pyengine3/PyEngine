def clamp(val, mini=None, maxi=None):
    if mini is None and maxi is None:
        return val
    elif mini is None:
        return val if val < maxi else maxi
    elif maxi is None:
        return val if val > mini else mini
    else:
        if val < mini:
            return mini
        elif val > maxi:
            return maxi
        else:
            return val
