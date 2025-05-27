The Movie Recommendation System is a Python-based project that suggests movies to
users based on their preferences.

The system leverages data from The Movie Database (TMDB) and utilizes machine learning
and natural language processing (NLP) techniques to recommend similar movies.

Additionally, it displays movie posters to enhance user experience.
The system is deployed using Streamlit, a lightweight web application framework, and
pickle for model storage.



Objectives
● To build a recommendation system that suggests movies based on user input.
● To fetch movie data, including posters, from TMDB.
● To provide an interactive and user-friendly interface using Streamlit.
● To apply machine learning and NLP techniques to improve recommendation
accuracy.


Technology Stack
Programming Language
Python
Libraries Used
● Pandas and NumPy for data manipulation
● Scikit-learn for machine learning (cosine similarity)
● NLTK for natural language processing (stemming, tokenization)
● Text vectorization techniques including Bag of Words
● Requests for fetching data from TMDB API
● Streamlit for building the web interface
● Pickle for saving and loading the trained model
Methodology
1. Data Collection:
○ Movie data is collected from TMDB, including titles, genres, descriptions, and
posters.
○ TMDB API is used to fetch real-time data.
2. Data Preprocessing:
○ Removing duplicates and missing values.
○ Feature extraction using text vectorization and Bag of Words for text-based
features.
○ Applying NLP techniques such as stemming to process text data.
3. Recommendation Generation:
○ The top similar movies are retrieved and displayed along with their
posters.
4. Deployment:
○ The system is deployed using Streamlit, providing an interactive UI for
users to search and receive recommendations.

Implementation Details
● Fetching Data :
The TMDB API is used to retrieve movie details dynamically.
● Natural Language Processing :
NLP Tools :
Movie descriptions are preprocessed using stemming and text vectorization
techniques.
Bag of Words is used for feature extraction.
● Machine Learning Model :
Cosine Similarity is used to find movies similar to the user’s choice by comparing
vectorized movie descriptions.
● User Interface :
○ Users input a movie name.
○ The system displays recommended movies with posters.
○ Streamlit provides an intuitive experience with minimal setup.
Results and Discussion
The system successfully recommends movies based on user input and provides visually
appealing results with posters. The use of TMDB data ensures real-time updates. The
integration of NLP techniques improves text-based similarity calculations. While the
recommendations are effective, future improvements can include hybrid filtering
techniques and deep learning models to enhance accuracy.

