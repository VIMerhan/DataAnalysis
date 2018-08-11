import sys

import matplotlib.pyplot as plt
from pyecharts import WordCloud


class WordImg(object):
    NAME = [
        'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break'
        ]

    VALUE = [
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def get_word(name=NAME, value=VALUE):
        path = sys.path[1]
        maskimg = plt.imread(path + '/Image/brunomars.jpeg')
        wc = WordCloud(width=600, height=600, background_color='white')
        wc.use_theme('dark')
        wc.add("词云图", name, value, shape="circle", word_gap=20, word_size_range=None, rotate_step=45, mask=maskimg)
        return wc


if __name__ == '__main__':
    Wd = WordImg()
    Wd.get_word().render()
