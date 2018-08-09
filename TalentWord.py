from pyecharts import Map
from pyecharts import WordCloud


class TalentWord(object):
    def word(self, name, value):
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

        cloudpage = WordCloud(width=1080, height=620)
        cloudpage.add("", name, value, shape="circle", word_gap=20, word_size_range=None, rotate_step=45)

        return cloudpage

    def Map(self):
        value = [95.1, 23.2, 43.3, 66.4, 88.5]
        attr = ["China", "Canada", "Brazil", "Russia", "United States"]
        map = Map("World Map Example", width=1200, height=600)
        map.add("", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
        map.render()


if __name__ == '__main__':
    Wd = TalentWord()
    Wd.word(None,None).render()
    # Wd.Map()
