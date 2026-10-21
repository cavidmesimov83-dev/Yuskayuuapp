from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

Window.clearcolor = (0.05, 0.0, 0.0, 1)

class YuskayuuSafeJokeApp(App):
    def build(self):
        self.saygac = 60
        self.anim_say = 0
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.basliq = Label(text='[color=ff0000][b]☠️ YUSKAYUU HACKED ☠️[/b][/color]', markup=True, font_size='24sp', halign='center', size_hint=(1, 0.2))
        main_layout.add_widget(self.basliq)
        self.durum_lbl = Label(text='[color=ffff00]SİSTEMİNİZ TAMAMİLƏ NƏZARƏT ALTINDADIR![/color]', markup=True, font_size='14sp', halign='center', size_hint=(1, 0.2))
        main_layout.add_widget(self.durum_lbl)
        fidye_metni = Label(text='[color=ffffff]Bütün şəxsi fayllar şifrələndi.\nKilidi açmaq üçün təlimatları gözləyin...[/color]', markup=True, font_size='13sp', halign='center', size_hint=(1, 0.25))
        main_layout.add_widget(fidye_metni)
        self.timer_lbl = Label(text=f'[color=ff3333][b]QALAN VAXT: {self.saygac}s[/b][/color]', markup=True, font_size='18sp', halign='center', size_hint=(1, 0.15))
        main_layout.add_widget(self.timer_lbl)
        btn = Button(text='ZARAFATI BİTİR / ÇIXIŞ', background_color=(0.3, 0.3, 0.3, 1), font_size='14sp', bold=True, size_hint=(1, 0.2))
        btn.bind(on_press=self.cixis_et)
        main_layout.add_widget(btn)
        Clock.schedule_interval(self.geri_say, 1.0)
        Clock.schedule_interval(self.animasiya_islet, 0.5)
        return main_layout

    def animasiya_islet(self, dt):
        self.anim_say += 1
        if self.anim_say % 2 == 0:
            self.basliq.text = '[color=ff0000][b]☠️ YUSKAYUU HACKED ☠️[/b][/color]'
        else:
            self.basliq.text = '[color=ffffff][b]🔒 SİSTEM KİLİDLƏNDİ 🔒[/b][/color]'

    def geri_say(self, dt):
        if self.saygac > 0:
            self.saygac -= 1
            self.timer_lbl.text = f'[color=ff3333][b]QALAN VAXT: {self.saygac}s[/b][/color]'

    def cixis_et(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    YuskayuuSafeJokeApp().run()
