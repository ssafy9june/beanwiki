import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

def recommend(search):
    data = pd.read_csv('movies.csv', encoding='utf-8')
    data = data[['id', 'title', 'genres', 'vote_average', 'vote_count', 'popularity','keywords','actors']]

    m = data['vote_count'].quantile(0.23)
    C = data['vote_average'].mean()

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        return (v / (v + m) * R) + (m / (m + v) * C)

    data['score'] = data.apply(weighted_rating, axis=1)

    data['genres'] = data['genres'].apply(literal_eval)
    data['genres'] = data['genres'].apply(lambda x: [d['name'] for d in x]).apply(lambda x: " ".join(x))

    data['actors'] = data['actors'].apply(literal_eval)
    data['actors'] = data['actors'].apply(lambda x: [d['name'] for d in x]).apply(lambda x: " ".join(x))

    data['keywords'] = data['keywords'].apply(literal_eval)
    data['keywords'] = data['keywords'].apply(lambda x: [d['name'] for d in x]).apply(lambda x: " ".join(x))

    count_vector = CountVectorizer(ngram_range=(1, 5))
    c_vector_genres = count_vector.fit_transform(data['actors'])
    # count_vector = CountVectorizer(ngram_range=(1, 3))
    # c_vector_genres = count_vector.fit_transform(data['genres'])

    gerne_c_sim = cosine_similarity(c_vector_genres, c_vector_genres).argsort()[:, ::-1]


    def get_recommended_movie_list(df, movie_title, top=30):
        target_movie_indices = df[df['title'] == movie_title].index.values
        sim_indices = gerne_c_sim[target_movie_indices, :top].reshape(-1)
        sim_indices = sim_indices[sim_indices != target_movie_indices]
        result = df.iloc[sim_indices].sort_values('score', ascending=False)[:30]
        return result


    # print("마음에 들었던 영화를 조건에 맞게 입력하세요:")
    # movie = input()
    movie = search
    temp = get_recommended_movie_list(data, movie_title=movie)
    ans = []
    ans = temp.values.tolist()
    ans = array(ans)

    # for i in range(10):
    #     if i == 0:
    #         print('%50s %40s %35s %20s %14s %20s' % ('title', 'genres', 'vote_average', 'vote_count', 'popularity', 'score'))
    #     else:
    #         print('%60s %50s %20s %20s %20.4s %20.4s' % (ans[i][1], ans[i][2], ans[i][3], ans[i][4], ans[i][5], ans[i][6]))

    # [0] id, [1] title, [2] gernes, [3] vote_average, [4] vote_count, [5] popularity, [6] keywords, [7] actors, [8] score 
    js = []
    for i in ans:
        js.append({'id' : i[0],'title': i[1], 'genres':i[2],'vote_average': i[3], 'vote_count' : i[4], 'popularity': i[5],'score' : i[8]})
    # print(fi - st)
    # return json.dumps(js,ensure_ascii=False)
    return js

