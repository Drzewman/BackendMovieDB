import requests

from Request import Endpoint


def Request(title):
    response = requests.get(Endpoint.Endpoint.endpoint + title)
    if response.status_code != 200:
        print("Error while attempting to get data from api")
    data = response.json()
    film = data

    try:
        year = {'Year': data['Year'].strip('–')}
        film.update(year)
    except:
        na = {'Year': 'N/A'}
        film.update(na)
    try:
        rating = {'IMDb_Rating': data['Ratings'][0]['Value']}
        film.update(rating)
    except:
        na = {'IMDb_Rating': 'N/A'}
        film.update(na)
    try:
        cast = {'Cast': data['Actors']}
        film.update(cast)
    except:
        na = {'Cast': 'N/A'}
        film.update(na)
    try:
        votes = {'IMDb_Votes': data['imdbVotes'].replace(',','')}
        film.update(votes)
    except:
        na = {'IMDb_Votes': 'N/A'}
        film.update(na)
    try:
        boxoffice = {'BOX_OFFICE': data['BoxOffice'].strip('$').replace(',','')}
        film.update(boxoffice)
    except:
        na = {'BOX_OFFICE': 'N/A'}
        film.update(na)

    return film
