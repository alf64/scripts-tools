@echo off

# REM This script sends given file to remote PC.
# REM OpenSSH server shall be installed and enabled (under Windows OS Services) on remote machine.
# REM OpenSSH client and Putty shall be installed on PC that calls this script.

echo # A script to send files to remote PC.    #
echo.

SET DESTINATION=Administrator@22.167.77.47:C:\resources\

IF [%1] == [/?] (
    echo The usage is as follows:
    echo %0 ^<files-to-be-send^>
    EXIT /b
)

REM Check if 1st argument has been given
IF [%1] == [] (
    echo Error! file not passed as 1st argument.
    EXIT /b
) ELSE (
    SET SOME_FILE="%1"
)

IF NOT EXIST %SOME_FILE% (
    echo Error! %SOME_FILE% not found.
    EXIT /b
)

REM Optional 2nd argument to send.
IF [%2] == [] (
    echo Optional file not passed as 2nd argument, it won't be send.
    set OPTIONAL_FILE=0
) ELSE (
    SET OPTIONAL_FILE="%2"
)

IF %OPTIONAL_FILE% NEQ 0 (
    IF NOT EXIST %OPTIONAL_FILE% (
        echo Error! %OPTIONAL_FILE% not found.
        EXIT /b
)
)

echo %SOME_FILE% will be send to %DESTINATION%

IF %OPTIONAL_FILE% NEQ 0 ( 
    echo %FW_ELF_FILE% will be send to %DESTINATION%
)

REM The server needs a file "authorized_keys" present in .ssh directory (it contains public keys).
REM Simply take your id_rsa.pub, copy its content and put into authorized_keys (create if does not exist).
"C:\Program Files (x86)\PuTTY\pscp.exe" -i "C:\Users\alf\.ssh\alf.ppk" %SOME_FILE% %DESTINATION%
IF %OPTIONAL_FILE% NEQ 0 (
    "C:\Program Files (x86)\PuTTY\pscp.exe" -i "C:\Users\alf\.ssh\alf.ppk" %OPTIONAL_FILE% %DESTINATION%
)

REM Theory about keys - especially on Windows OS.
REM Public key is a key to encode. Private key is a key to decode.
REM Always share public key, never private.
REM You are sharing yours public key to server, because server needs to encode data for you. You will then decode it via your private key.
REM You are receinvg server's public key to encode data for server. Server will then decode it via its private key.

REM Typical problems with openSSH Server - Windows.
REM When server refuses your key and still asks for password during connection.
REM - You must add your authorized_keys to %PROGRAMDATA%\ssh directory, because Windows looks at this file (instead %HOME%\.ssh\authorized_keys) when your account is with administrator privileges.
REM - Also, you must rename this file to administrators_authorized_keys when in %PROGRAMDATA%\ssh directory
REM - You must reduce privileges of administrators_authorized_keys to Administrators only. Right click -> Properties -> Security -> Advanced -> Remove inheritance (convert to explicit) and then remove any other users, leave only Administrators group.
REM - It may be important for encoding of the authorized_keys file to be ANSI, not UTF-8, since for some people it's the issue. However it seems like UTF-8 is working for me.
REM 

echo.
echo Job done.
