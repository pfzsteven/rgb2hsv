import sys


def RGBTOHSVHelper(offset, dominantcolor, colorone, colortwo):
    V = dominantcolor
    if V != 0.0:
        if colorone <= colortwo:
            num1 = colorone
        else:
            num1 = colortwo
            pass
        num2 = V - num1
        if num2 != 0.0:
            S = num2 / V
            H = offset + (colorone - colortwo) / num2
            pass
        else:
            S = 0.0
            H = offset + (colorone - colortwo)
            pass
        H = H / 6.0
        if H >= 0.0:
            return (H, S, V)
        H = H + 1
        pass
    else:
        S = 0
        H = 0
        pass
    return (H, S, V)


def rgb2hsv(r: float, g: float, b: float):
    if b > g and b > r:
        hsv = RGBTOHSVHelper(4.0, b, r, g)
    elif g > r:
        hsv = RGBTOHSVHelper(2.0, g, b, r)
    else:
        hsv = RGBTOHSVHelper(0.0, r, g, b)
    return (int(hsv[0] * 360), int(hsv[1] * 100), int(hsv[2] * 100))


def hex_to_rgb(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    return ('{:02X}' * 3).format(r, g, b)


def print_hsv(rgb_str):
    rgb_arr = hex_to_rgb(rgb_str)
    r = rgb_arr[0] / 255.0
    g = rgb_arr[1] / 255.0
    b = rgb_arr[2] / 255.0
    # print("rgb is:", (r, g, b))
    hsv = rgb2hsv(r, g, b)
    print("%s:%s,%s,%s" % (rgb_str, hsv[0], hsv[1], hsv[2]))


if __name__ == '__main__':
    args = sys.argv
    if len(args) >= 2:
        for i in range(1, len(args)):
            rgb_str = str(args[i]).replace("#", "")
            if len(rgb_str) % 6 == 0:
                sub_i = 0
                index = 0
                while index < len(rgb_str):
                    rgb = rgb_str[index:index + 6]
                    index += 6
                    print_hsv(rgb)
                continue
