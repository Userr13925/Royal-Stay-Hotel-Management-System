from enum import Enum
from datetime import datetime

class PaymentMethod(Enum):
    """Enumeration of payment methods"""
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    MOBILE_WALLET = "Mobile Wallet"
    BANK_TRANSFER = "Bank Transfer"
    CASH = "Cash"

class Payment:
    """Class representing a payment for a booking"""
    
    def __init__(self, payment_id: str, booking, amount: float, 
                 payment_method: PaymentMethod, payment_date: datetime = None):
        """
        Initialize a Payment object
        
        Args:
            payment_id (str): Unique payment identifier
            booking (Booking): Booking being paid for
            amount (float): Payment amount
            payment_method (PaymentMethod): Method of payment
            payment_date (datetime, optional): Date of payment. Defaults to current datetime.
        """
        self._payment_id = payment_id
        self._booking = booking
        self._amount = amount
        self._payment_method = payment_method
        self._payment_date = payment_date if payment_date else datetime.now()
        self._is_refunded = False
        self._refund_date = None
    
    @property
    def payment_id(self):
        return self._payment_id
    
    @property
    def booking(self):
        return self._booking
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def payment_method(self):
        return self._payment_method
    
    @property
    def payment_date(self):
        return self._payment_date
    
    def process_refund(self, amount: float = None):
        """Process a refund for this payment"""
        if self._is_refunded:
            raise ValueError("Payment is already refunded")
        
        refund_amount = amount if amount is not None else self._amount
        if refund_amount > self._amount:
            raise ValueError("Refund amount cannot exceed original payment")
        
        self._is_refunded = True
        self._refund_date = datetime.now()
        return refund_amount
    
    def __str__(self):
        status = "Refunded" if self._is_refunded else "Completed"
        return (f"Payment(ID: {self._payment_id}, Amount: ${self._amount:.2f}, "
                f"Method: {self._payment_method.value}, Status: {status}, "
                f"Date: {self._payment_date.strftime('%Y-%m-%d %H:%M:%S')})")