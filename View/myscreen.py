import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.uix.screen import MDScreen

from Utility.observer import Observer


class MyScreenView(MDScreen, Observer):
    """"
    A class that implements the visual presentation `MyScreenModel`.

    """

    # <Controller.myscreen_controller.MyScreenController object>.
    controller = ObjectProperty()
    # <Model.myscreen.MyScreenModel object>.
    model = ObjectProperty()

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
        """
        The method is called when the model changes.

        """
        self.ids.result.text = str(self.model.sum)


Builder.load_file(os.path.join(os.path.dirname(__file__), "myscreen.kv"))
