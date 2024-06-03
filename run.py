from data_extractor import DataExtractor

folder_path = '/Users/vitaliy/Documents/demos'
folder_to_save = '/Users/vitaliy/Documents/collected_data'
extract_data = DataExtractor(folder_path, folder_to_save)
extract_data.data_collector()
