# -*- coding: utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline
from bmx import settings
import os

class BMXImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #这个方法是在发送下载请求之前调用
        request_objs = super(BMXImagesPipeline, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        #这个方法是在图片将要被保存的时候调用，用来获取图片存储的路劲
        path = super(BMXImagesPipeline, self).file_path(request,response,info)
        category = request.item.get('category')
        image_store = settings.IMAGES_STORE
        category_path = os.path.join(image_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace("full/","")
        image_path = os.path.join(category_path,image_name)
        return image_path

