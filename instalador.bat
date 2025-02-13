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
chcp 65001 >nul
setlocal EnableDelayedExpansion

:: Caminho padrão do Minecraft no Windows
set "DEFAULT_MC_PATH=%APPDATA%\.minecraft"

:: Permitir que o usuário escolha a pasta de instalação
set /p MC_PATH=Digite o caminho da pasta .minecraft (ou pressione Enter para usar o padrão: %DEFAULT_MC_PATH%): 
if "%MC_PATH%"=="" set "MC_PATH=%DEFAULT_MC_PATH%"

:: Definir caminhos do modpack
set "MODPACK_PATH=%~dp0(abra essa pasta e copie tudo para .minecraft)"
set "BACKUP_PATH=%MC_PATH%\BACKUP-MODPACK"

:: Criar pasta de backup se não existir
if not exist "%BACKUP_PATH%" mkdir "%BACKUP_PATH%"

:: Lista de arquivos e pastas do modpack
set FILES=mods config resourcepacks shaderpacks options.txt

echo Criando backup dos arquivos existentes...
for %%F in (%FILES%) do (
    if exist "%MC_PATH%\%%F" (
        move "%MC_PATH%\%%F" "%BACKUP_PATH%\" >nul
    )
)

echo Copiando novos arquivos do modpack...
for %%F in (%FILES%) do (
    if exist "%MODPACK_PATH%\%%F" (
        xcopy "%MODPACK_PATH%\%%F" "%MC_PATH%\%%F\" /E /I /Y >nul
    )
)

echo.
echo Modpack instalado com sucesso! Pressione qualquer tecla para sair.
pause >nul
exit
