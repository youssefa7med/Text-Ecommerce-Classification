# Text Ecommerce Classification

![Text Ecommerce Classification](https://th.bing.com/th/id/R.22a952145b87318bfe3f151c5f8acb6f?rik=oaY6dpZQrkw1Qg&pid=ImgRaw&r=0)

This project involves classifying ecommerce text data to uncover insights into product categories, customer reviews, and more. Using advanced text analysis techniques and machine learning algorithms, this application provides valuable insights for businesses, analysts, and data scientists.

## Overview

The Text Ecommerce Classification project aims to classify ecommerce-related text data, such as product descriptions and customer reviews, into predefined categories. The application uses various machine learning models and techniques to build an effective classification system.

### Key Features

- **Text Data Preprocessing**:
  - Tokenization, lemmatization, and vectorization of text data.
  - Use of TF-IDF for converting text into numerical features.

- **Model Training and Evaluation**:
  - Training and evaluation of different classification models including Random Forest, Naive Bayes, and K-Nearest Neighbors.
  - Hyperparameter tuning using Randomized Search.

- **Interactive Analysis**:
  - Detailed analysis of model performance and feature importance.
  - Comparison of different models based on classification metrics.

## Analysis

### Text Data Preprocessing

- **Tokenization and Lemmatization**:
  - Use of `spacy` for processing and preparing text data.

- **Vectorization**:
  - Conversion of text data into numerical format using `TfidfVectorizer`.

### Model Training and Evaluation

- **Classification Models**:
  - **Random Forest Classifier**: An ensemble method that builds multiple decision trees and combines their results.
  - **Naive Bayes Classifier**: Probabilistic model based on Bayes’ theorem for text classification.
  - **K-Nearest Neighbors (KNN)**: A non-parametric method that classifies data based on the majority vote of its neighbors.

- **Hyperparameter Tuning**:
  - Use of `RandomizedSearchCV` for optimizing hyperparameters of the models.

### Interactive Analysis

- **Model Performance**:
  - Evaluation of model performance using metrics such as precision, recall, and F1-score.
  - Analysis of feature importance and model predictions.

## Technologies Used

- **Python**: Core programming language for data analysis and machine learning.
- **pandas**: For data manipulation and analysis.
- **spacy**: For natural language processing tasks.
- **sklearn**: For machine learning algorithms and tools.
- **scipy**: For statistical functions and distributions.
- **Streamlit**: For creating interactive web applications and visualizations (if applicable).

## Live Application

Explore the Text Ecommerce Classification tool directly through the following application: [Text Ecommerce Classification](#).

## Getting Started

### Prerequisites

Ensure you have Python installed, along with the required libraries listed in the `requirements.txt` file.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/youssefa7med/TextEcommerceClassification.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd TextEcommerceClassification
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Prepare Data**:
   - Ensure your text data is properly formatted and placed in the appropriate directory.

2. **Run the Script**:
   ```bash
   python app.py
   ```

## Usage

1. **Model Training**:
   - Train and evaluate classification models using the provided scripts.

2. **Analysis**:
   - Analyze model performance and explore classification results.

## Contributing

Contributions are welcome! If you have suggestions for improvements, additional features, or bug fixes, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. For more information, please refer to the [LICENSE](LICENSE) file.

## Acknowledgments

Special thanks to the open-source community and contributors for the tools and libraries that made this project possible. Your support has been invaluable in developing and enhancing this classification system.

