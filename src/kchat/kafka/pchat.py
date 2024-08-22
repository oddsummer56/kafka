from kafka import KafkaProducer
import json
import time

p = KafkaProducer(
    
    #bootstrap_servers=['localhost:9092'],
    bootstrap_servers=['ec2-43-203-238-182.ap-northeast-2.compute.amazonaws.com:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

print("채팅 프로그램 - 메시지 발신자")
print("메시지를 입력하세여.(종료시 'exit' 입력") 

while True:
    msg = input("YOU: ")
    if msg.lower() == 'exit':
        break

    data = {'message' : msg, 'time':time.time()}
    # 보내기  
    p.send('chat',value=data)
    p.flush()











 
