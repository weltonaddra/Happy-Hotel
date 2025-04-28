class Guest:
    def __init__(self, id: int, name: str, email: str, phone: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone


    def to_dict(self):
        return self.__dict__
