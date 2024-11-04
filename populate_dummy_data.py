#!/usr/bin/env python3
"""
Dummy Data Insertion Script for SQLAlchemy

This script populates the 'person' table in a dummy database with
1,000,000 records of randomly generated data.
Each record consists of a randomly selected first name, last name, and age.
The first names and last names are chosen from a sample list representing
common US names, and the age is chosen from a range between 20 and 45.
"""
import os
import random
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base


# Define the SQLAlchemy base and model
Base = declarative_base()


class Person(Base):
    """
    Person model representing the 'person' table in the database.
    Fields:
    - id: Auto-incrementing primary key
    - firstname: String representing first name of the person
    - lastname: String representing last name of the person
    - age: Integer representing the age of the person
    """
    __tablename__ = 'person'
    id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    age = Column(Integer)


MYSQL_USER = os.getenv('DB_USER')
MYSQL_PWD = os.getenv('DB_PASSWORD')
MYSQL_HOST = os.getenv('DB_HOST')
MYSQL_DB = os.getenv('DB_NAME')
MYSQL_PORT = os.getenv('DB_PORT')
# Database connection setup
engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                       .format(MYSQL_USER,
                               MYSQL_PWD,
                               MYSQL_HOST,
                               MYSQL_PORT,
                               MYSQL_DB))
Session = sessionmaker(bind=engine)

