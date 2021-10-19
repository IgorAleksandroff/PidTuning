from View.myscreen import MyScreenView


class MyScreenController:
    """
    The `MyScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.

    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        """
        The constructor takes a reference to the model.
        The constructor creates the view.
        """

        self.model = model
        self.view = MyScreenView(controller=self, model=self.model)

    def get_screen(self):
        """The method creates get the view."""

        return self.view

    def set_gain(self, value):
        """
        When finished editing the data entry field for `Gain`, the controller
        changes the `gain` property of the model.
        """

        self.model.gain = value

    def set_tau(self, value):
        """
        When finished editing the data entry field for `Tau`, the controller
        changes the `tau` property of the model.
        """

        self.model.tau = value

    def set_dt(self, value):
        """
        When finished editing the data entry field for `dt`, the controller
        changes the `dt` property of the model.
        """

        self.model.dt = value