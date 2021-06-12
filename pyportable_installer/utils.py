import os
import subprocess
from os import path as ospath
from threading import Thread

_pyinterpreter = 'python'


def mkdirs(start: str, *new: str):
    path = start
    for n in new:
        path += '/' + n
        if not ospath.exists(path):
            os.mkdir(path)
    return path


def send_cmd(cmd: str, ignore_errors=False):
    """
    
    Args:
        cmd:
            支持以下插入值:
                '{python}': 将被替换为 `globals:_pyinterpreter`
        ignore_errors
        
    References:
        https://docs.python.org/zh-cn/3/library/subprocess.html
        
    Raises:
        subprocess.CalledProcessError
    """
    # lk.loga(cmd, h='parent')
    global _pyinterpreter
    try:
        '''
        subprocess.run:params
            shell=True  传入字符串, 以字符串方式调用命令
            shell=False 传入一个列表, 列表的第一个元素当作命令, 后续元素当作该命
                        令的参数
            check=True  检查返回码, 如果 subprocess 正常运行完, 则返回码是 0. 如
                        果有异常发生, 则返回码非 0. 当返回码非 0 时, 会报
                        `subprocess.CalledProcessError` 错误
            capture_output=True
                        捕获输出后, 控制台不会打印; 通过:
                            output = subprocess.run(..., capture_output=True)
                            output.stdout.read()  # -> bytes ...
                            output.stderr.read()  # -> bytes ...
                        可以获取.
        '''
        subprocess.run(
            cmd.format(python=_pyinterpreter),
            shell=True, check=True, capture_output=True
        )
    except subprocess.CalledProcessError as e:
        if ignore_errors:
            return False
        else:
            raise e
    else:
        return True


def set_pyinterpreter(new_interpreter: str):
    global _pyinterpreter
    _pyinterpreter = new_interpreter


def exhaust(generator):
    # https://stackoverflow.com/questions/47456631/simpler-way-to-run-a
    # -generator-function-without-caring-about-items
    for _ in generator:
        pass


def wrap_new_thread(func):
    return lambda *args, **kwargs: runnin_new_thread(func, *args, **kwargs)


def runnin_new_thread(func, *args, **kwargs):
    t = Thread(target=func, args=args, kwargs=kwargs)
    t.start()
    return t
