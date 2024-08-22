from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
        'chat',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='chat-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("채팅 프로그램 - 메세지 수신")
print("메세지 대기 중...")

try:
    for m in consumer:
        print(f"xxxxxxxxxxxxxxxx")

except KeyboardInterrupt:
    print("채팅종료")

finally:
    consumer.close()
