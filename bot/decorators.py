from functools import wraps


def input_error(func):
    @wraps(func)
    def run(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
        except KeyError:
            print('Contact does not exist.')
        except IndexError:
            print('Contact does not exist.')

    return run
