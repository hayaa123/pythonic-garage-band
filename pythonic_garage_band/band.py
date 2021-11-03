
from abc import abstractmethod


class Musician:

    def __init__(self, name):
        self.name = name

    def __repr__(self, type):
        if type:
            return f"{type} instance. Name = {self.name}"
        else:
            return f"musican instance. Name = {self.name}"

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass



class Guitarist(Musician):
    instrument = "guitar"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return super().__repr__("Guitarist")

    def get_instrument(self):
        return self.instrument
    @abstractmethod
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    instrument = "bass"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return super().__repr__("Bassist")

    def get_instrument(self):
        return self.instrument
    
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    instrument = "drums"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return super().__repr__("Drummer")

    def get_instrument(self):
        return self.instrument

    def play_solo(sels):
        return "rattle boom crash"


class Band(Musician):

    instances=[]
    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        plays =[]
        for member in self.members:
            plays.append(member.play_solo())
        return plays

    @classmethod
    def to_list(cls):
        return cls.instances
   

if __name__ == "__main__":
    john = Bassist("john")
    print(repr(john))
