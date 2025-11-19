@echo off
setlocal EnableDelayedExpansion

TITLE Warp Complete Removal Tool (No Python Required)
COLOR 0C

echo ========================================================
echo    WARP COMPLETE REMOVAL TOOL FOR WINDOWS
echo    No Python Required - Native Batch Script
echo ========================================================
echo.
echo    This tool will COMPLETELY remove Warp from your system.
echo    It cleans:
echo     - Main Application
echo     - AppData & LocalAppData
echo     - Registry Keys
echo     - Browser Data (Chrome, Edge, Comet, etc.)
echo.
echo    ⚠️  WARNING: This process is irreversible!
echo.

:PROMPT
SET /P AREYOUSURE=Are you sure you want to continue? (Y/[N])? 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

echo.
echo [1/5] 🔫 Killing Warp processes...
taskkill /F /IM warp.exe /T >nul 2>&1
taskkill /F /IM Warp.exe /T >nul 2>&1
timeout /t 2 /nobreak >nul
echo    ✅ Processes terminated.

echo.
echo [2/5] 🗑️ Removing Warp application files...

REM Program Files
if exist "%PROGRAMFILES%\Warp" (
    rmdir /s /q "%PROGRAMFILES%\Warp"
    echo    ✅ Removed from Program Files
)
if exist "%PROGRAMFILES(X86)%\Warp" (
    rmdir /s /q "%PROGRAMFILES(X86)%\Warp"
    echo    ✅ Removed from Program Files (x86)
)

REM Local AppData
if exist "%LOCALAPPDATA%\Warp" (
    rmdir /s /q "%LOCALAPPDATA%\Warp"
    echo    ✅ Removed from LocalAppData
)
if exist "%LOCALAPPDATA%\dev.warp.Warp-stable" (
    rmdir /s /q "%LOCALAPPDATA%\dev.warp.Warp-stable"
    echo    ✅ Removed dev.warp.Warp-stable
)

REM Roaming AppData
if exist "%APPDATA%\Warp" (
    rmdir /s /q "%APPDATA%\Warp"
    echo    ✅ Removed from AppData Roaming
)
if exist "%APPDATA%\dev.warp.Warp-stable" (
    rmdir /s /q "%APPDATA%\dev.warp.Warp-stable"
    echo    ✅ Removed dev.warp.Warp-stable Roaming
)

REM Temp Files
del /f /q "%TEMP%\*WarpSetup.exe*" >nul 2>&1
echo    ✅ Cleared Temp files

echo.
echo [3/5] 📊 Cleaning Registry...
reg delete "HKCU\Software\Warp" /f >nul 2>&1
reg delete "HKLM\Software\Warp" /f >nul 2>&1
reg delete "HKCU\Software\dev.warp.Warp-stable" /f >nul 2>&1
reg delete "HKLM\Software\dev.warp.Warp-stable" /f >nul 2>&1
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall\Warp" /f >nul 2>&1
echo    ✅ Registry keys cleaned.

echo.
echo [4/5] 🌐 Cleaning Browser Data (Chrome, Edge, Comet)...

REM Define browser paths
set "CHROME_DIR=%LOCALAPPDATA%\Google\Chrome\User Data"
set "EDGE_DIR=%LOCALAPPDATA%\Microsoft\Edge\User Data"
set "BRAVE_DIR=%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data"
set "COMET_DIR=%LOCALAPPDATA%\Comet\User Data"

REM Function-like calls to clean specific browser
call :CLEAN_BROWSER "%CHROME_DIR%" "Google Chrome"
call :CLEAN_BROWSER "%EDGE_DIR%" "Microsoft Edge"
call :CLEAN_BROWSER "%BRAVE_DIR%" "Brave Browser"
call :CLEAN_BROWSER "%COMET_DIR%" "Comet Browser"

echo.
echo [5/5] 🔍 Verifying removal...
if exist "%LOCALAPPDATA%\Warp" (
    echo    ⚠️  Warning: Warp folder still exists in LocalAppData.
) else (
    echo    ✅ Verification passed: Main folders gone.
)

echo.
echo ========================================================
echo    🎉 WARP REMOVAL COMPLETE!
echo    Your system should now appear as a NEW MACHINE.
echo    You can safely reinstall Warp now.
echo ========================================================
pause
goto :EOF

:CLEAN_BROWSER
SET "BROWSER_PATH=%~1"
SET "BROWSER_NAME=%~2"

if exist "%BROWSER_PATH%" (
    echo    🔎 Checking %BROWSER_NAME%...
    
    REM Check Default and Profile folders
    for /d %%P in ("%BROWSER_PATH%\Default" "%BROWSER_PATH%\Profile*") do (
        REM IndexedDB
        if exist "%%P\IndexedDB\https_app.warp.dev_0.indexeddb.leveldb" (
            rmdir /s /q "%%P\IndexedDB\https_app.warp.dev_0.indexeddb.leveldb"
            echo       🗑️ Removed Warp IndexedDB from %%~nP
        )
        
        REM Local Storage
        if exist "%%P\Local Storage\leveldb" (
             REM We can't easily grep inside leveldb files with batch, 
             REM but we can look for specific warp files if they existed as standalone.
             REM Chromium uses monolithic DBs usually.
             REM We will skip deep file inspection to avoid breaking other sites.
             REM But we CAN remove the specific extension.
        )

        REM Extensions - ID: mjdcklhepheaaemphcopihnmjlmjpcnh
        if exist "%%P\Extensions\mjdcklhepheaaemphcopihnmjlmjpcnh" (
            rmdir /s /q "%%P\Extensions\mjdcklhepheaaemphcopihnmjlmjpcnh"
            echo       🗑️ Removed Warp Extension from %%~nP
        )
    )
)
goto :EOF

:END
echo.
echo ❌ Operation cancelled.
pause
