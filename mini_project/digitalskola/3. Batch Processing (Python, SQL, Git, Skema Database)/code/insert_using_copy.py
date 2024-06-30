import psycopg2

# Connection String
conn_string = "host=localhost port=5432 dbname=postgres user=postgres password=welcome123 sslmode=prefer connect_timeout=10"

# Membuat koneksi
conn = psycopg2.connect(conn_string)

# Membuat cursor
cur = conn.cursor()

# Create Table
cur.execute("""
            CREATE TABLE IF NOT EXISTS users_using_copy(
                id serial primary key,
                email text,
                name text,
                phone text,
                postal_code text
            )
            """)

with open ("/002_Documents/001_Private/LEARNING/DATA ENGINEER/Digital Skola/Sesi 17/Project 3/source/users_w_postal_code.csv","r") as f :
    next(f)
    cur.copy_from(f, "users_using_copy", sep=",", columns=("email","name","phone","postal_code"))

# Commit perubahan ke database
conn.commit()

# Menutup cursor dan koneksi
cur.close()
conn.close()    