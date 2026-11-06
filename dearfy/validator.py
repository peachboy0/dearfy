import functools
from datetime import date, datetime

import dateparser

from dearfy.action import Action
from dearfy.field import field
from dearfy.functions import formatting_kwargs
from dearfy.typing import DateLike, DatePickerValue

# ! Validator Kwargs Base

class ValidatorKwargsBase:
    VALIDATE_KWARGS_KEYS: tuple[str, ...] = ()
    VALIDATE_ERRORS_IGNORE: bool = False

    def __init__(self, **kwargs: object) -> None:
        self.kwargs: dict[str, object] = kwargs
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({formatting_kwargs(**self.kwargs)})'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def validate_value(self, value: object) -> object:
        return value
    
    def validate(self, **kwargs: object) -> dict[str, object]:
        for key, value in kwargs.copy().items():
            if key in self.VALIDATE_KWARGS_KEYS:
                kwargs[key] = self.validate_value(value)
        return kwargs

# ! Validate Callbacks

class ValidateKwargsAction(ValidatorKwargsBase):
    VALIDATE_KWARGS_KEYS: tuple[str, ...] = (
        'callback',
        'drag_callback',
        'drop_callback',
        'on_close',
    )

    def __init__(self, *, app: object | None=None, **kwargs: object) -> None:
        super().__init__(app=app, **kwargs)

    @staticmethod
    def _validate_action(
        app: object,
        action: str | tuple[str, str] | Action | None
    ) -> Action | None:
        if action is None or callable(action) or isinstance(action, Action):
            return action
        if isinstance(action, (str, tuple)):
            if not hasattr(app, '_actioner'):
                raise AttributeError("App object has no '_actioner' attribute")
            return app._actioner.get(action)
        raise ValueError(f"Invalid action type: {type(action)}")
    
    def validate_value(self, value: str | tuple[str, str] | Action | None) -> Action | None:
        app: object | None = self.kwargs.get('app', None)
        if app is None:
            if self.VALIDATE_ERRORS_IGNORE:
                return None
            else:
                raise RuntimeError('Argument of validator \'app\' not be `None`.')
        return field(
            value,
            default=None,
            wrap=functools.partial(self._validate_action, app),
            nullable=True
        )

# ! Validate Date Values

class ValidateKwargsDate(ValidatorKwargsBase):
    VALIDATE_KWARGS_KEYS: tuple[str, ...] = ('default_value', )

    def __init__(self, *, app: object | None=None, **kwargs: object) -> None:
        super().__init__(app=app, **kwargs)

    @staticmethod
    def _to_datetime(value: DateLike | None) -> datetime:
        if isinstance(value, datetime):
            return value
        elif isinstance(value, date):
            return datetime(value.year, value.month, value.day)
        elif isinstance(value, str):
            result = dateparser.parse(value)
            if result is not None:
                return result
        elif isinstance(value, (float, int)):
            return datetime.fromtimestamp(float(value))
        elif isinstance(value, dict):
            try:
                return datetime(value['year'] + 1900, value['month'] + 1, value['month_day'])
            except KeyError:
                raise ValueError('Incorrect dictionary format')
        raise TypeError('Unsupported value type.')

    @staticmethod
    def _to_value(value: DateLike | None) -> DatePickerValue:
        if isinstance(value, dict) and ('year' in value) and ('month' in value) and ('month_day' in value):
            return value
        dt = ValidateKwargsDate._to_datetime(value)
        return {'year': dt.year - 1900, 'month': dt.month - 1, 'month_day': dt.day}

    def _validate_value(self, value: DateLike | None) -> DatePickerValue | None:
        try:
            return self._to_value(value)
        except (ValueError, TypeError):
            pass

    def validate_value(self, value: DateLike | None) -> DatePickerValue:
        dt = datetime.now()
        return field(value,
            nullable=False,
            default_wrapped=False,
            wrap=self._validate_value,
            default_factory=( lambda: {'year': dt.year - 1900, 'month': dt.month - 1, 'month_day': dt.day} )
        )