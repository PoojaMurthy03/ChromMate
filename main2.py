from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image

KV = '''
ScreenManager:
    id: screen_manager
    SplashScreen:
    HomeScreen:
    NewScreen:
    TestScreen1:
    TestScreen2:
    TestScreen3:
    TestScreen4:
    TestScreen5:
    TestScreen6:
    TestScreen7:
    TestScreen8:
    TestScreen9:
    TestScreen10:
    TestScreen11:
    TestScreen12:
    TestScreen13:
    TestScreen14:
    TestScreen15:
    TestScreen16:
    TestScreen17:
    TestScreen18:
    TestScreen19:
    TestScreen20:
    TestScreen21:
    TestScreen22:
    TestScreen23:
    TestScreen24:
    TestScreen25:
    TestScreen26:
    TestScreen27:
    TestScreen28:
    TestScreen29:
    TestScreen30:
    TestScreen31:
    TestScreen32:
    TestScreen33:
    TestScreen34:
    TestScreen35:
    TestScreen36:
    TestScreen37:
    TestScreen38:
    PredictionScreen
    # Add all your 38 screens here as TestScreenX

<SplashScreen>:
    name: 'splash'
    MDBoxLayout:
        orientation: 'vertical'
        Image:
            source:'logo.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

<HomeScreen>:
    name: 'home'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: top_app_bar
            title: 'ChromMate'
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
            elevation: 10
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            size_hint_y: None
            height: dp(56)
        MDNavigationDrawer:
            id: nav_drawer
            swipe_distance: 10
            ScrollView:
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: '18dp'
                    padding: '50dp'
                    MDRaisedButton:
                        text: 'Take a Test'
                        size_hint_x: None
                        width: root.width - dp(100)
                        on_release:
                            nav_drawer.set_state("close")
                            app.show_new_screen()
                    MDRaisedButton:
                        text: 'Protanomaly'
                        size_hint_x: None
                        width: root.width - dp(100)
                        on_release: nav_drawer.set_state("close")
                    MDRaisedButton:
                        text: 'Deuteranomaly'
                        size_hint_x: None
                        width: root.width - dp(100)
                        on_release: nav_drawer.set_state("close")
                    MDRaisedButton:
                        text: 'Tritanomaly'
                        size_hint_x: None
                        width: root.width - dp(100)
                        on_release: nav_drawer.set_state("close")

<NewScreen>:
    name: 'new_screen'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'ChromMate'
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
            elevation: 10
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(50)
            spacing: dp(20)
            MDLabel:
                text: 'Instructions: Please read the instructions carefully before starting the test.'
                halign: 'center'
                theme_text_color: 'Primary'
                size_hint_y: None
                height: self.texture_size[1]
            MDRaisedButton:
                text: 'Start'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: dp(100), dp(50)
                on_release: app.show_test_screen()

<TestScreen1>:
    name: 'test_screen_1'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image1.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '12/0.7'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '8/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '15/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '7/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen2>:
    name: 'test_screen_2'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image2.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '6/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '3/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '8/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '5/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen3>:
    name: 'test_screen_3'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image3.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '8/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '6/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '0/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '5/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen4>:
    name: 'test_screen_4'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image4.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '20/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '70/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '28/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '29/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen5>:
    name: 'test_screen_5'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image5.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '57/o.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '35/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '67/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '61/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen6>:
    name: 'test_screen_6'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image6.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '5/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '6/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '2/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '8/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
<TestScreen7>:
    name: 'test_screen_7'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image7.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '3/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '9/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '5/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '8/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen8>:
    name: 'test_screen_8'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image8.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '17/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '15/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '16/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '13/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen9>:
    name: 'test_screen_9'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image9.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '14/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '24/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '21/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '74/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen10>:
    name: 'test_screen_10'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image10.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '7/0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '8/0.2'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '2/0.8'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '9/0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
<TestScreen11>:
    name: 'test_screen_11'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image11.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '5/0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '6/0.8'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '0/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '8/1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
<TestScreen12>:
    name: 'test_screen_12'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image12.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '97/0.9'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '87/0.5'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '81/0.5'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '91/0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
<TestScreen13>:
    name: 'test_screen_13'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image13.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '45/0.9'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '15/0.5'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '46/0.5'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '18/0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen14>:
    name: 'test_screen_14'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image14.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '5/0.9'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '8/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '6/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '3/0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen15>:
    name: 'test_screen_15'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image15.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '7/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '1/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '9/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '4/0.02'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
<TestScreen16>:
    name: 'test_screen_16'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image16.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '16/0.8'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '10/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '46/0.0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '40/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen17>:
    name: 'test_screen_17'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image17.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '73/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '23/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '78/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '28/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen18>:
    name: 'test_screen_18'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image18.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'Nothing/0.8'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '3/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '4/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '8/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen19>:
    name: 'test_screen_19'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image19.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '13/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '18/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'Nothing/0.06'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '15/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen20>:
    name: 'test_screen_20'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image20.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'Nothing/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '28/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '23/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '25/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen21>:
    name: 'test_screen_21'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image21.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'Nothing/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '43/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '48/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '18/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen22>:
    name: 'test_screen_22'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image22.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '20/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '2/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '26/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '6/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen23>:
    name: 'test_screen_23'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image23.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '42/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '2/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '4/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '48/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen24>:
    name: 'test_screen_24'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image24.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '35/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '5/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '3/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '38/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen25>:
    name: 'test_screen_25'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image25.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: '96/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '6/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '9/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '90/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen26>:
    name: 'test_screen_26'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image26.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'purple and red spots/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'only the purple line/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'only the red line/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'none/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen27>:
    name: 'test_screen_27'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image27.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'purple and red spots/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'only the purple line/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'only the red line/0.15'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'none/0.1'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen28>:
    name: 'test_screen_28'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image28.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'nothing/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'a line/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'none/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '3/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen29>:
    name: 'test_screen_29'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image29.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'nothing/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'line/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'none/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '3/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen30>:
    name: 'test_screen_30'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image30.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'blue-green line/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'nothing/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'line/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: '5/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen31>:
    name: 'test_screen_31'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image31.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'blue/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'blue-green line/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'nothing/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'green/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen32>:
    name: 'test_screen_32'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image32.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'orange line/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'nothing or a false line/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'blue/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'green/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen33>:
    name: 'test_screen_33'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image33.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'orange line/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'nothing or false line/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'green/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'orange/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen34>:
    name: 'test_screen_34'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image34.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'blue-green and yellow-green line/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'only red green and voilet line/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'nothing/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'green line/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen35>:
    name: 'test_screen_35'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image35.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'blue-green and yellow-green line/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'only blue-green and voilet line/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'blue/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'nothing/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen36>:
    name: 'test_screen_36'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image36.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'voilet and orange line/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'blue-green and voilet line/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'voilet/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'green/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen37>:
    name: 'test_screen_37'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image37.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'voilet and orange line/0.6'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'blue-green and voilet line/0.3'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'blue/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()
        MDRaisedButton:
            text: 'nothing/0.05'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_next_screen()

<TestScreen38>:
    name: 'test_screen_38'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        Image:
            source: 'image38.png'
            size_hint: None, None
            size: dp(200), dp(200)
            pos_hint: {'center_x': 0.5}
        MDRaisedButton:
            text: 'red-line-basic/1.0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_prediction_screen()
        MDRaisedButton:
            text: 'red-line-curve/0.0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_prediction_screen()
        MDRaisedButton:
            text: 'red-straight-line/0.0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_prediction_screen()
        MDRaisedButton:
            text: 'red-line-sharp/0.0'
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {'center_x': 0.5}
            on_release: app.show_prediction_screen()
<PredictionScreen>:
    name: 'prediction_screen'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'ChromMate'
            md_bg_color: app.theme_cls.primary_color
            specific_text_color: 1, 1, 1, 1
            elevation: 10
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(50)
            spacing: dp(20)
            MDLabel:
                text: 'Prediction'
                halign: 'center'
                theme_text_color: 'Primary'
                size_hint_y: None
                height: self.texture_size[1]
            MDRaisedButton:
                text: 'Home'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint: None, None
                size: dp(100), dp(50)
                on_release: app.show_home_screen()


# Add TestScreenX for all 38 screens here
'''

