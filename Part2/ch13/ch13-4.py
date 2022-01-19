class Horse:
    def __init__(self, name, rider) -> None:
        self.name = name
        self.rider = rider


class Rider:
    def __init__(self, name) -> None:
        self.name = name


rd1 = Rider("Umazo")
uma1 = Horse("Umako", rd1)

print(uma1.rider.name)
