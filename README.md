<p align="middle"><img src='https://i.imgur.com/HfAUyKJ.png' /></p>  

# CSRF Prober
CSRF Prober is a advanced scanner for hunting down Cross Site Request Forgery bugs in web applications.

#### Working:
The typical flow of this scanner is :-
- Spiders the target website to find all pages.\n
- Finds all types of forms present on the each page.\n
- Hunts out hidden as well as visible parameter values.\n
- Submits each form with normal tokens & parameter values.\n
- Generates random token strings and sets parameter values.\n
- Submits each form with the crafted tokens.\n
- Finds out if the tokens are sufficiently protected.\n
- Generates custom proof of concepts after each successful bug hunt.

#### Features:

- [x] Features continuous crawling and scanning.
- [x] Support for both GET and POST requests.
- [x] Support for custom cookie values and generic headers.
- [x] Generates special crafted tokens for different parameters.
- [x] Submits forms in the normal way as well as with crafted token.
- [x] Rare chances of false positives occuring during scan.
- [x] Follows redirects when there is a 302 response.
- [x] Generates PoCs for both exploitable and not exploitable CSRFs.
- [x] Has a user-friendly interaction environment.
- [x] Everything is automated on demand.

#### Drawbacks:
The scanner has the following drawbacks presently:

➤ Normally the scanner assumes that every form has a hidden/visible parameter and token field.
➤ Changing or removing that token field usually causes a 403 Forbidden response.
➤ Spidering is restricted to domains of startpages (so doesn't work with all domains). :(

#### Requirements:

➾ mechanize
➾ urllib
➾ urllib2
➾ requests
➾ bs4
➾ lxml
➾ logging

#### Usage:

➲ Clone the script and launch it.
```
git clone https://github.com/the-Infected-Drake/<name>.git
cd <name>
```
➲ Install the dependencies.
```
pip install -r requirements
```
➲ Launch the script.
```
python <name>.py
```
➲ Enter the website target.
➲ Let the scanner load up.
➲ Keep track of PoCs which may appear (if bug exists).
➲ Once you find a bug, report it. ;)

#### Version:

- v1.0.0

#### To Do's:
- Associate multithreading for the better.

Thank you...
✎ @_tID (Team CodeSploit)
