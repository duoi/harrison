# harrison

This was built using Django 3 and Django Rest Framework for the APIs. To simplify things I used generic viewsets with the appropriate mixins, although I stopped short of using their pre-built functions and wrote my own creation and updating methods, as well as my own validation where appropriate. I also opted against using `ModelSerializer`s and similar to ensure
that none of the core logic is abstracted away during this exercise.

This project was interesting to develop. As I worked through it, several considerations needed to be made:-

* What do labels represent to doctors and the researchers
* How can we begin to make the data suitable for research
* The various compliance considerations we need considering it is medical data

Eventually I decided to extend the `label` app and begin relating `disease`s to those labels, and also relating medical standards (such as ICD-9 and ICD-10) for those diseases. All of these were put into their own tables - with relations where appropriate.

Doctors have the ability to add and modify medical imagry, as well as attach labels to those images, but researchers are only given read-only access. Simularly, the researchers are the only ones able to manipulate labels and doctors are just given read-only access to those labels. This can go either way depending on how the business works, i.e maybe the researchers are the ones attaching the labels and the doctors just do the uploads, but I added it in there just to demonstrate some differing permissions handling. In this I also limited doctors to only being able to view their own uploads - i.e, a doctor cannot view another person's uploads.

Part of the compliance aspects added involved including `reversion` to store, in JSON, any database row updates to the core clinical diagnoses. This allows us to go back in time and view what entries were updated and by whom. There is also a model called `Event` which tracks every interaction with the website (as middleware) and stores the full request headers, the url accessed, when it was accessed and by which user (if logged in).

It's worth noting that I've only added tests for the `disease` app - on the serializers and the models. But I've made factories (using `factory_boy`) for almost all of the models.

![UML diagram](https://i.imgur.com/Tgnt3MN.png)

The approach I took is pseudo-production. I made several decisions along the way that were appropriate for a demo, but things
I wouldn't implement in a production environment. This involves various things like:

1. Using the default DRF token implementation, I would prefer to use [rest knox](https://github.com/James1345/django-rest-knox) or something.
2. Debug mode is enabled.
3. Using SQLITE3 vs. Postgres - I would have changed my schema somewhat if I had access to JSONB fields or Array fields.
4. I didn't add the ability to link a medical image to a specific patient. This would make more sense in the real world, of course, but I thought it would over-complicate things for this exercise and force me to look into datascrubbing to avoid leaking PII to the researchers.
5. I would attach fields similar to `is_active` to be able to show, hide or achive various different table rows as needed.
6. I would almost always sub out the default `auth` model rather than sticking with Django's default one.
7. I might opt for using UUIDs or some hash as API identifiers rather than exposing primary keys
8. I don't really like my approach to how I associated classification codes to diseases - I feel that the individual foreign key relations could have been better handled with a m2m field or a reversed foreign key relationship, but I left it in there because I timeboxed the exercise.
9. I'd have some sort of linter in place, and of course have larger code coverage.
10. I'd probably make Django admin usable - at the moment I haven't registered any of the apps for Admin.
11. Uploaded files would of course be sent somewhere else and not kept on the instance's storage
12. Also worth mentioning that I don't like how permissions are being handled here: I'd much rather add [django-guardian](https://django-guardian.readthedocs.io) and have a more complex permissions system associated with groups that can be stepped in and out of.
13. Separate serializers for list and detail views would probably go in as well (overriding `get_serializer` and switching based on the action)

-----

# Running the app

1. Run `pip install -r requirements.txt` to install the dependencies
2. Run `python manage.py migrate` to create the sqlite3 database and the various tables
3. Run `python manage.py create_user_groups` to create the user groups - this can of course be moved to a migration action
4. Run `python manage.py create_dummy_data` to populate the database with a random number of records, as well as providing auth information for `research`, `doctor` and pre-seeded `doctor` users.
5. You can then start the environment by calling `python manage.py runserver_plus --cert CERT`
6. It should become available on `https://127.0.0.1:8000/`.

Django Rest Framework provides a browsable API out of the box, to access it navigate to `/admin` and log via the admin panel, then navigate to `/api/v1/` and Django debug should get angry and tell you which endpoints are possible to visit.

-----

# Deployment considerations

Depending on my code repo, say if it were bitbucket or gitlab, I would probably use their pipeline automation channels. The first step would be to run a linter, then to run the tests, and if everything passes then it would be merged to master. When something is merged into master we'd immediately build it with Docker or some other containerisation tool and push it out to our cloud provider - I'm using AWS in this example as its the freshest in my mind. 

The next steps really depend on capacity - AWS Beanstalk is probably the easiest in terms of a one-click solution - it sets all of the load balancers, security groups, storage and standing instances up and down for you once you go through a trivial config page. You could use cloud formation, or ansible or terraform if you want to roll your own. 

If you play your cards right you could also stay within the AWS free tier - I think t3.micros are probably enough for this - although I would usually opt for a minimum of two instances for the app server and have RDS hold the database information independently. I'd keep secrets in AWS Systems Manager' Parameter Store and not in `settings.py`, naturally. 

This would change somewhat if I'm using Azure of course, but the idea is similar.

Avoiding downtime is possible if we don't have any database migrations - if we do then it becomes somewhat more difficult to have blue/green deployments. For just frontend changes we can add cache busters stamped with `master` commit hashes so that on redeploy the user would just download the new frontend and go along their way.
