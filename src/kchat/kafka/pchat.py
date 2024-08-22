from kafka import KafkaProducer
from json import dumps
import time

p = KafkaProducer(
        #
        )

print("채팅 프로그램 - 메세지 발신자")
print("메세지를 입력하세요. (종료시 'exit' 입력)")

while True:
    msg = input("YOU: ")
    if msg.lower == 'exit':
        break

    data = {'message':msg, 'time': time.time()}
    #보내기
