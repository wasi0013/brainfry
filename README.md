#[BRAIN FRY](http://brainfry.heroku.com)

encrypts text to emoji and decrypts brainfry encrypted emojis to text.

####[demo](http://brainfry.heroku.com)

##powered by:
* [Django 1.10](https://www.djangoproject.com/)
* [twemoji - (Twitter emoji)](https://twitter.github.io/twemoji/)
* [Bootstrap](https://getbootstrap.com/)
* [facebook like & comment plugin](https://developers.facebook.com/docs/plugins/comments)


##Test using Virtualenv
 * clone the repo
 * cd to the repo directory
 * `pip install virtualenv` (only if virtualenv is not already installed)
 * `virtualenv -p /usr/bin/python3.5 .env` (create virtual environment)
 * `source .env/bin/activate` (activate the virtual environment )
 * `pip install -r requirements.txt` (install dependencies)
 *  `python3 manage.py runserver` (run the server)
 *  Test the app via browser typically at http://localhost:8000

##note
Inspired by [firefox codemoji](https://blog.mozilla.org/press-uk/2016/06/28/meet-codemoji-mozillas-new-game-for-teaching-encryption-basics-with-emoji/)
