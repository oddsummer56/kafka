from kafka import KafkaConsumer
from json import loads
import time
from datetime import datetime

consumer = KafkaConsumer(
        'chat',
        #bootstrap_servers=['localhost:9092'],
        bootstrap_servers=['ec2-43-203-238-182.ap-northeast-2.compute.amazonaws.com:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='chat-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("채팅 프로그램 - 메세지 수신")
print("메세지 대기 중...")

try:
    for m in consumer:
        data = m.value
        print(f"[FRIEND]:[{datetime.fromtimestamp(data['time'])}] {data['message']}")

except KeyboardInterrupt:
    print("채팅종료")

finally:
    consumer.close()
