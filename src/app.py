import os

from flask import Flask

import fruitpal

app = Flask(__name__)


@app.route('/hello/<string:name>', methods=['POST'])
def hello(name):
    return f"Hello {name}"


@app.route('/<string:commodity>/<int:price_per_ton>/<int:trade_volume>', methods=['POST'])
def _fruitpal(commodity, price_per_ton, trade_volume):
    return fruitpal.list_results(commodity, price_per_ton, trade_volume)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=os.environ.get('DEBUG', False)
    )
