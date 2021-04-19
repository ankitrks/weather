# Weather APP - Project Setup

# Setup
- Clone project
- Install pyenv `brew install pyenv` or `apt install pyenv`
- cd to the project directory and run all of the below from this directory
- create python environment `virtualenv -p python3 pyenv`
- activate python environment `source pyenv/bin/activate`


### Database Setup

- Install Postgres: `brew install postgresql@10`
- Start the db: `pg_ctl -D /usr/local/var/postgresql@10 start`
- Create DB User: `createuser --pwprompt dbo`
- Creaete DB: `createdb -O dbuser weather_app`


### Running the server
- Run `python manage.py runserver`
- Open http://localhost:8000


### Testing

To run tests: `./manage.py test tests` 

To run with coverage:  `coverage run --branch --source='.' --omit='*migrations*' manage.py test api.tests`

`coverage report` will show the coverage data in CLI after you run the above command.

`coverage html` will generate pretty coverage files that you can browse using `open htmlcov/index.html`


### Automatic tests
Tests will automatically be run via GitHub Actions on all `push` events. To skip running tests add one 
of the following strings to the commit message:

- `[skip actions]`
- `[actions skip]`

_eg:_ `git commit -m "my commit [skip actions]"`

