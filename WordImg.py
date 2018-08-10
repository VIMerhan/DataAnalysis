from pyecharts import Map
from pyecharts import WordCloud
import matplotlib.pyplot as plt


class WordImg(object):
    @staticmethod
    def get_word(name, value):
        if name is None:
            name = [
                'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
                'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
                'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
                'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
        if value is None:
            value = [
                1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        maskimg = plt.imread('./image/brunomars.jpeg')
        wc = WordCloud(width=600, height=600, background_color='white')
        wc.use_theme('dark')
        wc.add("", name, value, shape="circle", word_gap=20, word_size_range=None, rotate_step=45)
        return wc


if __name__ == '__main__':
    Wd = WordImg()
    # Wd.word(None,None).render()
    # Wd.Map()
