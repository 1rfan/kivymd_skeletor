from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from db_func import DbObject
from kivy.properties import ObjectProperty
from kivymd.uix.toolbar import MDToolbar


class LoginCard(MDCard):
    dbl = DbObject('myappdb.db')
    username_input = ObjectProperty()
    userpswd_input = ObjectProperty()
    chk_authorized = 0

    def chk_user(self):
        uname_input = self.username_input.text
        upswd_input = self.userpswd_input.text

        self.chk_authorized = self.dbl.chk_login_pwd(uname_input, upswd_input)
        if(self.chk_authorized == 1):
            print("authorized access!!")
            self.parent.parent.parent.ids.screen_mgr.current = "scr_main"
        else:
            self.ids.txt_info.text = "[color=ff0000]Unauthorized access. Invalid Username or Password? Try again![/color]"
            print("UNauthorized access!!")


class TopToolBar(MDToolbar):
    pass


class Myapp(MDApp):
    db = DbObject('myappdb.db')


Myapp().run()
