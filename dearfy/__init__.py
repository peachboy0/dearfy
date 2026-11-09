import loguru

from dearfy.logging import LoguruRichHandler, spetific_format_log

# ! Metadata

__name__ = 'dearfy'
__version__ = '0.1.15a1'
__author__ = 'peachboy0'

# ! Logging

loguru.logger.add(LoguruRichHandler(markup=True, show_path=False), format=spetific_format_log)