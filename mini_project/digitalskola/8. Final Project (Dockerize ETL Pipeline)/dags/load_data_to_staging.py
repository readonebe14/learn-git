from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import mysql.connector
import requests

# Load environment variables from .env file
load_dotenv()

# Fungsi untuk mengambil data dari API
def get_data_from_api():
    url = "http://103.150.197.96:5005/api/v1/rekapitulasi_v2/jabar/harian?level=kab"
    response = requests.get(url)
    data = response.json()
    return data["data"]["content"]

# Fungsi untuk menyimpan data ke database MySQL
def save_data_to_mysql(data):
    # Mengambil nilai dari environment variables
    host = os.getenv("MYSQL_HOST")
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    database = os.getenv("MYSQL_DATABASE")
    tls_client_auth = os.getenv("MYSQL_TLS_CLIENT_AUTH")
    tls_version = os.getenv("MYSQL_TLS_VERSION")

    # Menghubungkan ke database MySQL
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        auth_plugin='mysql_native_password' if tls_client_auth == '0' else 'caching_sha2_password',
        ssl_disabled=(tls_client_auth == '0'),
        ssl_version=tls_version
    )

    cursor = connection.cursor()

    # Query SQL untuk menyimpan data
    sql = """
    INSERT INTO data_covid (
        CLOSECONTACT, CONFIRMATION, PROBABLE, SUSPECT,
        closecontact_dikarantina, closecontact_discarded, closecontact_meninggal,
        confirmation_meninggal, confirmation_sembuh,
        kode_kab, kode_prov, nama_kab, nama_prov,
        probable_diisolasi, probable_discarded, probable_meninggal,
        suspect_diisolasi, suspect_discarded, suspect_meninggal,
        tanggal
    ) VALUES (
        %s, %s, %s, %s,
        %s, %s, %s,
        %s, %s,
        %s, %s, %s, %s,
        %s, %s, %s,
        %s, %s, %s,
        %s
    )
    """

    # Menyimpan data ke database
    for row in data:
        values = (
            row["CLOSECONTACT"], row["CONFIRMATION"], row["PROBABLE"], row["SUSPECT"],
            row["closecontact_dikarantina"], row["closecontact_discarded"], row["closecontact_meninggal"],
            row["confirmation_meninggal"], row["confirmation_sembuh"],
            row["kode_kab"], row["kode_prov"], row["nama_kab"], row["nama_prov"],
            row["probable_diisolasi"], row["probable_discarded"], row["probable_meninggal"],
            row["suspect_diisolasi"], row["suspect_discarded"], row["suspect_meninggal"],
            row["tanggal"]
        )
        cursor.execute(sql, values)

    # Commit perubahan
    connection.commit()

    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()

# Fungsi untuk menjalankan skrip
def run_script():
    data = get_data_from_api()
    save_data_to_mysql(data)
    print("Data telah disimpan ke database MySQL.")

# Definisikan argumen default untuk DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Buat objek DAG
dag = DAG(
    dag_id='load_data_to_staging',
    default_args=default_args,
    description='Pipeline untuk menarik data COVID dan menyimpannya ke MySQL',
    schedule_interval='0 20 * * *',  # Menjalankan DAG setiap jam 9 malam
)

# Definisikan tugas-tugas dalam DAG
start_task = EmptyOperator(
        task_id='start'
)

fetch_data_task = PythonOperator(
    task_id='fetch_data_from_api',
    python_callable=run_script,
    dag=dag,
)

end_task = EmptyOperator(
        task_id='end'
    )
# Atur dependensi antar tugas
start_task >> fetch_data_task >> end_task

