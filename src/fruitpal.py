def list_results(a, b, c):
    return f"MX {c} {b}"


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('fruit')
    parser.add_argument('price_per_ton')
    parser.add_argument('trade_volume')

    args = vars(parser.parse_args())

    print(args)
