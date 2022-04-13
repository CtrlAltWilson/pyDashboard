import os
import socket

#dashboard password
password = ""

debug_win = 1
guest = 1
isWin = True

#[leetcode]
csrftoken = ""
LEETCODE_SESSION = ""
Cookie = ""
# 0 = Disable, 1 = Centered Chart, 2 = 2 Charts
secondrow_charts = 0

#[Projects]
pName1 = pName2 = pName3 = pName4 = pName5 = pName6 = pName7 = pName8 = pName9 = pName10 = ""
pSrc1 = pSrc2 = pSrc3 = pSrc4 = pSrc5 = pSrc6 = pSrc7 = pSrc8 = pSrc9 = pSrc10 = ""
pDes1 = pDes2 = pDes3 = pDes4 = pDes5 = pDes6 = pDes7 = pDes8 = pDes9 = pDes10 = ""
pLin1 = pLin2 = pLin3 = pLin4 = pLin5 = pLin6 = pLin7 = pLin8 = pLin9 = pLin10 = ""
pName1  = "Raptor RC Bot"
pSrc1   = 'Projects/RaptorRCBot2-thumb.png'
pDes1   = "Commitment Alert! Telegram Notifier"
pLan1   = "Python, Telegram"
pLin1   = ""

pName2  = "ROSCA"
pSrc2   = 'Projects/ROSCA-thumb.png'
pDes2   = "Raptor Online Service Chat Assistant; Raptor's Support Chatbot"
pLan2   = "Snippet, NICE CXOne Studio, Telegram"
pLin2   = "is_Star"

pName3  = "Raspi"
pSrc3   = ''
pDes3   = "System Monitoring Bot"
pLan3   = "Python"
pLin3   = ""
 
pName4  = "RasRas"
pSrc4   = 'Projects/RasRas-thumb.png'
pDes4   = "Telegram AI Chatbot with Spotify and Smarthome Integration"
pLan4   = "Python, PySmartThings, Spotipy, Telegram"
pLin4   = ""

pName5  = "Portfolio Website"
pSrc5   = "Projects/pwebsite-thumb.png"
pDes5   = "Landing page"
pLan5   = "HTML, JS, CSS, PHP"
pLin5   = "https://www.wilsonngo.com"

pName6  = "Dashboard"
pSrc6   = "Projects/dashboardpic-thumb.png"
pDes6   = "Dashboard page showing current progress and projects"
pLan6   = "Python, Dash Plotly, React, HTML, JS, CSS"
pLin6   = "is_Here"

pName7  = "Spotipy for PiBoy"
pSrc7   = "Projects/spotipy-thumb.jpg"
pDes7   = "Visual (GUI) Spotify for a modified gameboy"
pLan7   = "Python, Spotipy"
pLin7   = "https://github.com/CtrlAltWilson/retro-ipod-spotify-client"

pName8  = "Crypto Wallet for PiBoy"
pSrc8   = "Projects/ElectrumPy-thumb.png"
pDes8   = "Visual (GUI) wallet for a modified gameboy"
pLan8   = "Python, ElectrumAPI"
pLin8   = ""

pName9  = "Commitment Alert!"
pSrc9   = "Projects/commitmentalert.png"
pDes9   = "Google Chrome extension for Salesforce commitments"
pLan9   = "HTML, JS, CSS"
pLin9   = "https://chrome.google.com/webstore/detail/commitment-alert/ckjfaimbgpioghcoekeenbmnbpjegeeo?hl=en&authuser=0"

pName10 = "RaptorHub"
pSrc10  = "Projects/sharepoint-thumb.png"
pDes10  = "Communication site"
pLan10  = "Microsoft SharePoint"
pLin10  = "is_Star"

pName11 = "LobbyGuard Suite"
pSrc11  = "Projects/LGSuite-thumb.png"
pDes11  = "LobbyGuard's Packaged Installer"
pLan11  = "Pascal Scripting, Inno Setup, Windows Batch, PowerShell Script"
pLin11  = "is_Star"

#   pName
#   pSrc
#   pDes
#   pLan
#   pLin

def get_ip():
    hostname = socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
