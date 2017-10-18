from nucleic.type.pyrimidine import Pyrimidine


class Thymine(Pyrimidine):
    def __init__(self):
        super(Thymine, self).__init__("T")

    def __repr__(self):
        return 'T'
