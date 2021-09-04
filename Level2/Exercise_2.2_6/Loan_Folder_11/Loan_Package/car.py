'''
This class defines the Car class, derived from Asset.
'''

from Loan_Folder_11.Loan_Package.Asset import Asset


class Car(Asset):
    # (1) Initialization Functions
    def __init__(self, value):
        '''
        This initialization function to initialize a Car class.
        :param value:
        '''

        super(Car, self).__init__(value)

    def annualDepr(self):
        return .12

class Civic(Car):
    # (1) Initialization Functions
    def __init__(self, value):
        '''
        This initialization function to initialize a Civic.
        :param value:
        '''

        super(Civic, self).__init__(value)

    def annualDepr(self):
        return .13

class Lexus(Car):
    # (1) Initialization Functions
    def __init__(self, value):
        '''
        This initialization function to initialize a Lexus.
        :param value:
        '''

        super(Lexus, self).__init__(value)

    def annualDepr(self):
        return .19

class Lamborghini(Car):
    # (1) Initialization Functions
    def __init__(self, value):
        '''
        This initialization function to initialize a Lamborghini.
        :param value:
        '''

        super(Lamborghini, self).__init__(value)

    def annualDepr(self):
        return .28