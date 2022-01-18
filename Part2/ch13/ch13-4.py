"""Composition
"""

class Horse:
    def __init__(self,name,rider) -> None:
        self.name = name
        self.rider = rider


class Rider:
    def __init__(self,name) -> None:
        self.name = name


rd = Rider('tadao')

uma = Horse('umako',rd)

print(uma.name.rider)
