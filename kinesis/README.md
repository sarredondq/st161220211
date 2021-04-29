# Universidad EAFIT
# Curso St1612 Sistemas Intensivos en Datos, 2021 - 1
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co

# Amazon Kinesis lab 6

1. crear un servicio kinesis firehose por la consola web:

        Create: Delivery streaming data with Kinesis Firehose
        Name: purchaseLogs
        Source: Direct PUT or other sources
        Use: Kinesis Agent
        Destination:
        Amazon S3 – select or create a bucket (st1612orderlogs)
        S3 buffer conditions: 
        Buffer interval: 60 segs
        IAM role:
        Create new: ‘firehose_delivery_role’ with defaults

2. crear una instancia EC2 AMI2 linux

Adicionar a esta instancia el permiso IAM: AmazonKinesisFullAccess y AmazonKinesisFirehoseFullAccess

3. instalar el agente kinesis

        $ sudo yum install –y https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-agent-latest.amzn1.noarch.rpm

4. descargar los logs (OnlineRetail.csv) ejemplo y LogsGenerator.py (ya estan en el github)

5. cambiar permisos, crear directorios, etc:

        $ chmod a+x LogGenerator.py
        $ sudo mkdir /var/log/acmeco
        $ sudo nano /etc/aws-kinesis/agent.json

6. iniciar el agente:

        $ sudo systemctl start aws-kinesis-agent

7. ejecutar un envio de logs:

Nota: antes de Generar Logs, descomprima el archivo: OnlineRetail.csv.gz
Nota: $ gunzip OnlineRetail.csv.gz

        $ sudo ./LogGenerator.py 1000

8. chequee en unos minutos el 'bucket' st1612orderlogs

# LAB 6 - Kinesis Data Streams + DynamoDB:

1. Crear un Kinesis Data Stream en AWS:

        Create Kinesis Stream:
        name: acmecoOrders
        Nro shards: 1
        Boton: Create Kinesis Stream

2. Configurar el kinesis-agent para enviar los logs al Kinesis Data Stream

        $ sudo nano /etc/aws-kinesis/agent.json

        adicionar:

           "flows": [
                {
                "filePattern": "/var/log/acmeco/*.log",
                "kinesisStream": "acmecoOrders",
                "partitionKeyOption": "RANDOM",
                "dataProcessingOptions": [
                        {
                        "optionName": "CSVTOJSON",
                        "customFieldNames": ["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "Customer", "Country"]
                        }
                ]
                },

3. reiniciar el servicio:

        $ sudo systemctl restart aws-kinesis-agent

4. generar logs de prueba:

        $ sudo ./LogGenerator.py 1000

5. crear la tabla DynamoDB

        Table Name: acmecoOrders
        Primary Key: CustomerID / Number
        Add sort key: OrderID / String
        Use defaults setting
        boton: create

6. ir a la instancia EC2 donde tenemos en kinesis-agent

        $ sudo yum install -y python3-pip
        $ sudo pip3 install boto3

        actualizar las credenciales AWS en el linux

        $ mkdir .aws
        $ aws configure

Nota: Copy las credenciales AWS EDUCATE en el archivo generado.

7. Configurar un Consumer del kinesis data stream, mediente un cliente standalone (Consumer.py)

Nota: tenga en cuenta que esta versión es python2, hay que adaptaro a versión python3

        configurar 'Consumer.py'
        $ chmod a+x Consumer.py
        $ python3 Consumer.py

        en otra terminal, generar nuevos registros para que el consumer los adquiera de kinesis y los inserte en DynamoDB

8. Crear una funcion aws lambda para consumir de kinesis data streams e insertar en una table DynamoDB:

        Crear un IAM Role Lambda llamado 'acmecoOrders' con los permisos: 'AmazonKinesisReadOnlyAccess' y 'AmazonDynamoDBFullAccess'

        Crear la function lambda 'Author from scratch':
        Function name: ProcessOrders
        Runtime: python 2.7
        Use an existing role: acmecoOrders
        crearla.

        +Add Trigger: Kinesis Data Stream