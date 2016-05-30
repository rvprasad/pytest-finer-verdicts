class Engine:
    def rotations(self):
        return 51
    def getTemp(self):
        return 75


def test_pass():
    o = Engine()
    while o.rotations() < 50:
        pass
    assert o.getTemp() <= 75


def test_fail():
    o = Engine()
    while o.rotations() < 50:
        pass
    assert o.getTemp() <= 70


def test_error():
    o = Engine()
    while o.rotations() < 50:
        pass
    raise RuntimeError()
    assert o.getTemp() <= 75
