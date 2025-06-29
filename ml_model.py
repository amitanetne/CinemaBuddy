import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#load CSV
df = pd.read_csv("moviesList.csv") # add our csv name here
#data cleaning
df = df[df['Total_Gross'].str.startswith('$')].copy()
df['Total_Gross'] = df['Total_Gross'].str.replace('[$M]', '', regex=True).astype(float)

# if total gross>500 -> hit else flop
df['Hit_or_Flop'] = df['Total_Gross'].apply(lambda x: 'Hit' if x >= 500 else 'Flop')

# encoding features
features = ['Director', 'Actors', 'Censor', 'main_genre', 'Runtime(Mins)']
for col in ['Director', 'Actors', 'Censor', 'main_genre']:
    df[col] = df[col].astype('category')

X = df[features].copy()

# convert features to codes
for col in ['Director', 'Actors', 'Censor', 'main_genre']:
    X[col] = X[col].cat.codes

# targets as y
y_rating = df['Rating']
y_gross = df['Total_Gross']

# train test spilt
X_train, X_test, y_rating_train, y_rating_test, y_gross_train, y_gross_test = train_test_split(X, y_rating, y_gross, test_size=0.2, random_state=42)

# model training
model_rating = LinearRegression()    # rating
model_rating.fit(X_train, y_rating_train)

model_gross = LinearRegression()     # gross
model_gross.fit(X_train, y_gross_train)

# encode user inputs 
def encode_input(value, col, df):
    value = value.strip().lower()
    categories = [str(cat).lower() for cat in df[col].cat.categories]

    if col == 'Actors':
        input_actors = [actor.strip().lower() for actor in value.split(',')]
        for idx, cat in enumerate(categories):
            if any(actor in cat for actor in input_actors):
                return idx
        return -1
    else:
        if value in categories:
            return categories.index(value)
        else:
            return -1
 #for flask       
def make_prediction(director, actors, censor, genre, runtime):
    director_code = encode_input(director, 'Director', df)
    actors_code = encode_input(actors, 'Actors', df)
    censor_code = encode_input(censor, 'Censor', df)
    genre_code = encode_input(genre, 'main_genre', df)

    input_df = pd.DataFrame(
       [[director_code, actors_code, censor_code, genre_code, runtime]],columns=features
    )

    rating_pred = model_rating.predict(input_df)[0]
    gross_pred = model_gross.predict(input_df)[0]
    hit_flop = 'Hit' if gross_pred >= 500 else 'Flop'

    return rating_pred, gross_pred, hit_flop


