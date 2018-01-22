import sqlite3

checkpoints_file = '/var/log/trklogs/checkpoints/adserver-dev-clickmanager/checkpoints'
create_table_statement = "create table if not exists FILE_CHECKPOINTS(flow text,path text,fileId text,lastModifiedTime bigint,size bigint,offset bigint,lastUpdated datetime,primary key (flow, path))"

try:
    connection = sqlite3.connect(checkpoints_file)
    c = connection.cursor()
    
    # Create table
    c.execute(create_table_statement)

    # Save (commit) the changes
    connection.commit()

    # Close the connection if we are done with it.
    connection.close()
except sqlite3.Error as e:
    print "An error occurred creating the database: ", e.args[0]