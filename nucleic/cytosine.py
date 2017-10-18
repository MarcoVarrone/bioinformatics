from nucleic.type.pyrimidine import Pyrimidine


class Cytosine(Pyrimidine):
    def __init__(self):
        super(Cytosine, self).__init__("C")

    def __repr__(self):
        return 'C'
