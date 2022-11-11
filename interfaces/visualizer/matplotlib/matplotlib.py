import matplotlib.pyplot as plt
from collections import Counter
from interfaces.db.utils.data_helper import preprocess_epoch_to_buckets
from datetime import datetime

def create_bar_graph(data, output_file):
    """
    Create a bar graph listing the per-minute count of issues created.
    """
    y, start_time = preprocess_epoch_to_buckets(data)
    start_time_str = datetime.fromtimestamp(start_time)
    plt.bar(list(range(60)), y)
    plt.xlabel('Minutes')
    plt.ylabel('High priority ticket count')
    plt.title('Frequency of High priority tickets since {}'.format(start_time_str))
    plt.savefig(output_file)
