from pyecharts import Pie


class PieImg(object):
    schema = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    data = [1, 20, 50, 100, 10, 10]

    @staticmethod
    def get_pie(schema, data):
        pie = Pie("饼图示例")
        pie.add("", schema, data, is_label_show=True,rosetype=None)
        return pie


if __name__ == '__main__':
    PieImg.get_pie(PieImg.schema, PieImg.data).render()
