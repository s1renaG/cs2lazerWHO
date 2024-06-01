from demoparser2 import DemoParser
import json


class DemToJson:

    def __init__(self, demo_path):
        self.demo_path = demo_path

    def dem_to_json(self):

        parser = DemoParser(demo_path)

        event_df = parser.parse_event("player_death", player=["X", "Y"], other=["total_rounds_played"])
        ticks_df = parser.parse_ticks(["X", "Y"])
        game_df = parser.parse_event("player_death", other=["game_time", "round_start_time"])
        game_df["player_died_time"] = game_df["game_time"] - game_df["round_start_time"]

        event_dict = event_df.to_dict(orient='records')
        ticks_dict = ticks_df.to_dict(orient='records')
        game_dict = game_df.to_dict(orient='records')

        data = {
            "events": event_dict,
            "ticks": ticks_dict,
            "game_time": game_dict
        }

        with open("match_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print('Data being printed to your json')
        return


demo_path = "/Users/vitaliy/Documents/demos/lazerdogs.dem"
dem_to_json_instance = DemToJson(demo_path)
dem_to_json_instance.dem_to_json()
