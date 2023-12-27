class TradeInfo:
    def __init__(self, trades):
        self.total = 0
        self.trades = []
        self._parse(trades)

    def _parse(self, trades):
        self.total = len(trades)
        self.trades = [self._map_to_trade(single) for single in trades]

    def _map_to_trade(self, single):
        time = single.create_datetime.strftime('%Y-%m-%d') if single.create_datetime else '未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
