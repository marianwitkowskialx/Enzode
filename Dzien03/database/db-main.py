from datetime import datetime

# Przykład korzystania z bazy danych z wykorzystaniem natywnego sterownika
from dbutils import connect_db

conn, cursor = connect_db()

# SELECT
sql = "SELECT film_id, title, description FROM public.film WHERE film_id<=10"
cursor.execute(sql)
rows = cursor.fetchall()
#print(rows)

sql = "SELECT film_id, title, description FROM public.film WHERE film_id=1"
cursor.execute(sql)
row = cursor.fetchone()
print(row)

# INSERT
sql = "INSERT INTO public.city " \
      "(city, last_update, country_id ) values (%s, %s, %s)"
data = ("Baku2A", datetime.today(), 10)
cursor.execute(sql, data)
conn.commit()

# UPDATE
sql = "UPDATE public.city SET city=%s WHERE city=%s "
data = ("Baku2AA", "Baku2A" )
cursor.execute(sql, data)
conn.commit()

# DELETE
sql = "DELETE FROM public.city WHERE city LIKE %s "
data = ("Baku2A",)
cursor.execute(sql, data)
conn.commit()

cursor.close()
conn.close()
