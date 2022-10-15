#
#  Contains functions that handle different intents.
#  Created On 15 October 2022
#

def bio_shared(res: str, parsed: dict):
    if parsed["intent"]["intentName"] != "set_bio":
        return

    starts_at = parsed["slots"][0]["range"]["start"]
    print(res[starts_at:])

def keyword_shared(res: str, parsed):
    if parsed["intent"]["intentName"] != "add_keyword":
        return
    
    print(parsed["slots"])

def index(res: str, parsed: dict):
    bio_shared(res, parsed)
    keyword_shared(res, parsed)
