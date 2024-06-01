import json
import pandas as pd


class GetLifeSpan:
    def get_death_data(self, json_file, team="TERRORIST"):
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
                        life_time = event.get("player_died_time")
                        victim_team = event.get("user_team_name")
                        if victim_team == team:
                            death_records.append({
                                "attacker": attacker_name,
                                "victim": victim_name,
                                "lifetime": life_time,
                                "weapon": weapon
                            })
                if not death_records:
                    print("No death events found for the specified team in the data.")
            else:
                print("No events found in the data.")

            return death_records

        except FileNotFoundError:
            print(f"The file '{json_file}' was not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON in '{json_file}'. Ensure the file contains valid JSON.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []


lifespan = GetLifeSpan()
death_records = lifespan.get_death_data('match_data.json', team='TERRORIST')
if death_records:
    df_death = pd.DataFrame(death_records)
    df_death.to_csv('time_to_die.csv', mode='w', index=False)
