from pydantic import BaseModel


class User(BaseModel):
    name: str
    mail: str
    address: str


class Banks(BaseModel):
    name: str
    rating: float = 0.0
    opened: str


class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: str


class Balance(BaseModel):
    card: Cards
    amount: int
    currency: str


user1 = User(name='Bob', mail='brooklynpookie@hotmail.com', address='1669 E 23rd St, Brooklyn, NY 11229, US')
bank1 = Banks(name='Chase', rating=4.7, opened='09.15.1995')
card1 = Cards(cardholder=user1, which_bank=bank1, opened='03.21.2023')
balance1= Balance(card=card1, amount=300, currency='USD')

print(vars(balance1))