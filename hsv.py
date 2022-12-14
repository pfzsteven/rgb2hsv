import sys


def rgb2hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    return h, s, v


def hex_to_rgb(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    return ('{:02X}' * 3).format(r, g, b)


def print_hsv(rgb_str):
    rgb_arr = hex_to_rgb(rgb_str)
    hsv = rgb2hsv(rgb_arr[0], rgb_arr[1], rgb_arr[2])
    h = '{:.2f}'.format(hsv[0])
    s = '{:.2f}'.format(hsv[1])
    v = '{:.2f}'.format(hsv[2])
    print("%s:%s,%s,%s" % (rgb_str, h, s, v))


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 2:
        for i in range(1, len(args)):
            rgb_str = str(args[i]).replace("#", "")
            if len(rgb_str) % 6 == 0:
                sub_i = 0
                index = 0
                while index < len(rgb_str):
                    rgb = rgb_str[index:index + 5]
                    index += 6
                    print_hsv(rgb)
                continue
