import loguru
import logging as std_logging
# > Local Imports
from dearfy.logging import LoguruRichHandler, spetific_format_log

# ! Metadata

__name__ = 'dearfy'
__version__ = '0.1.5a1'
__author__ = 'peachboy0'

# ! Logging

loguru.logger.configure(
    handlers=[
        {
            'sink': LoguruRichHandler(
                markup=True,
                show_path=False,
            ),
            'format': spetific_format_log,
            'level': std_logging.NOTSET,
        }
    ]
)