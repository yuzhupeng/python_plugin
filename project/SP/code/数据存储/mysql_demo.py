# coding=utf-8
import pymysql
from pymysql import err
import time
import re


class xhx_mysql(object):

    def __init__(self):
        self.db = None
        self.cursor = None

    def create_connect(self):
        try:
            self.db = pymysql.connect(
                host='192.168.116.128',
                port=3306,
                user='root',
                password='940628',
                database='pymysql_test'
            )
            self.db.ping()
            self.cursor = self.db.cursor()
        except err.OperationalError as f:
            print('错误信息:{}'.format(f))

    def close_connect(self):
        # 关闭数据库连接
        self.db.close()

    # ----------------------------------------------------表结构操作-----------------------------------------------------
    def create_goods_type_table(self):
        drop_sql = """drop table if exists goods_type"""
        self.cursor.execute(drop_sql)
        create_sql = """create table goods_type (
        `id` int(10) unsigned not null auto_increment comment '主键',
        `tinyint` tinyint null default null comment '1个字节 2^8字节',
        `smallint` smallint null default null comment '2个字节 2^16',
        `mediumint` mediumint null default null comment '3个字节 2^24',
        `bigint` bigint null default null comment '8个字节 2^64',
        `char` char(10) null default null comment '固定长度，小型数据',
        `varchar` varchar(255) null default null comment '可变长度，小型数据',
        `text` text null default null comment '可变长度，大型数据',
        `longtext` longtext null default null comment '可变长度，大型文本数据',
        `date` date null default null comment '年月日YYYY-MM-DD',
        `time` time null default null comment '时分秒HH:MM:SS',
        `year` year null default null comment '年份',
        `datetime` datetime not null default CURRENT_TIMESTAMP() comment '日期和时间混合',
        `timestamp` timestamp not null default NOW() comment '日期和时间混合 可做时间戳',
        `enum` enum('1','2','3') not null default '1' comment '枚举',
        `decimal` decimal(5,2) not null default '5.20' comment '小数表示，前面整数位数，后面小数位数',
        primary key (`id`) using btree
        )
        """
        try:
            self.cursor.execute(create_sql)
            self.db.commit()
            self.cursor.close()
        except:
            self.db.rollback()

    def alter_add_table(self, table_name, field_name, constraint):
        """
        添加表字段
        :param table_name: 表名称
        :param field_name: 添加字段名
        :param constraint: 字段约束
        :return:
        """
        alter_sql = """alter table {} add {} {}""".format(table_name, field_name, constraint)
        try:
            self.cursor.execute(alter_sql)
            self.db.commit()
            self.cursor.close()
        except:
            self.db.rollback()

    def alter_modify_table(self, table_name, field_name, constraint):
        """
        修改表字段
        :param table_name: 表名称
        :param field_name: 修改字段
        :param constraint: 字段约束
        :return:
        """
        alter_sql = """alter table {} modify {} {}""".format(table_name, field_name, constraint)
        try:
            self.cursor.execute(alter_sql)
            self.db.commit()
            self.cursor.close()
        except:
            self.db.rollback()

    # ----------------------------------------------------表数据操作-----------------------------------------------------
    def insert_into_table(self, table_name, data):
        key, value = str(tuple(data.keys())), str(tuple(data.values()))
        key = re.sub("'", '', key)
        insert_sql = """INSERT INTO %s %s VALUES %s""" % (table_name, key, value)
        try:
            self.cursor.execute(insert_sql)
            self.db.commit()
            self.cursor.close()
        except:
            self.db.rollback()


if __name__ == '__main__':
    xhx_mysql = xhx_mysql()
    xhx_mysql.create_connect()
    if xhx_mysql.db:

        # xhx_mysql.create_goods_type_table()
        # xhx_mysql.alter_add_table('user', 'height', 'decimal(5,2) null default null comment "身高"')
        # xhx_mysql.alter_modify_table(db, cursor, 'user', 'age', "tinyint null default null comment '年龄'"
        data = [{'username': '刘梦琪', 'age': 29, 'sex': '女', 'height': 169}, {'username': '夏浩轩', 'age': 28, 'sex': '男', 'height': 173}]

        data1 = {'username': '刘梦琪', 'age': 29, 'sex': '女', 'height': 169}

        xhx_mysql.insert_into_table('user', {'username': '刘梦琪', 'age': 29, 'sex': '女', 'height': 169})

    else:
        print("断开连接")
