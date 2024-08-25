from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import time
import threading
import uuid

# 프로듀서 함수
def producer():
    p = KafkaProducer(
        bootstrap_servers=['ec2-43-203-238-182.ap-northeast-2.compute.amazonaws.com:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

    print("채팅 프로그램 - 메시지 발신자")
    print("메시지를 입력하세요. (종료 시 'exit' 입력)")

    while True:
        msg = input("YOU : ")
        if msg == 'exit':
            break

        data = {'message': msg, 'time': time.time()}
        p.send('chat', value=data)
        p.flush()

    print("채팅 종료")
    p.close()

# 컨슈머 함수
def consumer():
    unique_group_id = f'chat_group_{uuid.uuid4()}'
    c = KafkaConsumer(
        'chat',
        bootstrap_servers=['ec2-43-203-238-182.ap-northeast-2.compute.amazonaws.com:9092'],
        auto_offset_reset='latest',
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        group_id=unique_group_id,  # 고유한 group_id 사용
        enable_auto_commit=False
    )

    print("채팅 프로그램 - 메시지 수신")
    print("메시지 대기 중")

    try:
        for m in c:
            data = m.value
            print(f"[FRIEND] {data['message']}")
    except KeyboardInterrupt:
        print("채팅 종료")
    finally:
        c.close()

# 스레드 생성 및 시작
if __name__ == "__main__":
    # 먼저 Consumer를 시작
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()
    
    # Consumer가 실행된 후 Producer 시작
    time.sleep(1)  # 잠깐 대기하여 Consumer가 시작될 시간을 확보
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    producer_thread.join()
    consumer_thread.join()

