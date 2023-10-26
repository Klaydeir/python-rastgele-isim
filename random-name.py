import random

def generate_name():
    first_names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard" "John", "Kadir", "Gürsoy", "Oğuzhan", "Ali", "Alparslan", "Recep", "Atilla", "Fırat", "Mahsun", "Necmettin", "Selim", "Yavuz", "Zülfü", "Selçuk", "Kadri", "Ahmet", "Uğur", "Pars", "Kara" "Tuncel"]
    last_names = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins" "Şahmeranoğulları" "Alemdar" "Uğur" "Ağaoğlu" "Anadolulu" "İvedik" "Fatihoğulları" "Albayram" "Erbakan" "Sarı" "Turgul" "Mercan" "Kartal" "Ulak" "Çakar" "Raksa"]
    return "{} {}".format(random.choice(first_names), random.choice(last_names))

for i in range(5):
    print(generate_name())