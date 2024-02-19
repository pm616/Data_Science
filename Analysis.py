
import kaggle as kg
import pandas as pd
import matplotlib.pyplot as plt
import yaml
import requests
import logging
from kaggle.api.kaggle_api_extended import KaggleApi



class Analysis():

    def __init__(self, analysis_config: str) -> None:
        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)

        self.config = config

    def load_data(self) -> None:
        data = requests.get('https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries/download?datasetVersionNumber=1').json()
        self.dataset = data
        print(self.dataset)
    
    def load_kaggle(self):
        api = KaggleApi()
        authentication = api.authenticate()
        api.dataset_download_files('hummaamqaasim/jobs-in-data', unzip=True)
        path = '/Users/pavla/Documents/Data_Science_program/Assigments/Building Robust Software/data_science/jobs_in_data.csv'
        df = pd.read_csv('jobs_in_data.csv', encoding='ISO-8859-1')
        assert isinstance(df, pd.DataFrame), "error loading csv, not a dataframe"


    def compute_analysis(self) -> max:
        print(self.dataset.max())
    
        # Location_group = df.groupby(['employee_residence','experience_level']).agg(salary_count = ('salary_in_usd','count'),salary_mean = ('salary_in_usd','mean'))
        # Location_group.head()

    def plot_data(self, save_path: [str] = None) -> plt.Figure: # type: ignore
        df = pd.read_csv('jobs_in_data.csv')
        fig, ax = plt.subplots()
        plt.style.use('seaborn-v0_8-darkgrid')
        ax.bar(df['experience_level'], df['salary'])
        ax.set_title('Jobs and Salaries in Data Science', fontsize=24)
        ax.set_xlabel('Experience level', fontsize=14)
        ax.set_ylabel('salary', fontsize=14)
        ax.tick_params(axis='both', which='major', labelsize=16, pad=12)
        plt.savefig('/Users/pavla/Documents/Data_Science_program/Assigments/Building Robust Software/data_science/data_science_salary.jpg')



    def notify_done(self, message: str) -> None:
        topicname = 'Data science'
        message = 'Data Science from Pav'
        requests.post(f"https://ntfy.sh/{topicname}", 
        data=message.encode(encoding='utf-8'))
        