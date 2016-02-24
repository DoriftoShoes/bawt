import click

from bawt.subsystems.camera import Camera
from bawt.subsystems.irrigation import Irrigation

@click.group()
def cli():
    pass

@cli.command()
@click.option('--state',help='turn it on yo')
@click.option('--runtime', help='Time of the run')
@click.argument('zone')
def irrigation(state, zone, runtime):
    irrigation = Irrigation()

    zone = int(zone)
    state = str(state)

    if state == 'on':
        irrigation.start(zone)
    elif state == 'off':
        irrigation.stop(zone)
    elif state == 'timed':
        runtime = int(runtime)
        irrigation.timed_run(zone, runtime)

@cli.command()
@click.option('--name', help='Name prefix for file')
@click.option('--target', help='bucket name')
def camera(name, target):
    cam = Camera()
    cam.setup()
    cam.get_picture(name=name, use_timestamp=True)
    cam.remote_save(delete_local=True, remote_target=target)

if __name__ == '__main__':
    cli()
