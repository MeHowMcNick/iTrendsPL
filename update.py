import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import scrap, os


dir_path = os.path.dirname(os.path.realpath(__file__))

def update(lang):
    try: 
        df = pd.read_json(os.path.join(dir_path, "data.json"))
        today = date.today()

        if df[(df["Date"] == today.isoformat()) & (df["Language"] == lang)].empty:
            offers = scrap.scrap_all(lang=lang)

            for i, j in offers.items():
                df = df.append({"Date": today,
                                "Website": i,
                                "Language": lang,
                                "Number of Offers": j
                                }, ignore_index=True)

            df.to_json(os.path.join(dir_path, "data.json"))
            return print("Database update completed for " + lang + ".")
        else:
            return print("Database for " + lang + " was updated today. Try tommorow.")

    except ValueError:
        df = pd.DataFrame(columns=["Date", "Website", "Language", "Number of Offers"])
        offers = scrap.scrap_all(lang=lang)

        for i, j in offers.items():
            df = df.append({"Date": date.today(),
                            "Website": i,
                            "Language": lang,
                            "Number of Offers": j
                            }, ignore_index=True)
        
        df.to_json(os.path.join(dir_path, "data.json"))
        return print("Database update completed for " + lang + ".")


def open():
    try:
        df = pd.read_json(os.path.join(dir_path, "data.json"))
        return print(df)
    except ValueError:
        return print("Sorry, database does not exist.")

'''
def plot():
    try:
        df = pd.read_json(os.path.join(dir_path, "data.json"))
        return print(df)
    except ValueError:
        return print("Sorry, database does not exist.")
'''