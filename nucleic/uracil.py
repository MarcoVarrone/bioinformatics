from nucleic.type.pyrimidine import Pyrimidine


class Uracil(Pyrimidine):
    def __init__(self):
        super(Uracil, self).__init__("U")

    def __repr__(self):
        return 'T'
