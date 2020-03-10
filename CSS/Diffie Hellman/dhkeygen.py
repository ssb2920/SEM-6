"""
Name:Shubham Bhate
roll no:8318
"""
class DH:
    def __init__(self, p, g):
        self.p = p
        self.g = g

    def ABVal(self, secret):
        return (self.g ** secret) % self.p

    def KeyGen(self, ctext, secret):
        return (ctext ** secret) % self.p