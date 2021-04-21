# Universidad EAFIT
# Curso ST1612 Sistemas Intensivos en Datos, 2021 - 1
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co

# HIVE

### TABLAS SENCILLAS EN HIVE

### 1 Conexión al cluster Hadoop via HUE en Amazon EMR

Hue Web (cada uno tiene su propio cluster EMR)

    http://ec2.compute-1.amazonaws.com:8888
    

Usuarios: (entrar como hadoop/********* y crear cada uno su usuario)

    username: hadoop
    password: ********

### 2 Los archivos de trabajo hdi-data.csv y export-data.csv

    /user/username/datasets/onu

### 3 Gestión (DDL) y Consultas (DQL)

### cada uno deberá crear su propia BD:

Hue-Hive:

    CREATE DATABASE usernamedb

### Crear la tabla HDI en Hive:

### NOTA: algunos de estos comandos son ejecutados desde Hue-Hive, para archivos desde Hue-Files o Conexión SSH al servidor Master del Cluster EMR (identificará los comandos desde SSH porque comienzan por $ )

### tabla manejada por hive: /user/hive/warehouse

Hue-Hive:

    use usernamedb;
    CREATE TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
    STORED AS TEXTFILE

### se requiere cargar datos a la tabla asi:
### 
### copiando datos directamente hacia hdfs:///warehouse/tablespace/managed/hive/mydb.db/hdi

ssh-hacia-master:

    $ hdfs dfs -cp hdfs:///user/username/datasets/onu/hdi-data.csv hdfs:///warehouse/tablespace/managed/hive/usernamedb.db/hdi

### cargardo datos desde hive:

### darle primero permisos completos al directorio:

ssh-hacia-master:

    $ hdfs dfs -chmod -R 777 /user/username/datasets/onu/

Hue-Hive:

    load data inpath '/user/username/datasets/onu/hdi-data.csv' into table HDI

    # tabla externa en hdfs: 
    use usernamedb;
    CREATE EXTERNAL TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE 
    LOCATION '/user/username/datasets/onu/hdi/'

    # tabla externa en S3: 
    use usernamedb;
    CREATE EXTERNAL TABLE HDI (id INT, country STRING, hdi FLOAT, lifeex INT, mysch INT, eysch INT, gni INT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE 
    LOCATION 's3://<bucketname>/datasets/onu/hdi/'

Nota: Esta tabla la crea en una BASE DE DATOS 'mydb'

    use usernamedb;
    show tables;
    describe hdi;

### hacer consultas y cálculos sobre la tabla HDI:

    select * from hdi;

    select country, gni from hdi where gni > 2000;    

### EJECUTAR UN JOIN CON HIVE:

### Obtener los datos base: export-data.csv

usar los datos en 'datasets' de este repositorio.

### Iniciar hive y crear la tabla EXPO:

    use usernamedb;
    CREATE EXTERNAL TABLE EXPO (country STRING, expct FLOAT) 
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE 
    LOCATION 's3://<bucketname>/datasets/onu/export/'

### EJECUTAR EL JOIN DE 2 TABLAS:

    SELECT h.country, gni, expct FROM HDI h JOIN EXPO e ON (h.country = e.country) WHERE gni > 2000;

### 4. WORDCOUNT EN HIVE:

    use usernamedb;
    CREATE EXTERNAL TABLE docs (line STRING) 
    STORED AS TEXTFILE 
    LOCATION 'hdfs://localhost/user/username/datasets/gutenberg-small/';

--- alternativa2:

    CREATE EXTERNAL TABLE docs (line STRING) 
    STORED AS TEXTFILE 
    LOCATION 's3://<<bucketname>>/datasets/gutenberg-small/';

--- ordenado por palabra

    SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
    GROUP BY word 
    ORDER BY word DESC LIMIT 10;

--- ordenado por frecuencia de menor a mayor

    SELECT word, count(1) AS count FROM (SELECT explode(split(line,' ')) AS word FROM docs) w 
    GROUP BY word 
    ORDER BY count DESC LIMIT 10;