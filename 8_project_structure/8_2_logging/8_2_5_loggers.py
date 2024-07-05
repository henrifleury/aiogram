import logging

logger = logging.getLogger()
print(logger)

logger = logging.getLogger(__name__)
print(logger)

print(dir(logger))

logger = logging.getLogger()
print(logger.parent)
logger = logging.getLogger(__name__)
print(logger.parent)

logger_1 = logging.getLogger('one.two')
print(logger_1.parent)
logger_2 = logging.getLogger('one.two.three')
print(logger_2.parent)

logger.warning('Предупреждение!')
logger.debug('Отладочная информация')