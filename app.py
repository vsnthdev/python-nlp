from simple_chalk import chalk
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN
from intent_router import index

engine = SnipsNLUEngine(config=CONFIG_EN)
engine = engine.from_path("engine")

while True:
    response = input("👉 ")
    parsed = engine.parse(response)

    # handle graceful termination
    if parsed["intent"]["intentName"] == "terminate":
        print("")
        print("Bye bye 👋")
        exit()

    # logging
    color = chalk.green if parsed["intent"]["probability"] > 0.7 else chalk.red
    print(color("[" + str(parsed["intent"]["probability"]) + "]") + " " + chalk.gray(parsed["intent"]["intentName"]))
    
    # handling different intents through an intent_router
    index(response, parsed)

    print("")
