Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\pipeline\Start_BigMenu.bat" & Chr(34), 0
Set WshShell = Nothing