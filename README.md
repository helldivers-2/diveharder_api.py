![HD2 Community API](https://i.imgur.com/I1wosdV.png)

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
pip install -r ./requirements.txt</code></pre>

</details>

<details>
<summary>Project .env Setup</summary><br>
In ./src/cfg/env you can find a .env.example<br />
This can be renamed to .env and used as is, and it will use api.diveharder.com<br />
Or you may change the links to the AHGS API endpoints if you have them.

SECURITY_TOKEN is what you use to access the /admin/* endpoints <br />
SESSION_TOKEN is for accessing AHGS API's that require authentication
</details>

<details>
<summary>Local Deployment</summary>
<pre><code>
docker build -t myappimage .
docker run --name myappname -p 1234:1234 myappimage

</code></pre>
</details>

You are now fully setup, and can access your project at:
<pre><code>
localhost:1234
localhost:1234/docs
</code></pre>

</details>

<details>
<summary>Acknowledgements</summary>

Language | API | Database

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)[![Python Black](https://img.shields.io/badge/Python%20Black-000000?style=for-the-badge&logo=python&logoColor=FFFFFF&labelColor=000000&color=000000)](https://github.com/psf/black)
<br />@dealloc, @lambstream, and the @helldivers-2 organization
</details>
