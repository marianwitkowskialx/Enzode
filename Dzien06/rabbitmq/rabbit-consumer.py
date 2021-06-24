
import pika

def callback(ch, method, proprties, body):
    print(f"odebrano: {str(body)}, props={str(proprties)}")

AMQP_URL = "amqps://rmtaquzr:JaMnEn-ivVKQTrcAZCi2YycWOiMejIdj@cow.rmq2.cloudamqp.com/rmtaquzr"
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params) # utworzenie polaczenia
channel = connection.channel() # utworzenie kanału
channel.queue_declare(queue="enzode", durable=True) # deklaracja kolejki
channel.basic_consume("enzode", callback, auto_ack=True)

print("Czekam na komunikaty....")
channel.start_consuming()

connection.close()