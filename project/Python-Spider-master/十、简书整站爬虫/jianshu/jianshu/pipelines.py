# -*- coding: utf-8 -*-
# import pymysql
#
# class JianshuPipeline(object):
#     def __init__(self):
#         dbparams = {
#             'host': '127.0.0.1',
#             'port': 3306,
#             'user': 'root',
#             'password': '123456',
#             'database': 'jianshu',
#             'charset': 'utf8'
#         }
#         self.conn = pymysql.connect(**dbparams)
#         self.cursor = self.conn.cursor()
#         self._sql = None
#
#     def process_item(self, item, spider):
#         self.cursor.execute(self.sql, (item['title'], item['content'],
#                                        item['author'], item['avatar'], item['pub_time'], item['article_id'],
#                                        item['origin_url'],item['like_count'],item['word_count'],item['subjects'],item['comment_count'],item['read_count']))
#         self.conn.commit()
#         return item
#
#     @property
#     def sql(self):
#         if not self._sql:
#             self._sql = """
#                 insert into article(id,title,content,author,avatar,pub_time,
#                 article_id,origin_url,like_count,word_count,subjects,comment_count,read_count) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#             """
#             return self._sql
#         return self._sql


# 采用twisted异步保存到mysql

import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors


class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool("pymysql", **dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                            insert into article(id,title,content,author,avatar,pub_time,
                            article_id,origin_url) values(null,%s,%s,%s,%s,%s,%s,%s)
                        """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (item['title'], item['content'],
                                       item['author'], item['avatar'], item['pub_time'], item['article_id'],
                                       item['origin_url']))

    def handle_error(self, error, item, spider):
        # print(error)
        pass
