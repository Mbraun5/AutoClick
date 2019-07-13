# used for timing functions for testing purposes
from functools import wraps
import gc
import timeit


def MeasureTime(f):
    @wraps(f)
    def _wrapper(*args, **kwargs):
        gcold = gc.isenabled()
        gc.disable()
        start_time = timeit.default_timer()
        try:
            result = f(*args, **kwargs)
        finally:
            elapsed = timeit.default_timer() - start_time
            if gcold:
                gc.enable()
            print('Function "{}": {}s'.format(f.__name__, elapsed))
        return result
    return _wrapper


class MeasureBlockTime:
    def __init__(self, name="(block)", no_print=False, disable_gc=True):
        self.name = name
        self.no_print = no_print
        self.disable_gc = disable_gc

    def __enter__(self):
        if self.disable_gc:
            self.gcold = gc.isenabled()
            gc.disable()
        self.start_time = timeit.default_timer()

    def __exit__(self,ty,val,tb):
        self.elapsed = timeit.default_timer() - self.start_time
        if self.disable_gc and self.gcold:
            gc.enable()
        if not self.no_print:
            print('Function "{}": {}s'.format(self.name, self.elapsed))

        # re-raise any exceptions
        return False

    '''
    # Same use case
    li = []
    for i in range(10000000):
        new = random.randint(0, 10000)
        li.append(new)

    @utils.MeasureTime
    def test1(li):
        new = []
        for i in range(len(li)):
            new.append(2 * li[i])

    @utils.MeasureTime
    def test2(li):
        new = []
        for elem in li:
            new.append(elem * 2)

    @utils.MeasureTime
    def test3(li):
        for index, elem in enumerate(li):
            li[index] = elem * 2

    print("here")
    test1(li)
    test2(li)
    test3(li)
    '''

    '''
    Image Editing
    pic = Image.open('sprites/icon_orig.png').convert('RGB')
    for i in range(48):
        for j in range(48):
            try:
                r, g, b = pic.getpixel((i, j))
            except:
                print(i, j)
                exit()
            print(r, g, b)
            if (r, g, b) != (71, 112, 76):
                pic.putpixel((i, j), (56, 78, 50))
                #pic.putpixel((i, j), (0, 0, 0))
            else:
                pic.putpixel((i, j), (255, 255, 255))
    pic.save('sprites/icon.png')
    '''