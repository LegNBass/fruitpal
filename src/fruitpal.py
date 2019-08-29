import os
import json

from collections import defaultdict


class Fruitpal:
    def __init__(self):
        self.prices = defaultdict(dict)
        self.bad_entries = {}

    def load_data(self):
        with open(
            os.path.join(
                '/data',
                os.environ.get('DATA_FILE', 'fruit_data.json')
            )
        ) as f:
            data = json.load(f)
            for i in data:
                try:
                    overhead = {
                        'fixed': float(i['FIXED_OVERHEAD']),
                        'variable': float(i['VARIABLE_OVERHEAD'])
                    }
                    self.prices[i['COMMODITY']][i['COUNTRY']] = overhead
                except ValueError:
                    self.bad_entries = i

    def calculate_and_list_prices(self, comm, ppt, t_vol):
        self.load_data()

        result_list = []
        for country, overhead in self.prices.get(comm, {}).items():
            total_ppt = ppt + overhead['variable']
            result_list.append((
                country,  # Country Code
                total_ppt * t_vol + overhead['fixed'],  # Total cost of trade
                f"({total_ppt}*{t_vol})+{overhead['fixed']}"  # Breakdown of trade cost calculation
            ))
        return result_list


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('commodity')  # comm
    parser.add_argument('price_per_ton')  # ppt
    parser.add_argument('trade_volume')  # t_vol

    args = vars(parser.parse_args())

    print(args)
