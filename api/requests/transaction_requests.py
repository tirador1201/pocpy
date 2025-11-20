from api.models.transaction_models import CashOutTransactionStatusRequest, TransactionStatusRequest
from api.soap_base import SoapBase


class TransactionRequests(SoapBase):

    # old class GetCashOutTransactionStatus
    def get_cash_out_transaction_status(self, request: CashOutTransactionStatusRequest):
        return self.client.service.getCashOut(merchantId=request.merchantId,
                                              referenceNr=request.referenceNr,
                                              merchantKeyword=request.merchantKeyword)

    # old class GetTransactionStatus
    def get_transaction_status(self, request: TransactionStatusRequest):
        return self.client.service.getTransaction(merchantId=request.merchantId, referenceNr=request.referenceNr)
