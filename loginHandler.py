# coding=utf-8
from sqlalchemy.dialects.postgresql import json

from BaseHandlerh import BaseHandler
from Database.tables import Appointment, User


class LoginHandler(BaseHandler):

    def post(self):
        m_phone = self.get_argument('phone')
        m_password = self.get_argument('password')
        retjson = {'code' : '400', 'content' : u'未处理 '}
        if not m_phone or not m_password:
            retjson['code'] = 400
            retjson['content'] = u'用户名密码不能为空'
            retjson = {'code': '400', 'content': 'None','Code':''}

        # 防止重复注册
        else:
            try:
                user = self.db.query(User).filter(User.phone == m_phone).one()
                if user:
                    password = user.password
                    if m_password == password:
                        retjson['code'] = 200
                        retdata = []
                        data = dict(
                            daohanglan="约拍首页顶部滑动图片,应设置与本地对比或增加一特定链接，图片未更新时应使用本地缓存",
                            renqibang="人气榜前多少名,每人应该是一组数据",
                        )

                        retjson['Code'] = 10101
                        retjson['data']=data

                    else:
                        retjson['Code'] = 10104  # 密码错误
                else:  # 用户不存在
                    retjson['Code'] = 10103

            except: # 还没有注册
                retjson['code'] = 400
                retjson['Code'] = u'该用户名不存在'
            self.write(json.dumps(retjson, ensure_ascii=False, indent=2))
