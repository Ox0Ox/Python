#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

<^Tab::
KeyWait Tab
KeyWait Shift
KeyWait Ctrl
Send {Space Down}
Send {Space Up}
Send {Ctrl Down}
Send {LWin Down}
Send {Left Down}
Send {Ctrl Up}
Send {LWin Up}
Send {Left Up}
Send {LButton}
Send {LButton}
Send {LButton}
Send {LButton}
Send {LButton}
Send {LButton}
Send {LButton}
Send, ^m

return