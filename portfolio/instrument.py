from dataclasses import dataclass
from datetime import datetime


@dataclass
class Instrument:
    seccode: str
    lots: int = 1
    currency: str = "RUB"
    minstep: float = 0.01
    amount: int = 0
    ask: float | None = None
    bid: float | None = None
    spread: float | None = None
    mean_price: float | None = None
    value: float | None = None
    last_deal_price: float | None = None

    def calculate_spread(self):
        if self.ask is not None and self.bid is not None:
            self.spread = self.ask - self.bid

    def calculate_mean_price(self):
        if self.ask is not None and self.bid is not None:
            self.mean_price = (self.ask + self.bid) / 2

    def calculate_position_value(self):
        if self.mean_price is not None:
            self.value = self.mean_price * self.amount

    def update_quatations(self, ask: float | None = None, bid: float | None = None):
        if ask is not None:
            self.ask = ask
        if bid is not None:
            self.bid = bid
        self.calculate_spread()
        self.calculate_mean_price()
        self.calculate_position_value()


@dataclass
class Bond(Instrument):
    nominal: float = 1000
    nkd: float = 0
    coupon_date: datetime | None = None
    coupon_value: float | None = None

    def calculate_position_value(self):
        if self.mean_price is not None:
            self.value = ((self.mean_price * self.nominal/100) + self.nkd) * self.amount
