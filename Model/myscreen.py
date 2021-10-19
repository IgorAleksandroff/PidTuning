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
        self._tau = 1
        self._dt = 1
        self._p = 0
        self._i = 0
        self._d = 0
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
    def p(self):
        return self._p

    @property
    def i(self):
        return self._i

    @property
    def d(self):
        return self._d

    @gain.setter
    def gain(self, value):
        self._gain = value
        self.calculation_param()
        self.notify_observers()

    @tau.setter
    def tau(self, value):
        self._tau = value
        self.calculation_param()
        self.notify_observers()

    @dt.setter
    def dt(self, value):
        self._dt = value
        self.calculation_param()
        self.notify_observers()

    def calculation_param(self):
        """The Cohen-Coon method calculates PID parameters."""
        print(self._gain, self._tau, self._dt)
        # Calculating Proportional Band (PB)
        self._p = 100 * self._gain / ((0.185 + self._tau / self._dt) * 1.35)
        # Calculating Integral Time (Ti)
        self._i = 2.5 * self._dt * (self._tau + 0.185 * self._dt) / (self._tau + 0.611 * self._dt)
        # Calculating Derivative Time (Td)
        self._d = 0.37 * self._dt * self._tau / (self._tau + 0.185 * self._dt)
        print(self._p, self._i, self._d)
    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()
