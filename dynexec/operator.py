class DisallowedUseError(Exception):

    def __init__(self, *args):
        if args:
            self.err = args[0]
        else:
            self.err = None

    def __str__(self):
        if self.err:
            return f'Raised exception: {str(self.err)}'
        else:
            return f'{self.__name__} raised'


class Operator(object):
    def __init__(self):
        class Api(object):
            pass
        api = Api()
        self._script = None
        self._result = None
        api._message = self.message
        self._api = api

    class _Message:
        def __init__(self, body):
            self.body = body

    def message(self,body):
        self._result = self._Message(body)

    def _execute(self):
        from .sandbox import safe_builtins
        try:
            exec(self._script, {
                'api': self._api,
                '__name__': '__main__',
                '__builtins__': safe_builtins
            })
        except Exception as e:
            raise DisallowedUseError(e)
