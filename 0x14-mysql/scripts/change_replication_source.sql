-- starting mysql replication
CHANGE MASTER TO
    MASTER_HOST = '54.237.77.75',
    MASTER_USER = 'replica_user',
    MASTER_PASSWORD = 'projectcorrection280hbtn',
    MASTER_LOG_FILE = 'mysql-bin.000001',
    MASTER_LOG_POS = 154;

START SLAVE;
SHOW SLAVE STATUS\G
