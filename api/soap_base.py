from zeep import Client


class SoapBase:
    def __init__(self, wsdl):
        self.client = Client(wsdl)
