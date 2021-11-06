import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField

from Utility.observer import Observer

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MyScreenView(MDScreen, Observer):
    """"
    A class that implements the visual presentation `MyScreenModel`.

    """

    # <Controller.myscreen_controller.MyScreenController object>.
    controller = ObjectProperty()
    # <Model.myscreen.MyScreenModel object>.
    model = ObjectProperty()

    pi_tables, pid_tables = None, None

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)  # register the view as an observer

    def set_gain(self, focus, value):
        if not focus:
            self.controller.set_gain(value)

    def set_tau(self, focus, value):
        if not focus:
            self.controller.set_tau(value)

    def set_dt(self, focus, value):
        if not focus:
            self.controller.set_dt(value)

    def model_is_changed(self):
        row_data_for_tab = []
        """
        The method is called when the model changes.

        """
        self.ids.pp.text = str(round(self.model.pp, 2))
        self.ids.ii.text = str(round(self.model.ii, 2))

        self.ids.p.text = str(round(self.model.p, 2))
        self.ids.i.text = str(round(self.model.i, 2))
        self.ids.d.text = str(round(self.model.d, 2))

        row_pi_for_tab = [
            (
                "1",
                "Cohen-Coon",
                str(round(self.model.pp, 2)),
                str(round(self.model.ii, 2)),
                "-",
            ),
        ]
        row_pid_for_tab = [
            (
                "1",
                "Cohen-Coon",
                str(round(self.model.p, 2)),
                str(round(self.model.i, 2)),
                str(round(self.model.d, 2)),
                "-",
            ),
        ]

        self.pi_tables = MDDataTable(
            size_hint = (0.9, 0.9),
            # name column, width column, sorting function column(optional)
            column_data = [
                ("No.", dp(10)),
                ("Method", dp(30)),
                ("P", dp(15)),
                ("I", dp(15)),
            ],
            row_data = row_pi_for_tab,
        )
        self.ids.calc_pi_table.clear_widgets()
        self.ids.calc_pi_table.add_widget(self.pi_tables)

        self.pid_tables = MDDataTable(
            size_hint = (0.9, 0.9),
            # name column, width column, sorting function column(optional)
            column_data = [
                ("No.", dp(10)),
                ("Method", dp(30)),
                ("P", dp(15)),
                ("I", dp(15)),
                ("D", dp(15)),
            ],
            row_data = row_pid_for_tab,
        )
        self.ids.calc_pid_table.clear_widgets()
        self.ids.calc_pid_table.add_widget(self.pid_tables)

    def on_tab_switch(self, *args):
        self.current_tab = args[1].name


Builder.load_file(os.path.join(os.path.dirname(__file__), "myscreen.kv"))
