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
            retjson = {'code': '400', 'content': 'None'}

        # 防止重复注册
        else:
            try:
                user = self.db.query(User).filter(User.phone == m_phone).one()
                if user:  # 用户存在
                    password = user.password
                    if m_password == password:  # 密码正确
                        retjson['code'] = 200
                        retdata = []
                        data = dict(
                            huodong="待加入"

                        )

                        retjson['content'] = 10101

                    else:
                        retjson['content'] = 10104  # 密码错误
                else:  # 用户不存在
                    retjson['content'] = 10103



            except: # 还没有注册
                retjson['code'] = 400
                retjson['content'] = u'该用户名不存在'
            self.write(json.dumps(retjson, ensure_ascii=False, indent=2))
