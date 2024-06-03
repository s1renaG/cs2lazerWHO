from json_demo_parser import JsonDemoParser
from life_span import LifeSpan

class DataExtractor:

    def __init__(self, folder_path, folder_to_save):
        self.folder_path = folder_path
        self.folder_to_save = folder_to_save

    def data_collector(self):
        dem_to_json_instance = JsonDemoParser(self.folder_path)
        dem_to_json_instance.process_demos_folder()
        life_span_instance = LifeSpan(self.folder_path, self.folder_to_save)
        life_span_instance.process_demos_folder()


