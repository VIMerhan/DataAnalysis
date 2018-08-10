import pymongo
from scrapy.utils.project import get_project_settings


class Mongo(object):

    def test(self):
        settings = get_project_settings()

        # 连接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])

        self.db = self.client[settings['MONGO_DB']]
        self.coll = self.db[settings['MONGO_COLL']]

        def process_item(self, item, spider):
            pass


if __name__ == '__main__':
    tt = Mongo()
    tt.test()
