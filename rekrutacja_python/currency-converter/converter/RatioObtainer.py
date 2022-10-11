import json, datetime, urllib.request, os, requests
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise

        if not os.path.exists("ratios.json"):
            return False

        with open("ratios.json") as ratios:
            data = json.load(ratios)

        for ratio in data:
            if ratio["base_currency"] == self.base and \
                ratio["target_currency"] == self.target and \
                ratio["date_fetched"] == datetime.date.today():
                    return True
                
    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it

        url = f"https://api.exchangerate.host/latest?base={self.base}&symbols={self.target}"
        response = requests.get(url)
        currency_data = response.json()
        ratio = float(currency_data["rates"][self.target])
        self.save_ratio(ratio)

    def make_dict(self, ratio, base, target):
        return {"base_currency": base, \
            "target_currency": target, \
            "date_fetched": str(datetime.date.today()), \
            "ratio": ratio}

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        
        with open("ratios.json") as ratios:
            data = json.load(ratios)

        for ratioNode in data:
            if ratioNode["base_currency"] == self.base and \
                ratioNode["target_currency"] == self.target:    
                    ratioNode["ratio"] = ratio
                    ratioNode["date_fetched"] = str(datetime.date.today())
                    with open("ratios.json", 'w') as ratios:
                        json.dump(data, ratios)
                    return

        data.append(self.make_dict(ratio, self.base, self.target))      

        with open("ratios.json", 'w') as ratios:
            json.dump(data, ratios)

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        
        with open("ratios.json") as ratios:
            data = json.load(ratios)
            for ratioNode in data:
                if ratioNode["base_currency"] == self.base and \
                    ratioNode["target_currency"] == self.target:
                        return ratioNode["ratio"]
        