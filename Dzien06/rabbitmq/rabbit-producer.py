
import pika

AMQP_URL = "amqps://rmtaquzr:JaMnEn-ivVKQTrcAZCi2YycWOiMejIdj@cow.rmq2.cloudamqp.com/rmtaquzr"
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params) # utworzenie polaczenia
channel = connection.channel() # utworzenie kanału
channel.queue_declare(queue="enzode", durable=True) # deklaracja kolejki

for nr in range(1,6):
    channel.basic_publish(exchange="",
                          routing_key="enzode",
                          body=f"Komunikat nr {nr}")

connection.close()