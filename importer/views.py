import logging
from ast import parse

import requests
from django.core.management import BaseCommand

# Create your views here.
from django.shortcuts import render
from django.template.base import logger
from rest_framework.utils import json

logger = logging.getLogger("command")

API_END_POINT = ("https://api.waqi.info/feed/{city}/?token=f8c14b8df33312a1d1842fe35e360768f958f4c0")


def aquire_pm25_data_from_api(city: str):

    request_url = API_END_POINT.format(
        city=city,
    )
    res = requests.get(request_url)
    res.raise_for_status()
    row_data = json.loads(res.content)["data"]

    logger.info("Finish importing data of PM2.5")

    return row_data


def call_importer(request):
    city = request.GET["city"]

    res = aquire_pm25_data_from_api(city)

    return res


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--from_date", default=None)
        parser.add_argument("--to_date", default=None)
        parser.add_argument("--city", default='bangkok')

    def handle(self, *args, **options):
        from_date = options.get("from_date")
        to_date = options.get("to_date")
        city = options.get("city")

        if from_date is not None:
            try:
                from_date = parse(from_date)
            except (ValueError, OverflowError) as e:
                raise ValueError("The format of the from_date is wrong: %s." % e)

        if to_date is not None:
            try:
                to_date = parse(to_date)
            except (ValueError, OverflowError) as e:
                raise ValueError("The format of the to_date is wrong: %s." % e)
        logger.info("start: update exchange rate")
        aquire_pm25_data_from_api(city)
        logger.info("end: update exchange rate")

