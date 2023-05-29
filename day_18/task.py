class Distance:
    def __init__(self, in_kms):
        self.in_kms = in_kms

    @classmethod
    def into_kms(cls, miles): #this is a factory method
        in_kms = miles * 1.6
        return cls(miles * 1.6)
d1 = Distance(4)
print(d1.in_kms)
d2 = Distance.into_kms(4) #here input is 4 miles
print(d2.in_kms)