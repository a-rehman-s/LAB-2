from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card Payment of Rs. {amount}")

class PaypalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Paypal Payment of Rs. {amount}")

payment = CreditCardPayment()
payment.process_payment(1000)