Window.size = (390, 680)

class SplashScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class NewScreen(Screen):
    pass

class TestScreen1(Screen):
    pass

class TestScreen2(Screen):
    pass

class TestScreen3(Screen):
    pass

class TestScreen4(Screen):
    pass
class TestScreen5(Screen):
    pass
class TestScreen6(Screen):
    pass
class TestScreen7(Screen):
    pass
class TestScreen8(Screen):
    pass

class TestScreen9(Screen):
    pass

class TestScreen10(Screen):
    pass

class TestScreen11(Screen):
    pass

class TestScreen12(Screen):
    pass
class TestScreen13(Screen):
    pass
class TestScreen14(Screen):
    pass
class TestScreen15(Screen):
    pass
class TestScreen16(Screen):
    pass

class TestScreen17(Screen):
    pass

class TestScreen18(Screen):
    pass

class TestScreen19(Screen):
    pass

class TestScreen20(Screen):
    pass
class TestScreen21(Screen):
    pass
class TestScreen22(Screen):
    pass
class TestScreen23(Screen):
    pass
class TestScreen24(Screen):
    pass

class TestScreen25(Screen):
    pass

class TestScreen26(Screen):
    pass

class TestScreen27(Screen):
    pass

class TestScreen28(Screen):
    pass
class TestScreen29(Screen):
    pass
class TestScreen30(Screen):
    pass
class TestScreen31(Screen):
    pass
class TestScreen32(Screen):
    pass

class TestScreen33(Screen):
    pass

class TestScreen34(Screen):
    pass

class TestScreen35(Screen):
    pass

class TestScreen36(Screen):
    pass
class TestScreen37(Screen):
    pass
class TestScreen38(Screen):
    pass
class PredictionScreen(Screen):
    pass


# Define TestScreenX for all 38 screens here

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        screen_manager = Builder.load_string(KV)
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.switch_to_home, 38)

    def switch_to_home(self, dt):
        self.root.current = 'home'

    def show_test_screen(self):
        self.root.current = 'test_screen_1'

    def show_new_screen(self):
        self.root.current = 'new_screen'
    
    def show_next_screen(self):
        current_screen_index = self.get_current_test_screen_index()
        if current_screen_index < 38:  # Adjust this number based on total screens
            next_screen_name = f"test_screen_{current_screen_index + 1}"
            self.root.current = next_screen_name

    def get_current_test_screen_index(self):
        current_screen_name = self.root.current
        if current_screen_name.startswith('test_screen_'):
            return int(current_screen_name.split('_')[-1])
        return 1

    def show_prediction_screen(self):
        self.root.current = 'prediction_screen'

    def show_home_screen(self):
        self.root.current = 'home'

if __name__ == '__main__':
    MyApp().run()
