from weboa import os

class FileSystem:

    @staticmethod
    def is_file_changed(_weboa, i, precss="less"):
        if precss not in _weboa.keys():
            _weboa[precss] = dict()
        if i not in _weboa[precss].keys():
            _weboa[precss][i] = 0

        ts0 = _weboa[precss][i]
        ts1 = os.stat(i).st_mtime

        return ts0 != ts1