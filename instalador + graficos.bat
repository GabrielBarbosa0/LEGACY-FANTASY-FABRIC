::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
title Instalador do Modpack - LEGACY FANTASY FABRIC
setlocal enabledelayedexpansion

:: Definir caminho padrão do Minecraft
set "MINECRAFT_PATH=%APPDATA%\.minecraft"
set "MODPACK_SOURCE=%~dp0(abra essa pasta e copie tudo para .minecraft)"
set "BACKUP_PATH=%MINECRAFT_PATH%\BACKUP-MODPACK"

:: Criar pasta de backup se não existir
if not exist "%BACKUP_PATH%" mkdir "%BACKUP_PATH%"

:: Função para criar um nome único para backups
set "COUNTER=1"
set "NEW_BACKUP_NAME=%BACKUP_PATH%\options.txt_OLD"
:CHECK_BACKUP
if exist "%NEW_BACKUP_NAME%" (
    set /a COUNTER+=1
    set "NEW_BACKUP_NAME=%BACKUP_PATH%\options.txt_OLD_%COUNTER%"
    goto CHECK_BACKUP
)

:: Mover arquivos para backup
for %%I in (mods config resourcepacks shaderpacks options.txt) do (
    if exist "%MINECRAFT_PATH%\%%I" (
        if exist "%BACKUP_PATH%\%%I" (
            ren "%BACKUP_PATH%\%%I" "%%I_OLD"
        )
        move "%MINECRAFT_PATH%\%%I" "%BACKUP_PATH%"
    )
)

:: Copiar novos arquivos do modpack
for %%I in (mods config resourcepacks shaderpacks) do (
    if exist "%MODPACK_SOURCE%\%%I" (
        xcopy /E /I /Y "%MODPACK_SOURCE%\%%I" "%MINECRAFT_PATH%\%%I"
    )
)

:: Perguntar ao usuário sobre a qualidade gráfica
:ASK_GRAPHICS
set /p GRAPHICS="Escolha a qualidade gráfica (Alto ou Baixo): "
set GRAPHICS=%GRAPHICS:~0,5%
set GRAPHICS=%GRAPHICS:~0,1%%GRAPHICS:~1,4%

:: Normalizar entrada para evitar erros
if /I "%GRAPHICS%"=="Alto" (
    set "OPTIONS_FILE=options_alto.txt"
) else if /I "%GRAPHICS%"=="Baixo" (
    set "OPTIONS_FILE=options_baixo.txt"
) else (
    echo Opção inválida! Digite "Alto" ou "Baixo".
    goto ASK_GRAPHICS
)

:: Copiar o arquivo correto para "options.txt"
if exist "%MODPACK_SOURCE%\%OPTIONS_FILE%" (
    copy /Y "%MODPACK_SOURCE%\%OPTIONS_FILE%" "%MINECRAFT_PATH%\options.txt"
    echo Gráficos %GRAPHICS% aplicados com sucesso!
) else (
    echo ERRO: Arquivo "%OPTIONS_FILE%" não encontrado! Verifique se está na pasta do modpack.
    pause
    exit /b
)

echo Modpack instalado com sucesso!
pause
