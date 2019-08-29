import os
import json

from collections import defaultdict


class Fruitpal:
    def __init__(self):
        self.prices = defaultdict(dict)
        self.bad_entries = {}

    def load_data(self, path=None):
        if not path:
            path = os.path.join(
                '/data',
                os.environ.get('DATA_FILE', 'fruit_data.json')
            )
        with open(
            path
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

    def calculate_and_list_prices(self, comm, ppt, t_vol, path=None):
        self.load_data(path=path)

        result_list = []
        for country, overhead in self.prices.get(comm, {}).items():
            total_ppt = ppt + overhead['variable']
            result_list.append((
                country,  # Country Code
                total_ppt * t_vol + overhead['fixed'],  # Total cost of trade
                f"({total_ppt}*{t_vol})+{overhead['fixed']}"  # Breakdown of trade cost calculation
            ))
        return result_list

    @staticmethod
    def format_data(result_list):
        return '\n'.join(
            f"{i[0]} {i[1]:.2f} | {i[2]}"
            for i in sorted(
                result_list,
                key=lambda x: x[1],
                reverse=True
            )
        )


if __name__ == '__main__':
    import argparse

    # Create a parser and add the required args for the script to run
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'commodity',
        help='The commodity to calculate prices for'
    )  # comm
    parser.add_argument(
        'price_per_ton',
        help='The price per ton of that commodity'
    )  # ppt
    parser.add_argument(
        'trade_volume',
        help='The number of tons to be purchased'
    )  # t_vol
    parser.add_argument(
        '--path',
        default='./data/fruit_data.json',
        help="The filepath to the JSON overhead data"
    )
    args = parser.parse_args()

    # Perform the actual calculation
    fp = Fruitpal()
    try:
        results = fp.calculate_and_list_prices(
            args.commodity,
            float(args.price_per_ton),
            float(args.trade_volume),
            args.path
        )
        print(Fruitpal.format_data(results))
    except ValueError:
        print(
            "Arguments were not in the required format.\n"
            "Try running again with -h or --help for more information."
        )