# Sample list of 1,000 most common names
firstnames = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin",
    "Lucas", "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel",
    "Jacob", "Logan", "Jackson", "Sebastian", "Aiden", "Matthew", "Jack",
    "Owen", "Samuel", "David", "Joseph", "Carter", "John", "Wyatt", "Luke",
    "Gabriel", "Anthony", "Isaac", "Dylan", "Leo", "Lincoln", "Julian",
    "Asher", "Christopher", "Joshua", "Andrew", "Drew", "Theodore", "Caleb",
    "Ryan", "Adrian", "Jeremiah", "Nolan", "Derek", "Zachary", "Charles",
    "Jaxon", "Parker", "Max", "Hunter", "Jordan", "Cole", "Gavin", "Silas",
    "Xavier", "Ryder", "Tristan", "Austin", "Luca", "Jasper", "Elias",
    "Nicholas", "Sawyer", "Bentley", "Luis", "Diego", "Maverick", "Hayden",
    "Santiago", "Cameron", "Kaden", "Jaden", "Easton", "Landon", "Riley",
    "Zane", "Bodhi", "Kyrie", "Bennett", "Cruz", "Emmett", "Kylie", "Milo",
    "Braxton", "Kylan", "Nicolas", "Emilio", "Keegan", "Dalton", "Ezekiel",
    "Caden", "Jett", "Dante", "Damon", "Ronan", "Finley", "Cyrus", "Gideon",
    "Phoenix", "Chase", "Rory", "Ari", "Peyton", "Wesley", "Malachi", "Zion",
    "Avery", "Sawyer", "Lyla", "Lena", "Mila", "Ella", "Scarlett", "Aubrey",
    "Chloe", "Madison", "Sofia", "Aria", "Grace", "Isabella", "Riley",
    "Lillian", "Zoe", "Addison", "Camila", "Aaliyah", "Kinsley", "Nora",
    "Hannah", "Layla", "Ellie", "Samantha", "Stella", "Victoria", "Audrey",
    "Brooklyn", "Bella", "Lucy", "Paisley", "Claire", "Savannah", "Skylar",
    "Ariana", "Genesis", "Kaylee", "Mackenzie", "Sarah", "Allison", "Lydia",
    "Anna", "Charlotte", "Aurora", "Naomi", "Violet", "Emilia", "Ruby",
    "Madeline", "Jasmine", "Sophie", "Caroline", "Elena", "Rachel", "Mary",
    "Ivy", "Natalie", "Sienna", "Piper", "Luna", "Gia", "Tessa", "Maya",
    "Mila", "Cora", "Ashley", "Kimberly", "Emma", "Katherine", "Nicole",
    "Chloe", "Jordan", "Holly", "Daisy", "Megan", "Serenity", "Kimberly",
    "Isla", "Margaret", "Bailey", "Aubree", "Sadie", "Katherine", "Jade",
    "Ruth", "Ember", "Phoebe", "Melody", "Kayla", "Madison", "Lola", "Quinn",
    "Kendra", "Mariana", "Clara", "Miriam", "Sylvia", "Callie", "Lana",
    "Brooke", "Daphne", "Cecilia", "Arielle", "Zaria", "Jordyn", "Talia",
    "Brielle", "Bianca", "Marley", "Makenna", "Kaydence", "Rhea", "Sabrina",
    "Skye", "Laurel", "Esther", "Gianna", "Summer", "Emery", "Willa", "Hayley",
    "Freya", "Ashlyn", "Kaya", "Indigo", "Lindsey", "Diana", "Iris", "Bria",
    "Selah", "Amber", "Autumn", "Lilliana", "Journee", "Raegan", "Mikayla",
    "Alina", "Reagan", "Selene", "Erin", "Sandy", "Nadia", "Paige", "Blake",
    "Tatum", "Kira", "Marissa", "Zuri", "Journey", "Raven", "Giana", "Lacey",
    "Destiny", "Ayla", "Carmen", "Janelle", "Makenzie", "Noelle", "Alison",
    "Summer", "Reese", "Malia", "Jade", "Vivienne", "Rylie", "Dalia",
    "Caitlyn", "Gloria", "Alondra", "Dahlia", "Giselle", "Aubrielle",
    "Maddison", "Yasmin", "Allegra", "Nola", "Adley", "Ellis", "Mikayla",
    "Lillian", "Lana", "Yara", "Sasha", "Lia", "Kaylani", "Tenley", "Clio",
    "Bridget", "Esmeralda", "Iyla", "Aine", "Savanna", "Azaria", "Cynthia",
    "Luciana", "Estella", "Anaya", "Laylah", "Rosalie", "Kinley", "Rosalind",
    "Zaila", "Amira", "Kaia", "Karsyn", "Lailah", "Emery", "Bellamy",
    "Amara", "Gwendolyn", "Cassandra", "Wren", "Margo", "Mariana", "Opal",
    "Keira", "Kalani", "Adelina", "Amaris", "Alani", "Amaya", "Soleil",
    "Liora", "Emberly", "Dalia", "Emersyn", "Giovanna", "Leona", "Aspen",
    "Suri", "Dahlia", "Charleigh", "Sapphira", "Iliana", "Everlee", "Nina",
    "Kira", "Amaya", "Emery", "Sariah", "Ainsley", "Haisley", "Armani",
    "Selena", "Dahlia", "Ayla", "Livia", "Brinley", "Raegan", "Kylie", "Talia",
    "Kensley", "Aviana", "Zariyah", "Soleil", "Kylah", "Faye", "Elliott",
    "Emerie", "Yareli", "Ivana", "Amirah", "Cecily", "Camille", "Julieta",
    "Evie", "Raina", "Sarina", "Tia", "Blair", "Cleo", "Siena", "Kaliyah",
    "Astrid", "Lyric", "Ember", "Cleo", "Nayeli", "Elora", "Indie",
    "Bellatrix", "Alia", "Mira", "Chastity", "Mirabel", "Jovie", "Indigo",
    "Nylah", "Avianna", "Aimee", "Lysandra", "Maia", "Ellison", "Rowan",
    "Cypress", "Vesper", "Bria", "Callista", "Keilani", "Nya", "Petra",
    "Kensley", "Zinnia", "Galilea", "Briella", "Elowen", "Kalani", "Coral",
    "Ishani", "Selene", "Veda", "Ciel", "Mika", "Vera", "Giovanna", "Liora",
    "Zuri", "Amora", "Saskia", "Azura", "Mabel", "Niamh", "Petunia", "Zelda",
    "Carmen", "Fiona", "Opal", "Calla", "Clover", "Azalea", "Niamh", "Zara",
    "Elysia", "Lily", "Margot", "Thalia", "Celeste", "Bryony", "Soraya",
    "Selah", "Nova", "Shiloh", "Kaia", "Arwen", "Zadie", "Zara", "Gemma",
    "Octavia", "Eden", "Danica", "Kamryn", "Ember", "Cecilia", "Mira", "Yuna",
    "Kyrie", "Waverly", "Xanthe", "Layne", "Zuri", "Kaelyn", "Saige", "Alani",
    "Cypress", "Olive", "Selah", "Darcy", "Haven", "Misty", "Nia", "Esme",
    "Clementine", "Yara", "Carmela", "Paloma", "Reverie", "Sable", "Indie",
    "Zelda", "Lyric", "Honor", "Nola", "Calliope", "Zephyr", "Odessa",
    "Kaelani", "Allegra", "Carys", "Emberly", "Freya", "Juniper", "Fawn",
    "Lyra", "Amity", "Fable", "Roselyn", "Moxie", "Junie", "Tully", "Dory",
    "Zadie", "Raven", "Sonya", "Hattie", "Marigold", "Clarity", "Lyra",
    "Isolde", "Lark", "Clover", "Tamsin", "Zuri", "Misty", "Primrose", "Wren",
    "Briar", "Cleo", "Galadriel", "Cecily", "Liberty", "Zahara", "Valentina",
    "Cher", "Fleur", "Winter", "Marigold", "Elsie", "Seraphina", "Joy",
    "Lacey", "Jubilee", "Whitley", "Talisa", "Daffodil", "Harper", "Zinnia",
    "Ophelia", "Azura", "Clover", "Journey", "Skylar", "Emerson", "Harley",
    "Alia", "Greer", "Kaia", "Isolde", "Zara", "Libby", "Cressida", "Aurelia",
    "Adley", "Nyx", "Esme", "Samara", "Blossom", "Mikayla", "Daisy",
    "Serenity", "Valley", "Sadie", "Valentina", "Ivy", "Lyric", "Juniper",
    "Tansy", "Lilith", "Amaya", "Clementine", "Zelda", "Kensley", "Azalea",
    "Misty", "Clarity", "Nevaeh", "Heidi", "Everly", "Adalyn", "Haley",
    "Tatum", "Charity", "Lyra", "Juliette", "Lorelei", "Viola", "Celestia",
    "Blythe", "Isla", "Soleil", "Sonnet", "Zara", "Fleur", "Gloria", "Nia",
    "Bronwyn", "Elara", "Harlow", "Livia", "Sable", "Zadie", "Shiloh",
    "Kylie", "Alba", "Isha", "Azaria", "Sapphira", "Raina", "Kinley",
    "Aislinn", "Nylah", "Kyra", "Haven", "Meadow", "Clio", "Petra", "Asha",
    "Nika", "Tansy", "Aisling", "Cassia", "Kairi", "Kalani", "Zena", "Azura",
    "Valley", "Emberly", "Anouk", "Soleil", "Carys", "Giovanna", "Jessamy",
    "Kylah", "Celeste", "Alaina", "Sophie", "Amara", "Mabel", "Lyra",
    "Emmeline", "Vesper", "Coralie", "Nyx", "Arwen", "Zephyr", "Nia",
    "Sable", "Viola", "Willow", "Waverly", "Echo", "Daisy", "Asha", "Gemma",
    "Liberty", "Soleil", "Kaia", "Faye", "Suri", "Clover", "Alayna", "Calista",
    "Iona", "Carys", "Thalia", "Niamh", "Sky", "Margot", "Lyric", "Ginevra",
    "Sonnet", "Odessa", "Ophelia"
]
lastnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
    "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Hall", "Allen", "King",
    "Wright", "Scott", "Green", "Baker", "Adams", "Nelson", "Carter",
    "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker",
    "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers",
    "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper",
    "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray",
    "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price",
    "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Cole", "Jenkins",
    "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington",
    "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander",
    "Russell", "Griffin", "Diaz", "Hayes", "Myers", "Ford", "Hamilton",
    "Graham", "Sullivan", "Wallace", "Woods", "Coleman", "West", "Jordan",
    "Owens", "McBride", "Harrison", "Gibson", "Mcdonald", "Cruz", "Marshall",
    "Ortiz", "Gonzalez", "Nelson", "Ellis", "Stevens", "Santos", "Dunn",
    "Mclaughlin", "Mendez", "Bishop", "Cannon", "Holt", "Gonzales", "Burns",
    "Dixon", "Higgins", "Crawford", "Kelley", "Snyder", "Carlson", "Mason",
    "Glover", "Ramos", "Floyd", "Higgins", "Whitehead", "Sparks", "Nichols",
    "Murray", "Morris", "Pope", "Nash", "Hodge", "Patel", "Rios", "Hernandez",
    "Nunez", "Cameron", "Mack", "Bowers", "Tyler", "Underwood", "Barton",
    "Cannon", "Oneill", "Leach", "Rogers", "Bates", "Peters", "Sampson",
    "Wade", "Hardin", "Yang", "Fuentes", "Hodge", "Huerta", "Hwang",
    "Gonzales", "Melendez", "Rangel", "Rivas", "Sanchez", "Cervantes",
    "Maldonado", "Pacheco", "Romero", "Gil", "Bautista", "Acosta", "Bermudez",
    "Montoya", "Alvarez", "Duarte", "Avila", "Serrano", "Moreno", "Vega",
    "Guerrero", "Calderon", "Villanueva", "Salinas", "Ochoa", "Santos",
    "Rosales", "Luna", "Cruz", "Carrillo", "Cortez", "Flores", "Mendoza",
    "Mena", "Valencia", "Cisneros", "Salas", "Guevara", "Figueroa", "Mata",
    "Martinez", "Esquivel", "Alvarado", "Ramirez", "Gomez", "Trevino",
    "Duran", "Tovar", "Contreras", "Vargas", "Valenzuela", "Morales",
    "Hernandez", "Burgos", "Martinez", "Pineda", "Valenzuela", "Guerrero",
    "Montero", "Bermudez", "Martinez", "Lugo", "Gonzalez", "Salazar", "Orozco",
    "Rosario", "Ramos", "Castaneda", "Bocanegra", "Gonzalez", "Trevino",
    "Ortega", "Solis", "Zamora", "Rangel", "Tapia", "Ocampo", "Rivera",
    "Vasquez", "DeLeon", "DeJesus", "Delgado", "Jasso", "Lara", "Hernandez",
    "Marquez", "Castillo", "Medina", "Rodriguez", "Roman", "Lima", "Luna",
    "Moreno", "Cervantes", "Noriega", "Cantu", "Zuniga", "Cardenas",
    "Santana", "Pizarro", "Rios", "Mata", "Alvarez", "Solano", "Hernandez",
    "Alfaro", "Rodriguez", "Coronado", "Saldana", "Vega", "Vazquez", "Cruz",
    "Lozano", "Lopez", "Salinas", "Gonzalez", "Cabrera", "Espinoza",
    "Rodriguez", "Hernandez", "Juarez", "Salinas", "Rivas", "Quinones",
    "Gonzalez", "Olivares", "Gonzalez", "Grijalva", "Marroquin", "Reyes",
    "Medina", "Cantu", "Luna", "Rodriguez", "Morales", "Nava", "Santana",
    "Molina", "Alvarado", "Salas", "Guzman", "Duran", "Padilla", "Jimenez",
    "Vasquez", "Monroy", "Cortez", "Soto", "Moya", "Ochoa", "Rangel",
    "Alvarado", "Solis", "Gallegos", "Trevino", "Garcia", "Alvarez", "Valdez",
    "Serrano", "Gonzalez", "Zepeda", "Salas", "Murillo", "Bautista",
    "Cervantes", "Hernandez", "Bello", "Rosales", "Meza", "Valenzuela",
    "Salas", "Rojas", "Pineda", "Hernandez", "Delgado", "Sanchez", "Rosario",
    "Hernandez", "Moreno", "Castillo", "Vasquez", "Lara", "Lopez", "Ramirez",
    "Ponce", "Hernandez", "Salas", "Ruiz", "Esparza", "Rivas", "Reyes",
    "Pacheco", "Maldonado", "Morales", "Lara", "Hernandez", "Palacios",
    "Serrano", "Zamora", "Jasso", "Zambrano", "Hernandez", "Mora", "Sosa",
    "Morales", "Torres", "Gonzalez", "Cantu", "Flores", "Rodriguez",
    "Martinez", "Salazar", "Gonzalez", "Acosta", "Trevino", "Saldana",
    "Guzman", "Garcia", "Cordero", "Palacios", "Vasquez", "Moreno",
    "Hernandez", "Cruz", "DeLaCruz", "Fernandez", "Martinez", "Reyes",
    "Martinez", "Bautista", "Ceballos", "Gonzalez", "Zambrano", "Cruz",
    "Hernandez", "Gonzalez", "Nunez", "Castillo", "Santos", "Moreno",
    "Rodriguez", "Salas", "Carrillo", "Duran", "Lara", "Santos", "Martinez",
    "Reyes", "Nunez", "Gonzalez", "Hernandez", "Cano", "Hernandez", "Mora",
    "Zuniga", "Rodriguez", "Ramirez", "Valdez", "Hernandez", "Maldonado",
    "Torres", "Rosales", "Acosta", "Bermudez", "Medina", "Zavala", "Cruz",
    "Moreno", "Hernandez", "Lara", "Torres", "Serrano", "Cantu", "Gonzalez",
    "Salas", "Torres", "Hernandez", "Montoya", "Cabrera", "Ponce", "Hernandez",
    "Rodriguez", "Aguirre", "Gonzalez", "Marroquin", "Espinoza", "Salinas",
    "Ochoa", "Zamora", "Luna", "Rosario", "Hernandez", "Salas", "Martinez",
    "Solis", "Hernandez", "Reyes", "Serrano", "Solis", "DeLaCruz", "Cano",
    "Vega", "Rodriguez", "Rangel", "Torres", "Cantu", "Martinez", "Gonzalez",
    "Gonzalez", "Duarte", "Quintana", "Palacios"
]


def generate_random_person():
    """
    Generates a dictionary with random person data.
    Fields include a random firstname, lastname, and age.

    Returns:
    - Dictionary representing a person with keys 'firstname',
        'lastname', and 'age'
    """
    firstname = random.choice(firstnames)
    lastname = random.choice(lastnames)
    age = random.randint(20, 45)
    return {'firstname': firstname, 'lastname': lastname, 'age': age}


def populate_person_table(session, num_records=1000000):
    """
    Populates the person table with a specified number of dummy records.

    Parameters:
    - session: SQLAlchemy session used for database transactions
    - num_records: Integer representing the number of records to
        insert into the table
    """
    # Generate data in bulk to reduce the number of database transactions
    bulk_data = [generate_random_person() for _ in range(num_records)]
    session.bulk_insert_mappings(Person, bulk_data)
    session.commit()


# Main execution
if __name__ == '__main__':
    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Open a session
    session = Session()
    try:
        # Populate the table with 1,000,000 dummy records
        populate_person_table(session)
        print("Successfully added 1,000,000 dummy records to the person table")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()
