# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.


class MyScreenModel:
    """
    The MyScreenModel class is a data model implementation. The model stores
    the values of the variables `c`, `d` and their sum. The model provides an
    interface through which to work with stored values. The model contains
    methods for registration, deletion and notification observers.

    The model is (primarily) responsible for the logic of the application.
    MyScreenModel class task is to add two numbers.
    """

    def __init__(self):
        self._gain = 0
        self._tau = 0
        self._dt = 0
        self._sum = 0
        self._observers = []

    @property
    def gain(self):
        return self._gain

    @property
    def tau(self):
        return self._tau

    @property
    def dt(self):
        return self._dt

    @property
    def sum(self):
        return self._sum

    @gain.setter
    def gain(self, value):
        self._gain = value
        self._sum = self._gain + self._tau + self._dt
        self.notify_observers()

    @tau.setter
    def tau(self, value):
        self._tau = value
        self._sum = self._gain + self._tau + self._dt
        self.notify_observers()

    @dt.setter
    def dt(self, value):
        self._dt = value
        self._sum = self._gain + self._tau + self._dt
        self.notify_observers()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()
