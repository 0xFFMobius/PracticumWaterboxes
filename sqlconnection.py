def connection_tensile():
    conn_str_parameters={
        'user': 'blakamp',
        'pass': 'Changeme1',
        'host': 'sqisproddb.evrazna.com',
        'port': '1521',
        'service': 'sqis_app.eina.evrazinc.ad'
    }
    return "oracle+oracledb://{user}:{pass}@{host}:{port}?service_name={service}".format(**conn_str_parameters)

def connection_waterbox():
    return connection_str('ibaCoil')

def connection_process():
    return connection_str('RodAndBar_L2_Mirror')

def connection_str(database):
    conn_str_parameters={
        'driver': 'SQL Server'.replace(' ', '+'),
        'user': 'RB_SPC',
        'pass': 'spc1!',
        'host': '10.101.67.12',
        'db_name': database
    }
    #connection_string = r"DRIVER={SQL Server Native Client 11.0};SERVER={host}\{db_name};UID=Proc_ctl;PWD=pass"
    #connection_string = quote(connection_string)
    return "mssql+pyodbc://{user}:{pass}@{host}/{db_name}?driver={driver}".format(**conn_str_parameters)