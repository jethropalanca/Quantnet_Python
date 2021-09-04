'''
This class defines the HouseBase class, derived from Asset.
'''

from Exercise_5_2.Exercise_5_2_3.Loan_Package.asset import Asset

class HouseBase(Asset):
    # (1) Initialization Functions
    def __init__(self, value):
        '''
        This initialization function to initialize a HouseBase class.
        :param value:
        '''
        super(HouseBase, self).__init__(value)

    def annualDepr(self):
        return 0.2

class PrimaryHome(HouseBase):
    # (1) Initialization Functions
    def __init__(self, value):
        '''
        This initialization function to initialize a PrimaryHome class.
        :param value:
        '''
        super(PrimaryHome, self).__init__(value)

    def annualDepr(self):
        return .03636

class VacationHome(HouseBase):
    # (1) Initialization Functions
    def __init__(self, value):
        '''
        This initialization function to initialize a VacationHome class.
        :param value:
        '''
        super(VacationHome, self).__init__(value)

    def annualDepr(self):
        return .01584