Set oShell = WScript.CreateObject ("WScript.Shell")
oShell.run "cmd.exe /C sqlite3 -header -csv log.db ""select * from my_table_name;"" > report.csv"
Set oShell = Nothing'