
from recommender.food_recommender import FoodRecommender

def main():
  recommender = FoodRecommender("data/food.csv")
  print("Recommendations for type='Dessert', occasion='Party':")
  print(recommender.recommend(type='Dessert', occasion='Party'))

if __name__ == "__main__":
  main()
