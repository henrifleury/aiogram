import logging

logger = logging.getLogger(__name__)

try:
    print(4 / 2)
    print(2 / 0)
except ZeroDivisionError:
    logger.error('Тут было исключение')

try:
    print(6 / 2)
    print(2 / 0)
except ZeroDivisionError:
    logger.error('Тут было исключение', exc_info=True)

logger = logging.getLogger(__name__)

try:
    print(8 / 2)
    print(2 / 0)
except ZeroDivisionError:
    logger.exception('Тут было исключение')