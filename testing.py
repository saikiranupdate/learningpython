from tableauhyperapi import HyperProcess, Connection, TableDefinition, SqlType, Telemetry, Inserter, CreateMode, \
    TableName

PATH_TO_HYPER = 'testing.hyper'
with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU,'Sai') as hyper:
    with Connection(endpoint=hyper.endpoint,
                    create_mode=CreateMode.CREATE_AND_REPLACE,
                    database=PATH_TO_HYPER) as connection:
        connection.catalog.create_schema('Saikiran')

        cmd = TableDefinition(table_name=TableName('Saikiran','pabbu'),
                          columns=[
                              TableDefinition.Column('date', SqlType.date()),
                              TableDefinition.Column('country', SqlType.text()),
                              TableDefinition.Column('sales', SqlType.double()),
                              TableDefinition.Column('profit', SqlType.double()),
                              TableDefinition.Column('profit_ratio', SqlType.double()),
                          ])

        connection.catalog.create_table(cmd)

    print("The Hyper created.")
    print("The connection to the Hyper file is closed.")
