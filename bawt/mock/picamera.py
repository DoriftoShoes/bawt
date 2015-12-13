import os

class PiCamera(object):

    ANNOUNCEMENT = '''
    ############################################################
    #                                                          #
    #              WARNING: picamera unavailable.              #
    #         bawt.mock.picamera will be used instead          #
    #                                                          #
    ############################################################
    '''
    AWB_MODES = {u'horizon': 9, u'off': 0, u'cloudy': 3, u'shade': 4, u'fluorescent': 6, u'tungsten': 5, u'auto': 1, u'flash': 8, u'sunlight': 2, u'incandescent': 7}
    CAMERA_CAPTURE_PORT = 2
    CAMERA_PORTS = (0, 1, 2)
    CAMERA_PREVIEW_PORT = 0
    CAMERA_VIDEO_PORT = 1
    CAPTURE_TIMEOUT = 30
    DEFAULT_ANNOTATE_SIZE = 32
    DEFAULT_FRAME_RATE_DEN = 1
    DEFAULT_FRAME_RATE_NUM = 30
    DRC_STRENGTHS = {u'high': 3, u'medium': 2, u'off': 0, u'low': 1}
    EXPOSURE_MODES = {u'auto': 1, u'fireworks': 12, u'verylong': 9, u'fixedfps': 10, u'backlight': 4, u'off': 0, u'antishake': 11, u'snow': 7, u'sports': 6, u'nightpreview': 3, u'night': 2, u'beach': 8, u'spotlight': 5}
    FLASH_MODES = {u'fillin': 4, u'on': 2, u'off': 0, u'auto': 1, u'torch': 5, u'redeye': 3}
    IMAGE_EFFECTS = {u'sketch': 6, u'posterise': 19, u'gpen': 11, u'colorbalance': 21, u'film': 14, u'pastel': 12, u'emboss': 8, u'denoise': 7, u'negative': 1, u'blur': 15, u'colorswap': 17, u'colorpoint': 20, u'saturation': 16, u'hatch': 10, u'watercolor': 13, u'cartoon': 22, u'none': 0, u'deinterlace1': 23, u'deinterlace2': 24, u'washedout': 18, u'solarize': 2, u'oilpaint': 9}
    MAX_IMAGE_RESOLUTION = (2592, 1944)
    MAX_RESOLUTION = (2592, 1944)
    MAX_VIDEO_RESOLUTION = (1920, 1080)
    METER_MODES = {u'average': 0, u'spot': 1, u'matrix': 3, u'backlit': 2}
    RAW_FORMATS = {u'rgb': 861030210, u'bgra': 1095911234, u'bgr': 859981650, u'rgba': 1094862674, u'yuv': 808596553}
    STEREO_MODES = {u'top-bottom': 2, u'none': 0, u'side-by-side': 1}
    VIDEO_OUTPUT_BUFFERS_NUM = 3
    _AWB_MODES_R = {0: u'off', 1: u'auto', 2: u'sunlight', 3: u'cloudy', 4: u'shade', 5: u'tungsten', 6: u'fluorescent', 7: u'incandescent', 8: u'flash', 9: u'horizon'}
    _DRC_STRENGTHS_R = {0: u'off', 1: u'low', 2: u'medium', 3: u'high'}
    _EXPOSURE_MODES_R = {0: u'off', 1: u'auto', 2: u'night', 3: u'nightpreview', 4: u'backlight', 5: u'spotlight', 6: u'sports', 7: u'snow', 8: u'beach', 9: u'verylong', 10: u'fixedfps', 11: u'antishake', 12: u'fireworks'}
    _FLASH_MODES_R = {0: u'off', 1: u'auto', 2: u'on', 3: u'redeye', 4: u'fillin', 5: u'torch'}
    _IMAGE_EFFECTS_R = {0: u'none', 1: u'negative', 2: u'solarize', 6: u'sketch', 7: u'denoise', 8: u'emboss', 9: u'oilpaint', 10: u'hatch', 11: u'gpen', 12: u'pastel', 13: u'watercolor', 14: u'film', 15: u'blur', 16: u'saturation', 17: u'colorswap', 18: u'washedout', 19: u'posterise', 20: u'colorpoint', 21: u'colorbalance', 22: u'cartoon', 23: u'deinterlace1', 24: u'deinterlace2'}
    _METER_MODES_R = {0: u'average', 1: u'spot', 2: u'backlit', 3: u'matrix'}
    _RAW_FORMATS_R = {808596553: u'yuv', 861030210: u'rgb', 859981650: u'bgr', 1095911234: u'bgra', 1094862674: u'rgba'}
    _STEREO_MODES_R = {0: u'none', 1: u'side-by-side', 2: u'top-bottom'}

    def __init__(self):
        super(self.__class__, self).__init__()
        self.resolution = ()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def start_preview(self, **options):
        pass

    def stop_preview(self):
        pass

    def close(self):
        pass

    def add_overlay(self, source, size=None, **options):
        pass

    def remove_overlay(self, overlay):
        pass

    def start_recording(
            self, output, format=None, resize=None, splitter_port=1, **options):
        pass

    def split_recording(self, output, splitter_port=1, **options):
        pass

    def wait_recording(self, timeout=0, splitter_port=1):
        pass

    def stop_recording(self, splitter_port=1):
        pass

    def record_sequence(
            self, outputs, format='h264', resize=None, splitter_port=1, **options):
        pass

    def capture(
            self, output, format=None, use_video_port=False, resize=None,
            splitter_port=0, **options):

        with open(output, 'a') as f:
            f.write(output)

    def capture_sequence(
            self, outputs, format='jpeg', use_video_port=False, resize=None,
            splitter_port=0, burst=False, **options):
        pass

    def capture_continuous(
            self, output, format=None, use_video_port=False, resize=None,
            splitter_port=0, burst=False, **options):
        pass

    @property
    def closed(self):
        """
        Returns ``True`` if the :meth:`close` method has been called.
        """
        return not self._camera

    @property
    def recording(self):
        """
        Returns ``True`` if the :meth:`start_recording` method has been called,
        and no :meth:`stop_recording` call has been made yet.
        """
        return any(
                isinstance(e, PiVideoEncoder) and e.active
                for e in self._encoders.values()
                )

    @property
    def exif_tags(self):
        pass

class PiVideoEncoder:

    def __init__(self):
        pass
