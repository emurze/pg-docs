# CLI

## Entering

Postgres try to get user **role** from command line user and try to get a **role database**

### How to manage users

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
psql -U <username> <database>
```
or logged in
```
psql <database>
```
or logged in and db_name ad role_name
```
psql
```

### createdb

```
createdb -U <username> <database>
```

### dropdb

```
dropdb -U <username> <database>
```

## Working in database

Quit
```
\q
```

Display all commands or info about single command
```
\h
```
```
\h ABORT
```

List dbs or info about single db
```
\l
```
```
\l+
```
```
\l <database>
```
On/Off expanded info mode
```
\x
```