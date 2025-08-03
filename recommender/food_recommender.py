
import pandas as pd
class FoodRecommender:
  def __init__(self, csv_path):
    self.data = pd.read_csv(csv_path)

  def recommend(self, type=None, occasion=None):
    result = self.data
    if type:
      result = result[result['type'].str.lower() ==type.lower()]
    if occasion:
      result = result[result['occasion'].str.lower() ==occasion.lower()]
    return result['food'].tolist()
