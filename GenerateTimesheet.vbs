Set oShell = WScript.CreateObject ("WScript.Shell")
oShell.run "cmd.exe /C sqlite3 -header -csv log.db ""select * log;"" > report.csv"
Set oShell = Nothing'