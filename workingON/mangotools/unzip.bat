@@:: Script Credit - https://stackoverflow.com/questions/2609985/how-to-run-a-powershell-script-within-a-windows-batch-file
@@setlocal
@@set POWERSHELL_BAT_ARGS=%*
@@if defined POWERSHELL_BAT_ARGS set POWERSHELL_BAT_ARGS=%POWERSHELL_BAT_ARGS:"="%
@@PowerShell -Command Invoke-Expression $('$args=@(^&{$args} %POWERSHELL_BAT_ARGS%);'+[String]::Join([char]10,$((Get-Content '%~f0') -notmatch '^^@@'))) & goto :EOF
$whl = Read-Host -Prompt 'Enter absolute path for .whl file'
Set-Variable -Name "whlzip" -Value ($whl + ".zip")
Rename-Item -path $whl -NewName $whlzip
Expand-Archive -Force $whlzip -DestinationPath "output_temp"
Rename-Item -path $whlzip -NewName $whl
