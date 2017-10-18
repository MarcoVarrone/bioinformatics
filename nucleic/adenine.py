from nucleic.type.purine import Purine


class Adenine(Purine):
    def __init__(self):
        super(Adenine, self).__init__("A")

    def __repr__(self):
        return 'A'
