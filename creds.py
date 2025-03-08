def create_db_connection():
    return mysql.connector.connect(DB_CONFIG)

def setup_museum_table():
    conn = create_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS museum (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            artist VARCHAR(255) NOT NULL,
            year INT NOT NULL,
            description VARCHAR(255),
            owner VARCHAR(255),
            value DECIMAL(10,2)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_test_data():
    conn = create_db_connection()
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO museum (name, artist, year, description) VALUES (%s, %s, %s, %s)
    """, [
        ("Starry Night", "Vincent van Gogh", 1889, "A masterpiece of post-impressionism."),
        ("The Persistence of Memory", "Salvador Dalí", 1931, "Surrealist painting with melting clocks."),
        ("Mona Lisa", "Leonardo da Vinci", 1503, "The world-famous portrait."),
        ("The Scream", "Edvard Munch", 1893, "Expressionist depiction of anxiety."),
        ("Girl with a Pearl Earring", "Johannes Vermeer", 1665, "Also known as the Dutch Mona Lisa.")
    ])
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    setup_museum_table()
    insert_test_data()
    print("Museum table setup complete with test data.")