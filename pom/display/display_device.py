from abc import ABC


class DisplayDevice(ABC):
    def flush_buffer(self):
        """
        光栅数据到真实屏幕上
        """
        raise NotImplementedError

    def render(self):
        """
        从矢量数据到光栅数据
        """
        raise NotImplementedError
