# coding=utf-8
import json
from  BaseHandlerh import BaseHandler
from Database.tables import Appointment,User

class RegisterHandler(BaseHandler):
    def post(self):
        m_password=self.get_argument('password')
        m_nick_name=self.get_argument('nickName')  # 昵称
        m_real_name=self.get_argument('realName')
        m_location=self.get_argument('location')
        m_birthday=self.get_argument('birthday')
        m_phone=self.get_argument('phone')

        retjson = {'code': '400', 'content': 'None'}
        # 防止重复注册
        try:
            user = self.db.query(User).filter(User.phone == m_phone).one()
            if user:
                retjson['content']="改手机号已经被注册，请更换手机号或直接登录"
        except: # 还没有注册
            new_user=User(
                password=m_password,
                nick_name=m_nick_name,
                real_name=m_real_name,
                level=1,  #  新用户注册默认level为1
                location=m_location,
                birthday=m_birthday,
                phone=m_phone)
            try:
                same_nickname_user = self.db.query(User).filter(User.nick_name == m_nick_name).one()
                if same_nickname_user:  # 该昵称已被使用
                    retjson['code'] = 400  # Request Timeout
                    retjson['content'] = '改昵称已被使用，请更换昵称'
            except: # 手机号和昵称皆没有被注册过
                    self.db.merge(new_user)
                    try:
                        self.db.commit()
                        retjson['code'] = 200  # success
                        retjson['content'] = '注册成功'
                    except:
                        self.db.rollback()
                        retjson['code'] = 408  # Request Timeout
                        retjson['content'] = 'Some errors when commit to database, please try again'

        self.write(json.dumps(retjson, ensure_ascii=False, indent=2))

