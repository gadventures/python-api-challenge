# API Team Challenge

Thank you for your interest in joining G Adventures, and specifically being part
of the API Team! We're really excited to see what you can do.

## Submission

* Fork this project on Github. You will need to create an account if you don't already have one.
* Complete the project as described within your fork.
* Push all of your changes to your fork on github and submit a pull request.
* We will be notified of your pull request (or feel free to email us as well), and we'll review!

If you don't wish to publicize your work on this challenge, you may simply send
the completed project in an archived file to [bartekc@gadventures.com](mailto:bartekc@gadventures.com)

## Project

This project should not take you more than 4 hours. If you require extra time to
get familiar with documentation, please take your time. In the end, we don't
want you to feel rushed, but we also don't want you spending too much time on
this.

For this project, we want you to use the [Django REST Framework](http://www.django-rest-framework.org/) library to construct an API that displays a list of Trips.

A Trip model has been supplied for you within the project. It has a `name`,
`start_date`, and `finish_date`. If you wish to extend this model, feel free to
do so. The model has no data, you'll want to understand how to interact with
[Django Models](https://docs.djangoproject.com/en/1.9/topics/db/models/) to
create some data. Feel free to include a script of creating such data in your
submission.

Your API will provide this Trip data in a RESTful manner, ideally responding in
JSON (Built-in to Django REST Framework)

Once you have constructed the API to display these trips, you'll create a page
that displays the list of Trips, as per the response of the API.

Stylistically, how you display these trips is up to you. Data-wise, as long as the data is coming from the API view you've built, we
are agnostic as to what technology you use to query that view. Generally, it'd be in Javascript using an _AJAX_ call, or you can do something else. Feel like displaying it on an Android application instead? That's fine, as long as you built the API for it :)

... And that's it! Feel free to try new technologies, as long you're within the
scope of the challenge requirements, we're happy.

## Goal

We'd like to get a sense of how you work, specifically within areas that are
unexplored territory, and if you are able to fulfill the requirements scoped
for a project.

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

    git clone https://github.com/{YOUR USERNAME}/apichallenge.git

Once downloaded, you'll want to use `pip` to install the project requirements.

    cd ./apichallenge
    pip install -r requirements.txt

Once installed, you can run the Django project like so:

    python manage.py runserver

You should now be able to visit your project at `http://127.0.0.1:8000/trips`

We've included a basic Django project and a `Trip` model with some fields.
You'll want to focus on understanding how to integrate Django REST Framework
into an existing Django project. Their documentation is great!

We have also supplied a blank template, which lives in
`trips/templates/trips/index.html`. This is the template you see when you visit
`/trips` within your project.

Otherwise, the rest is up to you!

## Stuck?

If you get stuck -- Please don't hesitate to email
[bartekc@gadventures.com](mailto:bartekc@gadventures.com). We are looking for
candidates who are not afraid to ask questions, and explore new ideas. Asking
questions will not hurt your chances.

## Thank You!

We're excited for the opportunity to work with you. We look forward to seeing
what you create.
