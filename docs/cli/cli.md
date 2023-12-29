# CLI

## Entering

Postgres try to get user **role** from command line user and try to get a **role database**

### How to manage users?

```
adduser --disabled-password <username>
```

```
su - <username>
```

```
exit
```

```
cat /etc/passwd | cut -d: -f1
```

```
userdel -f <username>
```

### psql

```
psql -U <auth_username> <database>


psql <database>  # if authorized user 


psql  # if authorized user and db_name as authorized username    
```

### createdb / dropdb

```
createdb -U <auth_username> <database>
```

```
dropdb -U <auth_username> <database>
```

### createuser / dropuser

```
createuser -U <auth_username> <username>
```

```
dropuser -U <auth_username> <username>
```

## Working in database

```
\h, \? - help

         
\q, \c - connect, quit


\l, \l <db_name> - List of db


\d - Lit of tables, viewsm sequences


\dn - List of schemas


\dt, \d <tb_name> - List of tables


\dv - List of views


\df - List of fuctions


\du - List of roles


\i <sql_file> - Execute sql script
```