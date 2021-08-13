# Overview

This Flask Blueprints app calculates the distance from any given address to the Moscow Ring Road (MKAD) written in Python. The API I use is the Yandex Geocoder API. The challenge for me for this test is how I should learn about Flask Blueprints and Geocoder. It took quite a while for me to learn Flask as it was my first time using it. Yandex Geocoder itself requires an API key. To be able to get the key can visit the web https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html. The difficulty is because the web itself is in Russian so it took me a while to get the Yandex Geocoder API key. But overall, the results are quite satisfactory for me who is the first time using Flask and Geocoder API.


## How to use
For how to run it, you must create a new virtual environment.After that run the flask run command.

``` $ python -m venv.venv ```

Then Flask must be activated first.

``` $ venv\Scripts\activate```

Then change the flask environment to Development.

``` $ set FLASK_ENV=development ```

After that run the flask run command.

``` $ flask run ```

For more details, see the image below.

<img width="960" alt="set flask run" src="https://user-images.githubusercontent.com/73238313/129370030-fab2d23d-8855-4565-a351-5782295aae4b.PNG">

After that, you can go to the link provided.

http://127.0.0.1:5000/

## Test

Before run the program, make sure the server already running.

``` $ python Test_Task.py ```
