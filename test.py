import json
import pandas as pd


class GetLifeSpan:
    def get_death_data(self, json_file):
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

            death_records = []
            round_data = data.get("events")
            if round_data:
                for event in round_data:
                    death_tick = event.get("tick")
                    if death_tick is not None:
                        attacker_name = event.get("attacker_name")
                        victim_name = event.get("user_name")
                        weapon = event.get("weapon")
                        death_records.append({
                            "attacker": attacker_name,
                            "victim": victim_name,
                            "weapon": weapon
                        })
                if not death_records:
                    print("No death events found in the data.")
            else:
                print("No events found in the data.")

            lifetime_records = []
            lifetime_data = data.get("game_time")
            if lifetime_data:
                for time_data in lifetime_data:
                    life_time = time_data.get("player_died_time")
                    if life_time is not None:
                        lifetime_records.append({
                            "lifetime": life_time
                        })

            return {"death_records": death_records, "lifetime_records": lifetime_records}

        except FileNotFoundError:
            print(f"The file '{json_file}' was not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON in '{json_file}'. Ensure the file contains valid JSON.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}


lifespan = GetLifeSpan()
record_dict = lifespan.get_death_data('match_data.json')
if record_dict:
    df_death = pd.DataFrame(record_dict["death_records"])
    df_lifetime = pd.DataFrame(record_dict["lifetime_records"])

    combined_df = pd.concat([df_death, df_lifetime], axis=1)
    combined_df.to_csv('time_to_die.csv', mode='w', index=False)
