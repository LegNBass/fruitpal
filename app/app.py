import os

from flask import Flask
from werkzeug.routing import FloatConverter as BaseFloatConverter

import fruitpal


# Allows handling integers or floats in route
class FloatConverter(BaseFloatConverter):
    regex = r'-?\d+(\.\d+)?'


app = Flask(__name__)
# Apply the custom float regex
app.url_map.converters['float'] = FloatConverter


@app.route('/hello/<string:name>', methods=['POST'])
def hello(name):
    return f"Hello {name}"


@app.route('/<string:commodity>/<float:price_per_ton>/<float:trade_volume>', methods=['GET'])
def _fruitpal(commodity, price_per_ton, trade_volume):
    fp = fruitpal.Fruitpal()
    fp.load_data()
    results = fp.calculate_and_list_prices(
        commodity,
        price_per_ton,
        trade_volume
    )
    return fruitpal.Fruitpal.format_data(results)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=os.environ.get('DEBUG', False)
    )
