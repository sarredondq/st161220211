## Profesor: Edwin Montoya, Universidad EAFIT, Medellín-Colombia
## emontoya@eafit.edu.co

# instalar:

    AWS EC2: t2.medium / 20 GB DD

Filebeat: https://www.elastic.co/es/downloads/beats/filebeat (envio de logs de una máquina Linux a ElasticSearch)

    wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.12.0-linux-x86_64.tar.gz

    tar -xzf filebeat-7.12.0-linux-x86_64.tar.gz
    cd filebeat-7.12.0

Edit the filebeat.yml configuration file
Start the daemon by running sudo ./filebeat -e -c filebeat.yml

Metricbeat: https://www.elastic.co/es/downloads/beats/metricbeat (envio de info del sistema - cpu, mem, disco, etc a ElasticSearch)

    wget https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-7.12.0-linux-x86_64.tar.gz
    tar -xvf metricbeat-7.12.0-linux-x86_64.tar.gz
    cd metricbeat-7.12.0

Edit the metricbeat.yml configuration file
sudo ./metricbeat -e -c metricbeat.yml