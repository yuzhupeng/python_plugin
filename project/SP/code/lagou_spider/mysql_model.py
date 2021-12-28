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
            # self.db = pymysql.connect(
            #     host='localhost',
            #     port=3306,
            #     user='root',
            #     password='54Haoxuan!',
            #     database='kuaidaili_ip'
            # )
            self.db = pymysql.connect(
                host='192.168.116.128',
                port=3306,
                user='root',
                password='940628',
                database='kuaidaili_ip'
            )
            self.db.ping()
            self.cursor = self.db.cursor()
        except err.OperationalError as f:
            print('错误信息:{}'.format(f))

    def close_connect(self):
        #关闭游标
        self.cursor.close()
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
        except:
            self.db.rollback()

    # ----------------------------------------------------表数据操作-----------------------------------------------------
    def insert_into_table(self, table_name, data):
        """
        添加数据
        :param table_name: 表名称
        :param data: 数据，传一个列表字典
        :return:
        """
        data_list = []
        if data:
            for i in data:
                key, value = tuple(i.keys()), tuple(i.values())
                data_list.append(value)
            value = re.sub(r"^\[|\]$", '', str(data_list))
            key = re.sub("'", '', str(key))
            insert_sql = """INSERT INTO %s %s VALUES %s""" % (table_name, key, value)
            try:
                self.cursor.execute(insert_sql)
                self.db.commit()
            except Exception as e:
                print(' %s插入失败，原因是 %s' % (table_name, e))
                self.db.rollback()

    def delete_table(self, table_name, condition):
        """
        更新数据
        :param table_name: 表名称
        :param condition: 条件
        :return:
        """
        delete_sql = """DELETE FROM %s WHERE %s""" % (table_name, condition)
        try:
            self.cursor.execute(delete_sql)
            self.db.commit()
        except:
            self.db.rollback()

    def update_table(self, table_name, data, condition):
        """
        更新数据
        :param table_name: 表名称
        :param data: 数据
        :param condition: sql条件
        :return:
        """
        values = ""
        for key, value in data.items():
            values += ", %s='%s'" % (key, value) if values else "%s='%s'" % (key, value)
        delete_sql = """UPDATE %s SET %s WHERE %s""" % (table_name, values, condition)
        try:
            self.cursor.execute(delete_sql)
            self.db.commit()
        except:
            self.db.rollback()

    def find_all_table(self, table_name, condition):
        """
        查询所有数据
        :param table_name: 表名称
        :param condition: sql条件
        :return: 查询结果
        """
        find_all_sql = """SELECT * FROM %s WHERE %s""" % (table_name, condition)
        try:
            self.cursor.execute(find_all_sql)
            find_result = self.cursor.fetchall()
            row_count = self.cursor.rowcount
            self.db.commit()

            return find_result, row_count
        except Exception as e:
            self.db.rollback()


if __name__ == '__main__':
    xhx_mysql = xhx_mysql()
    xhx_mysql.create_connect()
    if xhx_mysql.db:
        # xhx_mysql.create_goods_type_table()
        # xhx_mysql.alter_add_table('user', 'height', 'decimal(5,2) null default null comment "身高"')
        # xhx_mysql.alter_modify_table(db, cursor, 'user', 'age', "tinyint null default null comment '年龄'"
        # data = [{'username': '刘梦琪', 'age': 29, 'sex': '女', 'height': 169},
        #         {'username': '夏浩轩', 'age': 28, 'sex': '男', 'height': 173}]
        # xhx_mysql.insert_into_table('user', data)
        # xhx_mysql.delete_table('user', "username='%s'" % '夏浩轩')
        # data = {"username": '夏浩轩', 'age': 28, 'sex': '男', 'height': 179}
        # xhx_mysql.update_table('user', data, "id=%d AND age=%d" % (21, 28))
        result, row_count = xhx_mysql.find_all_table('ip_list', 'id > %d' % 21)
        print(result, row_count)
    else:
        print("断开连接")
