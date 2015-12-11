import os

class PiCamera(object):

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
