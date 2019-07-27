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


def wrap_text(text, font, width):
    if width == 0:
        return ""
    line_width = font.rendered_size(text)[0]
    if line_width > width:
        words = text.split(' ')
        for i in range(len(words)-1, 0, -1):
            curr_line = ' '.join(words[:-i])
            if font.rendered_size(curr_line)[0] <= width:
                return curr_line + "\n" + str(wrap_text(' '.join(words[len(words)-i:]), font, width))
        return text
    else:
        return text
