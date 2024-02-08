#create all morroco states and cities, just run the code once

from models import storage
from models.city import City
from models.state import State


storage.reload()

morocco_state = [
    {'name': 'Chaouia-Ouardigha', 'cities': ['Settat', 'Khouribga', 'Berrechid', 'Beni Mellal', 'Khénifra', 'Boujniba', 'Fquih Ben Salah', 'Benslimane', 'El Kelâa des Sraghna', 'Sidi Bennour', 'Dar Bel Amri']},
    {'name': 'Doukkala-Abda', 'cities': ['Safi', 'El Jadida', 'Azemmour', 'Khouribga', 'Oualidia', 'Sidi Bennour']},
    {'name': 'Fès-Boulemane', 'cities': ['Fès', 'Meknès', 'Sefrou', 'Taza', 'El Hajeb', 'Boulemane']},
    {'name': 'Gharb-Chrarda-Beni Hssen', 'cities': ['Kénitra', 'Sidi Kacem', 'Sidi Slimane', 'Sidi Yahya El Gharb', 'Sidi Smaïl', 'Sidi Allal El Bahraoui']},
    {'name': 'Grand Casablanca', 'cities': ['Casablanca', 'Mohammédia', 'Bouskoura', 'Benslimane', 'Mediouna', 'Tit Mellil']},
    {'name': 'Guelmim-Es Semara', 'cities': ['Guelmim', 'Assa', 'Tan-Tan', 'Sidi Ifni', 'Tata']},
    {'name': 'Laâyoune-Boujdour-Sakia El Hamra', 'cities': ['Laâyoune', 'Boujdour', 'Smara']},
    {'name': 'Marrakech-Tensift-Al Haouz', 'cities': ['Marrakech', 'Essaouira', 'Al Haouz', 'Chichaoua', 'El Kelâat Es-Sraghna']},
    {'name': 'Meknès-Tafilalet', 'cities': ['Meknès', 'Errachidia', 'Ifrane', 'El Hajeb', 'Khenifra', 'Midelt', 'Azrou']},
    {'name': 'Oriental', 'cities': ['Oujda', 'Nador', 'Berkane', 'Taourirt', 'Guercif', 'Jerada']},
    {'name': 'Oued Ed-Dahab-Lagouira', 'cities': ['Dakhla', 'Aousserd']},
    {'name': 'Rabat-Salé-Zemmour-Zaër', 'cities': ['Rabat', 'Salé', 'Skhirat', 'Témara', 'Khemisset', 'Sidi Kacem']},
    {'name': 'Souss-Massa-Drâa', 'cities': ['Agadir', 'Inezgane', 'Taroudannt', 'Tiznit', 'Chtouka Aït Baha', 'Tata', 'Tiznit']},
    {'name': 'Tadla-Azilal', 'cities': ['Beni Mellal', 'Fquih Ben Salah', 'Azilal', 'Khouribga', 'Kasba Tadla']},
    {'name': 'Tanger-Tétouan', 'cities': ['Tanger', 'Tétouan', 'Larache', 'Asilah', 'Chefchaouen']},
    {'name': 'Taza-Al Hoceima-Taounate', 'cities': ['Taza', 'Al Hoceïma', 'Taounate', 'Ouezzane', 'Guercif', 'Chefchaouen']}
]

for state in morocco_state:
    st = State(name=state['name'])
    st.save()
    for city in state['cities']:
        ct = City(name=city, state_id=st.id)
        ct.save()