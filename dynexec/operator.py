def an_error(e):
    er = ValueError(str(e))
    return er


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
            raise an_error(e)
