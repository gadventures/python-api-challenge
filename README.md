# Python API Challenge

Thank you for your interest in joining G Adventures. This challenge will allow
us to further evaluate where you may potentially fit from a technical
perspective. We're really excited to see what you can do.

## Submission

* Fork this project on Github. You will need to create an account if you don't already have one.
* Complete the project as described, within your fork.
* Push all of your changes to your fork on github and submit a pull request.
* We will be notified of your pull request (or feel free to email us as well), and we'll review!

If you don't wish to publicize your work on this challenge, you may simply send
the completed project in an archived file to [recruiting_tech@gadventures.com](mailto:recruiting_tech@gadventures.com)

We recommend using *Python 3* for all work you produce, but we're also happy if
you use *Go*, or *Javascript*

## Project

This project should not take you more than 4 hours. If you require extra time to
get familiar with documentation, please take your time. In the end, we don't
want you to feel rushed, but we also don't want you spending too much time on
this.

For this project, you'll build a script which consumes data from a local API
(provided). Your script will transform this data in various ways (described
below), and be output as a CSV.

### Local API

Provided within this project is a local API, which uses [Django REST Framework](http://www.django-rest-framework.org/)
to provide a simple, standards-compliant API. Below, within the `Getting
Started` section, you'll find instructions on how to run the API server.

Once running, your only task for the server, is to load data into the API. We've provided a
`departures.json` file, which you should load into the server using [Django Data
Migrations](https://docs.djangoproject.com/en/2.0/topics/migrations/#data-migrations).
You will need to make a new *empty* migration as per the documentation, and
write the code to read the file and [insert it into the Departure
Model](https://docs.djangoproject.com/en/2.0/ref/models/instances/#creating-objects).

After this data is loaded, you should be able to view it all at
`http://localhost:8000/departures`, assuming you're running the local API
server.

### Data Collection Script

Your primary task within this project is to build a script which consumes data
from your local API. Within this API, you have a `/departures` URL, which is a
multi-page listing of trips, operating on various dates.

The script will be expected to query for `/departures`, and iterate over every
page, collecting all `departures` referenced from the API.

To iterate over a page, the script simply needs to follow the `next` links,
which look like so in the API response:

```
{
    "count": 100,
    "next": "http://localhost:8000/departures/?limit=50&offset=50",
    "previous": null,
    "results": [`
        ...
    ]

```

Once the script has collected all `departures`, from all pages, it will need to
filter down the data to only include the following:

1. Filter down so that your local data only contains `departures` with a `start_date` after `June 1st, 2018`

2. Additionally, filter down to only `departures` of `category = Adventurous`

At this point, your script should have a subset of the data fetched from the
API. You will now want to write this information into a CSV. For the output,
ensure the following:


1. Every attribute within `departures` is given its own column, and there's a
   header within the CSV with the attribute names, title-case.
2. Every remaining `departures` instance is written to a row.

The CSV should be written to the root folder of your project, with whatever file
name you believe is relevant.

... And that's it! Feel free to try new technologies, as long you're within the
scope of the challenge requirements, we're happy.

## Goal

We'd like to get a sense of how you work, specifically within areas that are
unexplored territory, and if you are able to fulfill all the requirements scoped
for a task.

We're looking for code that is well structured, documented, and testable.

Please provide two or so paragraphs within the `README` of how you went about
completing the challenge.

## Getting Started

If you have not done so yet, you'll want to [install
Git](https://help.github.com/articles/set-up-git/), and
[pip](https://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x)

We've provided some scaffolding to save you time. You'll want to clone the fork
you made on Github. The url you fork is dependent on your username, but it'd
look something like this:

    git clone https://github.com/{YOUR USERNAME}/python-api-challenge.git

Once downloaded, you'll want to use `pip` to install the project requirements.

    cd ./python-api-challenge
    pip install -r requirements.txt

Once installed, you can run the Django project like so:

    python manage.py runserver

You should now be able to visit your project at `http://127.0.0.1:8000/departures`

We've included a basic Django project and a `Departure` model with some fields,
which you will consume.

Otherwise, the rest is up to you!

## Stuck?

If you get stuck -- Please don't hesitate to email
[recruiting_tech@gadventures.com](mailto:recruiting_tech@gadventures.com). We are looking for
candidates who are not afraid to ask questions, and explore new ideas. Asking
questions will not hurt your chances.

## Thank You!

We're excited for the opportunity to work with you. We look forward to seeing
what you create.
