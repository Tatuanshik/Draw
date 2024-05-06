import os
import pandas as pd
import matplotlib.pyplot as plt


class Draw:
    def __init__(self, url, folder='plots'):
        self.url = url
        self.folder = folder

    def create_folder(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        return self.folder

    def create_dataframe(self):
        dataframe = pd.read_json(self.url)
        return dataframe

    def draw_plots(self):
        dataframe = self.create_dataframe()
        self.create_folder()
        paths = []
        for column in dataframe.columns:
            if dataframe[column].dtype in ['int64', 'float64']:
                path = os.path.join(self.folder, f'{column}.png')
                plt.rcParams['font.family'] = 'sans-serif'
                plt.figure(figsize=(7, 7), facecolor='gray')
                f = dataframe[column].plot(kind='hist', color='crimson', title=column.upper())
                f.set(facecolor='beige')
                f.grid(True)
                plt.xlabel('Value', size=14)
                plt.ylabel('Frequency', size=14)
                plt.savefig(path)
                plt.close()
                paths.append(path)
        return paths


def draw_plot(url):
    dif = Draw(url)
    paths = dif.draw_plots()
    plt.show()
    return paths


url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
print(draw_plot(url))
