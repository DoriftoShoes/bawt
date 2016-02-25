import click

from bawt.subsystems.camera import Camera
from bawt.subsystems.device import Device
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

@cli.command()
def hvac():
    pass

@cli.command()
def sensor():
    pass

@cli.command()
def weather():
    pass

@cli.command()
def file():
    pass

@cli.command()
@click.argument('action')
@click.argument('device')
def device(action, device):
    device = Device()
    if action == 'on':
        device.on(device)
    elif action == 'off':
        device.off(device)
    elif action == 'toggle':
        device.toggle(device)
    elif action == 'moment':
        device.moment(device)

if __name__ == '__main__':
    cli()
