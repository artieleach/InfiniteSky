import numpy as np
from PIL import ImageFont
import art

font = ImageFont.truetype('Roboto-Regular.ttf', 15)

'''Notes:
    max char width per line is 250, try to keep it at 248.
    the font used is called mastodon-font but it's just roboto (for the time being)
    lines used should stay at 12, regardless of characters used.'''


cluster = ''' ░░░ 
░░▒░░
░▒▓▒░
░░▒░░
 ░░░ '''



def generate_art():
    canvas = np.zeros((31, 12), dtype=int)

    norm_dis = np.random.standard_normal(size=canvas.shape)
    for line_num, line in enumerate(norm_dis):
        for ele_num, element in enumerate(line):
            if element > 2.5:
                canvas[line_num][ele_num] = ord('◍')
            elif element > 2:
                canvas[line_num][ele_num] = ord('★')
            else:
                canvas[line_num][ele_num] = ord(' ')

    def add_art(ascii_art):
        art_arr = np.array([[ord(y) for y in x] for x in [list(i) for i in ascii_art.split('\n')]])
        y, x = (np.random.randint(canvas.shape[0]-art_arr.shape[0]), np.random.randint(canvas.shape[1]-art_arr.shape[1]))
        for col in range(y, y + art_arr.shape[0]):
            for row in range(x, x + art_arr.shape[1]):
                canvas[col, row] = art_arr[col-y, row-x]

    add_art(cluster)
    out_str = [[chr(cell) for cell in row] for row in canvas]
    fin_out = [''.join(row) for row in out_str]
    for line in fin_out:
        print(font.getsize(line), line)
    return '\n'.join(fin_out)


if __name__ == '__main__':
    print(generate_art())
