from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def payment(self, amount):
        pass



class PayPal(PaymentMethod):
    def payment(self, amount):
        return f"Paying {amount} using Paypal"
    
class CreditCardPayment(PaymentMethod):
    def payment(self, amount):
        return f"Paying {amount} using Credit Card"
    
class BitCoin(PaymentMethod):
    def payment(self, amount):
        return f"Paying {amount} using Bitcoin"
    

class ShoppingCart:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def checkout(self, amount):
        return self.payment_method.payment(amount)


if __name__ == "__main__":
    pay = ShoppingCart(CreditCardPayment())
    print(pay.checkout(100))

