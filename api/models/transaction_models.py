from pydantic import BaseModel


class CashOutTransactionStatusRequest(BaseModel):
    merchantId: str
    merchantKeyword: str
    referenceNr: str


class TransactionStatusRequest(BaseModel):
    merchantId: str
    referenceNr: str
