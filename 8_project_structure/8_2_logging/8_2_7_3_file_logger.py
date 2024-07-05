import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('logs.log', mode='w')

logger.addHandler(file_handler)

print(logger.handlers)

logger.warning('Это лог с предупреждением!')