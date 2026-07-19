from PySide6.QtWidgets import (
    QMainWindow, QLabel, QLineEdit,
    QPushButton, QWidget,
    QVBoxLayout, QHBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.index_pokemon = 0

        self.pokemons = [
            {
                "nom": "Pikachu",
                "type": "Électrik",
                "description": "Un Pokémon de type Électrik.",
                "image": "assets/Images/Pokémon_Pikachu_art.png"
            },
            {
                "nom": "Bulbizarre",
                "type": "Plante / Poison",
                "description": "Un Pokémon de type Plante.",
                "image": "assets/Images/bulbasaur.png"
            },
            {
                "nom": "Dracaufeu",
                "type": "Feu / Vol",
                "description": "Un puissant Pokémon de type Feu.",
                "image": "assets/Images/charizard.png"
            }
        ]

        self.setup_window()
        self.create_widgets()
        self.create_layout()
        self.connect_signals()

        self.afficher_pokemon()
    def setup_window(self):
        self.setWindowTitle("PokeAtlas")
        self.resize(900, 600)

    def create_widgets(self):

        #  Images

        pokedex = QPixmap("assets/Images/Pokedex.png")
        pokedex = pokedex.scaled(200, 200)

        self.label_pokedex = QLabel()
        self.label_pokedex.setPixmap(pokedex)

        image = QPixmap("assets/Images/Pokémon_Pikachu_art.png")
        image = image.scaled(350, 350)

        self.label_image = QLabel()
        self.label_image.setPixmap(image)

        #  Recherche 

        self.campo_busqueda = QLineEdit()
        self.campo_busqueda.setPlaceholderText("Rechercher un Pokémon...")
        self.campo_busqueda.setFixedWidth(250)

        #  Informations 

        self.label_nom = QLabel("Pikachu")
        self.label_type = QLabel("Type : Electric")
        self.label_description = QLabel("Raton amarillo")

        #  Boutons 

        self.button_precedent = QPushButton("◀ Précédent")
        self.button_suivant = QPushButton("Suivant ▶")

    def create_layout(self):

        #  Logo

        logo_layout = QHBoxLayout()
        logo_layout.addStretch()
        logo_layout.addWidget(self.label_pokedex)
        logo_layout.addStretch()

        # Recherche 

        search_layout = QHBoxLayout()
        search_layout.addStretch()
        search_layout.addWidget(self.campo_busqueda)
        search_layout.addStretch()

        #  Image 

        image_layout = QVBoxLayout()
        image_layout.addWidget(self.label_image)
        image_layout.setAlignment(Qt.AlignTop)

        #  Informations 

        self.label_nom.setWordWrap(True)
        self.label_type.setWordWrap(True)
        self.label_description.setWordWrap(True)

        self.label_nom.setAlignment(Qt.AlignLeft)
        self.label_type.setAlignment(Qt.AlignLeft)
        self.label_description.setAlignment(Qt.AlignTop)

        infos_layout = QVBoxLayout()

        infos_layout.addWidget(self.label_nom)
        infos_layout.addSpacing(15)

        infos_layout.addWidget(self.label_type)
        infos_layout.addSpacing(20)

        infos_layout.addWidget(self.label_description)
        infos_layout.addStretch()

        # Zone Pokémon

        pokemon_layout = QHBoxLayout()

        pokemon_layout.addStretch()

        pokemon_layout.addLayout(image_layout)

        pokemon_layout.addSpacing(60)

        pokemon_layout.addLayout(infos_layout)

        pokemon_layout.addStretch()

        #  Boutons 

        buttons_layout = QHBoxLayout()

        buttons_layout.addStretch()

        buttons_layout.addWidget(self.button_precedent)

        buttons_layout.addSpacing(30)

        buttons_layout.addWidget(self.button_suivant)

        buttons_layout.addStretch()

        # Layout principal 

        main_layout = QVBoxLayout()

        main_layout.addSpacing(10)
        main_layout.addLayout(logo_layout)

        main_layout.addSpacing(20)
        main_layout.addLayout(search_layout)

        main_layout.addSpacing(30)
        main_layout.addLayout(pokemon_layout)

        main_layout.addStretch()

        main_layout.addLayout(buttons_layout)

        main_layout.addSpacing(15)

        container = QWidget()
        container.setLayout(main_layout)

        self.setCentralWidget(container)
    
    def connect_signals(self):

        self.button_suivant.clicked.connect(self.pokemon_suivant)

        self.button_precedent.clicked.connect(self.pokemon_precedent)

    def pokemon_suivant(self):
        if self.index_pokemon <  len(self.pokemons) - 1 :
            self.index_pokemon += 1
        print(self.index_pokemon)
        self.afficher_pokemon()
    
    def pokemon_precedent(self):
        if self.index_pokemon > 0 :
            self.index_pokemon -= 1
        print(self.index_pokemon)
        self.afficher_pokemon()
    def afficher_pokemon(self):

        pokemon = self.pokemons[self.index_pokemon]

        self.label_nom.setText(pokemon["nom"])
        self.label_type.setText(pokemon["type"])
        self.label_description.setText(pokemon["description"])

        poke = QPixmap(pokemon["image"])
        poke = poke.scaled(200, 200)

        self.label_image.setPixmap(poke)
