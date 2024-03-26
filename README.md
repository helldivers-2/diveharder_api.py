![HD2 Community API](https://i.imgur.com/I1wosdV.png){width=50%}

A proxy API providing endpoints to access Helldivers 2 API data, both RAW API Data and Formatted API Data.
<br />

<details>
<summary>Project Setup</summary>
<details>
<summary>Environment Setup</summary>

For a sanitary environment, dev work should be done inside a [Virtual Environment](https://docs.python.org/3/library/venv.html)<br>


<pre><code>python -m pip install --user --upgrade pip
python -m pip install --user virtualenv
python -m venv venv
# Windows
./venv/Scripts/activate
# Linux/MacOS
source ./venv/bin/activate
pip install -r requirements</code></pre>

</details>

<details>
<summary>Project .env Setup</summary><br>
<ul>
    <li> This project uses 3 .env files too keep data organized
    <ul>
        <li>API Links and Config
        <li>Database Config
        <li>Google Sheets Config
    </ul>
<ul>
<details>
<summary>api.env</summary>

<pre><code>STATUS_API_URL=https://api.diveharder.com/raw/status/
WARINFO_API_URL=https://api.diveharder.com/raw/warInfo/
PLANET_STATS_API_URL=https://api.diveharder.com/raw/planetStats/

TIME_DELAY=30
TIMEOUT=20</code></pre>

</details>

<details>
<summary>db.env</summary>

<pre><code>USER=postgres
PWD=postgress
PGSVR=localhost
PORT=5432
DB=mydb</code></pre>

</details>

<details>
<summary>gsheet.env</summary>

<pre><code>SPREADSHEET_KEY=</code></pre>

</details>
</details>
<details>
<summary>Local Deployment</summary>
<pre><code> uvicorn app.main:app --host 127.0.0.1 --port 80 --reload</pre></code>
</details>
You are now fully setup, and can access your project at:
<pre><code>http://localhost
http://localhost/docs</pre></code>

</details>
</details>

<details>
<summary>MIT License</summary>
Copyright (c) 2024 Chatter Chats

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</details>

<details>
<summary>Acknowledgements</summary>

Language | API | Database | Linter<br>
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)<br>
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)[![Python Black](https://img.shields.io/badge/Python%20Black-000000?style=for-the-badge&logo=python&logoColor=FFFFFF&labelColor=000000&color=000000)](https://github.com/psf/black)
<br><br>Chat's Dev Environment:<br>
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)<br>
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&background=white)![One Dark Pro](https://img.shields.io/badge/One%20Dark%20Pro-000000?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj4KICA8ZGVmcy8+CiAgPGNpcmNsZSBjeD0iMjU2IiBjeT0iMjU2IiByPSIyNTYiIGZpbGw9IiMyRDMyM0IiLz4KICA8Y2lyY2xlIGN4PSIyNTYiIGN5PSIyNTYiIHI9IjI0IiBmaWxsPSIjQ0I4MURBIi8+CiAgPHBhdGggZmlsbD0iI0NCODFEQSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTY1IDE3MGM0IDMyIDE2IDcyIDM4IDExMyAyMSA0MiA0NiA3NiA3MCA5NyAxMiAxMSAyNCAxOCAzNCAyMnMxOCAzIDI0IDBjNS0zIDEwLTkgMTMtMTggMy0xMCAzLTIzIDItMzgtMy0zMS0xNC02OS0zNC0xMDlhNiA2IDAgMDExMS01YzIwIDQxIDMyIDgxIDM1IDExMyAxIDE2IDEgMzAtMyA0Mi0zIDExLTkgMjEtMTkgMjZzLTIyIDQtMzQgMGMtMTEtNC0yNC0xMy0zNy0yNC0yNS0yMy01MS01OC03My0xMDBzLTM1LTg0LTM5LTExOGMtMi0xNy0xLTMyIDItNDRzOS0yMiAyMC0yN2M5LTYgMjEtNSAzMy0xIDExIDUgMjQgMTMgMzYgMjRhNiA2IDAgMDEtOCA5Yy0xMS0xMS0yMy0xOC0zMi0yMS0xMC00LTE4LTQtMjQtMXMtMTEgMTAtMTMgMjBjLTMgMTAtNCAyNC0yIDQweiIgY2xpcC1ydWxlPSJldmVub2RkIi8+CiAgPHBhdGggZmlsbD0iI0NCODFEQSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTAwIDI2OGM2IDcgMTYgMTQgMjkgMjBhNiA2IDAgMDEtNSAxMWMtMTQtNy0yNS0xNC0zMy0yMy04LTgtMTItMTgtMTItMjkgMS0xMSA3LTIxIDE3LTI5czIzLTE0IDM5LTIwYzMzLTEwIDc2LTE1IDEyNC0xMyA0NyAyIDkwIDEyIDEyMSAyNiAxNiA3IDI5IDE1IDM4IDIzIDggOSAxNCAyMCAxMyAzMSAwIDEwLTYgMjAtMTQgMjctOSA4LTIwIDE0LTM0IDE5YTYgNiAwIDExLTUtMTFjMTQtNSAyNC0xMCAzMS0xNyA3LTYgMTAtMTIgMTAtMTkgMS02LTItMTQtMTAtMjEtNy04LTE5LTE1LTM0LTIxLTI5LTEzLTcwLTIzLTExNy0yNS00Ni0yLTg4IDMtMTE5IDEzLTE1IDUtMjcgMTEtMzUgMTgtOSA2LTEyIDEzLTEzIDIwIDAgNiAzIDEzIDkgMjB6IiBjbGlwLXJ1bGU9ImV2ZW5vZGQiLz4KICA8cGF0aCBmaWxsPSIjQ0I4MURBIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xODkgMzk2YzEwLTMgMjItOSAzNS0xOGE2IDYgMCAxMTYgMTBjLTEzIDEwLTI2IDE2LTM4IDE5cy0yNCAyLTMzLTQtMTQtMTYtMTYtMjljLTItMTItMS0yOCAyLTQ0IDgtMzMgMjYtNzMgNTItMTEzczU2LTcyIDg0LTkyYzEzLTkgMjctMTYgMzktMTkgMTItNCAyNC0zIDM0IDMgOSA2IDE0IDE3IDE2IDI5IDIgMTMgMSAyOC0zIDQ0YTYgNiAwIDAxLTEyLTJjNC0xNiA1LTI5IDMtNDAtMi0xMC01LTE3LTExLTIxcy0xNC00LTI0LTJjLTEwIDMtMjIgOS0zNSAxOC0yNiAxOS01NiA1MC04MSA4OS0yNiAzOC00MyA3Ny01MCAxMDktMyAxNS00IDI5LTMgMzkgMiAxMSA2IDE4IDEyIDIxIDUgNCAxMyA1IDIzIDN6IiBjbGlwLXJ1bGU9ImV2ZW5vZGQiLz4KPC9zdmc+)
<br><br>Live Environment Hosted On:<br>
[![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)](https://render.com)
</details>
