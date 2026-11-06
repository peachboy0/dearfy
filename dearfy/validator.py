import functools
from datetime import datetime

import dateparser

from dearfy.action import Action
from dearfy.field import field
from dearfy.functions import formatting_kwargs
from dearfy.typing import DatePickerValue

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
    def _validate_value(value: datetime | DatePickerValue | str | None) -> DatePickerValue | None:
        if isinstance(value, dict):
            return value
        dt = None
        if isinstance(value, datetime):
            dt = value
        elif isinstance(value, str):
            try:
                dt = datetime.strptime(value, "%G-W%V-%u")
            except:  # noqa: E722
                dt = dateparser.parse(value)
        if dt is not None:
            {'month_day': dt.day, 'year': dt.year - 1900, 'month': dt.month - 1}

    def validate_value(self, value: datetime | DatePickerValue | str | None) -> DatePickerValue:
        if (result := (value)) is not None:
            return result
        return field(
            value,
            nullable=False,
            default_wrapped=False,
            wrap=self._validate_value,
            default_factory=(
                lambda: {
                    'month_day': datetime.now().day,
                    'year': datetime.now().year - 1900,
                    'month': datetime.now().month - 1
                }
            )
        )