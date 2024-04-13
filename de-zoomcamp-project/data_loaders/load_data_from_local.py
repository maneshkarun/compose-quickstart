from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    filepath = 'product_hunt_products.csv'

    df_dtype = {
                    '_id': str,
                    'name': str,
                    'product_description': str,
                    'product_ranking':pd.Int64Dtype(),
                    'main_image':str,
                    'images': str,
                    'upvotes': pd.Int64Dtype(),
                    'comments':str,
                    'websites':str,
                    'category_tags':str,
                    'hunter':str,
                    'makers':str
                }
    parse_dates = ['release_date','product_of_the_day_date','last_updated']

    df = pd.read_csv(filepath, dtype=df_dtype, parse_dates=parse_dates)
    kwargs['df'] = df
    return df
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
