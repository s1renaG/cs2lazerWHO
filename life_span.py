import os
import json
import csv

class LifeSpan:

    def __init__(self, folder_path, folder_to_save):
        self.folder_path = folder_path
        self.folder_to_save = folder_to_save

    def get_death_data(self, json_file, team="TERRORIST"):
        filename = os.path.splitext(os.path.basename(json_file))[0] + ".csv"
        filepath = os.path.join(self.folder_to_save, filename)
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
                        current_round = event.get('total_rounds_played') + 1
                        if victim_team == team:
                            death_records.append({
                                "attacker": attacker_name,
                                "victim": victim_name,
                                "lifetime": life_time,
                                "weapon": weapon,
                                'current_round': current_round,
                            })
                if not death_records:
                    print("No death events found for the specified team in the data.")
            else:
                print("No events found in the data.")

            # Write death records to a CSV file
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = ["attacker", "victim", "lifetime", "weapon", "current_round"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for record in death_records:
                    writer.writerow(record)
            print(f"Death data written to {filepath}")

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

    def process_demos_folder(self):
        data_files = os.listdir(self.folder_path)
        json_files = [file for file in data_files if file.endswith('.json')]
        for json_file in json_files:
            json_file_path = os.path.join(self.folder_path, json_file)
            self.get_death_data(json_file_path)


