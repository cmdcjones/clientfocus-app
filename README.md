# clientfocus-app
Requires Python 3.9 or higher
## Installation

Start by cloning the repository:

```bash
git clone https://github.com/cmdcjones/clientfocus-app
```

Change directory to the root folder (`clientfocus-app`) and create a virtual environment and initialize it:

```
python3 -m venv venv
source venv/bin/activate
```

Install pip packages using pip and requirements.txt:

```
pip install -r requirements.txt
```

Create a dotenv file in the root `clientfocus-app` folder with no name and the `.env` extension. Place the following text into the file:

```
export FLASK_APP=clientfocus-app
export FLASK_DEBUG=true
```

Initialize the database and start the development server at localhost:5000 with the following commands:

```
flask init-db
flask run
```
