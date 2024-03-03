#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.extend([title] * quantity)

  def apply_discount(self):
    if self.discount > 0:
        self.total -= (self.total * self.discount) // 100
        if self.total == 0:
            print("After the discount, the total comes to $0.")
        else:
            print(f"After the discount, the total comes to ${self.total}.")
    else:
        print("There is no discount to apply.")

  # def void_last_transaction(self):
  #   if self.items:
  #       last_item_title, last_item_price = self.items.pop()
  #       self.total -= last_item_price
        
    def void_last_transaction(self):
      if self.items:
        last_item_title, last_item_price = self.items[-1]
        self.total -= last_item_price
        if len(self.items) == 1:
            self.items.pop()
        else:
            self.items[-1] = (last_item_title, last_item_price - self.items[-1][1])
        if self.items[-1][1] == 0:
            self.items.pop()

