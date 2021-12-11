class ObjectModel:
    def __init__(self, gain=1, tau=5, dt=2):
        self._gain = gain
        self._tau = tau
        self._dt = dt

    @property
    def gain(self):
        return self._gain

    @property
    def tau(self):
        return self._tau

    @property
    def dt(self):
        return self._dt

    @gain.setter
    def gain(self, gain):
        if gain > 0:
            self._gain = gain

    @tau.setter
    def tau(self, tau):
        if tau > 0:
            self._tau = tau

    @dt.setter
    def dt(self, dt):
        if dt == 0:
            self._dt = 0.01
        elif dt > 0:
            self._dt = dt
