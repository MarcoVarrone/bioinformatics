from nucleic.type.purine import Purine


class Guanine(Purine):
    def __init__(self):
        super(Guanine, self).__init__("G")

    def __repr__(self):
        return 'A'
