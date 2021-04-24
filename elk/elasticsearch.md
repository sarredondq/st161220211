## Profesor: Edwin Montoya, Universidad EAFIT, Medellín-Colombia
## emontoya@eafit.edu.co

# primeros pasos con ElasticSearch - webinar:

https://www.elastic.co/es/webinars/getting-started-elasticsearch

# instalar:

    AWS EC2: t2.medium / 20 GB DD

    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.12.0-linux-x86_64.tar.gz
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.12.0-linux-x86_64.tar.gz.sha512
    shasum -a 512 -c elasticsearch-7.12.0-linux-x86_64.tar.gz.sha512 
    tar -xzf elasticsearch-7.12.0-linux-x86_64.tar.gz
    cd elasticsearch-7.12.0/

# config:

    set memory:

    https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html

    $ sudo sysctl -w vm.max_map_count=262144

    $ sudo sysctl -w fs.file-max=65536

# iniciar servidor:

    bin/elasticsearch -d -p pid

# terminar:

    pkill -F pid