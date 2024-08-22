# kchat
## Start Server
```bash
$ cd $KAFKA_HOME
$ bin/zookeeper-server-start.sh config/zookeeper.properties

# 새창
$ bin/kafka-server-start.sh config/server.properties
```

## Test
#### KAFKA Producer
```bash
$ python src/kchat/kafka/pro.py
[DONE]: 0.04007911682128906
```

```bash
$ $KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092

{"str": "value0"}
{"str": "value1"}
{"str": "value2"}
{"str": "value3"}
{"str": "value4"}
{"str": "value5"}
{"str": "value6"}
{"str": "value7"}
{"str": "value8"}
{"str": "value9"}
```

## Test2
#### Producer
```python
$ python src/kchat/kafka/pro.py
```
#### Consumer
```python
$ python src/kchat/kafka/con.py
```
![image](https://github.com/user-attachments/assets/0461cfa7-8ef7-490d-9532-78c41b2b0b39)


