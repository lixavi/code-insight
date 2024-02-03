from code_review.code_reviewer import CodeReviewer
from machine_learning.ml_model import MLModel
from utils.data_loader import DataLoader
from utils.visualization import Visualization

def main():
    # Instantiate the code reviewer
    reviewer = CodeReviewer()

    # Perform code review
    reviewer.review_code()

    # Load data using DataLoader
    loader = DataLoader()
    data = loader.load_data("data.txt")

    # Train machine learning model
    model = MLModel()
    model.train(data)

    # Make predictions
    prediction = model.predict(data)

    # Visualize predictions
    visualizer = Visualization()
    visualizer.plot_prediction(prediction)

if __name__ == "__main__":
    main()
