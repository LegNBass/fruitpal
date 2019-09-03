# FruitPal

### To Run:
- `docker-compose up --build` if docker/docker-compose are installed and running.
    - Then send a GET request to `localhost:8080/<commodity>/<price_per_ton>/<trade_volume>`
    - An example command that shold work once the service is running is: `curl localhost:8080/mango/53/405`
- If you do not have docker/docker-compose, you can still calculate the result as a script
    - From the top-level fruitpal directory just run `python3 app/fruitpal.py <commodity> <price_per_ton> <trade_volume>`
    - This assumes that the JSON data is located in `./data/fruit_data.json` but an alternate path can be supplied with the `--path` argument
    - An example command for running as a script is `python3 app/fruitpal.py mango 53 405`
- To test: `python3 -m pytest tests/unit.py`
    