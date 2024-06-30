import psycopg2

# Connection String
conn_string = "host=localhost port=5432 dbname=postgres user=postgres password=welcome123 sslmode=prefer connect_timeout=10"

# Membuat koneksi
conn = psycopg2.connect(conn_string)

# Membuat cursor
cur = conn.cursor()

# Create Table
cur.execute("""
            CREATE TABLE IF NOT EXISTS latihan_users(
                id serial primary key,
                email text,
                name text,
                phone text,
                postal_code text
            )
            """)

# Commit perubahan ke database
conn.commit()

# Menutup cursor dan koneksi
cur.close()
conn.close()    