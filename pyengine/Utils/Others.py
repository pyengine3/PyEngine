import os
from PIL import Image


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


def get_images_from_gif(file):
    frames = []
    im = Image.open(file)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    mode = results['mode']

    im = Image.open(file)

    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')

    try:
        while True:

            from pyengine.Utils import loggers
            loggers.get_logger("PyEngine").debug("saving %s (%s) frame %d, %s %s" % (file, mode, i, im.size, im.tile))

            if not im.getpalette():
                im.putpalette(p)

            new_frame = Image.new('RGBA', im.size)

            if mode == 'partial':
                new_frame.paste(last_frame)

            name = '%s-%d.png' % (''.join(file.split('.')[:-1]), i)

            new_frame.paste(im, (0, 0), im.convert('RGBA'))
            new_frame.save(name, 'PNG')
            frames.append(name)

            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return frames
