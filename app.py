from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.filechooser import FileChooserIconView
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.popup import *
from engine import Compare
from kivymd.toast import toast
import os
import platform
import subprocess
import sys

def find_path(path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    else:
        return os.path.join(os.path.abspath('.'), path)
class Home(MDScreen):
    files_list = []
    def load_file(self, btn):
       
        file_chooser = FileChooserIconView()

        Float = FloatLayout()
        Float.add_widget(file_chooser)
        load_file_btn = MDFillRoundFlatButton(text = 'select file', font_size='20dp')
        Float.add_widget(load_file_btn)
        def load_selected_file(btn_object):
            if file_chooser.selection:
                path_of_file = file_chooser.selection[0]
                
                btn.text = 'file choosen'
                
                btn.disabled = True

                self.files_list.append(path_of_file)
               
                
                popup.dismiss()
                
        load_file_btn.bind(on_release=load_selected_file)

        
        popup = Popup(title='select file', content=Float)
       
        popup.open()

    def compare_files(self):
        
        if len(self.files_list) == 2:
            
            
            try:
                path = Compare().compare(self.files_list[0], self.files_list[1])
                if platform.system() == "Windows":
                    os.startfile(path)
                elif platform.system() == 'Darwin':
                    subprocess.call(['open', path])
                else:
                    subprocess.call(['xdg-open', path])
            except Exception as e:
               toast(str(e))
               
            self.files_list.pop()

            self.files_list.pop()
            self.ids.btn_1.disabled = False
            self.ids.btn_1.text = 'load first excel file'
            self.ids.btn_1.md_bg_color = 'orange'


            self.ids.btn_2.disabled = False
            self.ids.btn_2.text = 'load second excel file'
            self.ids.btn_2.md_bg_color = 'orange'
        else:
            toast('please choose two files to compare them')

    pass

class ExcelComparer(MDApp):
    def build(self):
        self.icon = find_path('assets/ExcelComparerIcon.png')
        Builder.load_file(find_path('kv_file.kv'))
       
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        return sm

if __name__ == "__main__":
    ExcelComparer().run()