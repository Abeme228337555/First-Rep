import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='logs_example.log',
                    filemode='w',
                    format='NEW LOG - %(asctime)s - %(levelname)s: %(message)s')
logging.debug('debug example')
logging.info('info example')
logging.warning('warning example')
logging.error('error example')
logging.critical('critical example')