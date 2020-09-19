from WBT.whitebox_tools import WhiteboxTools
import click

wbt = WhiteboxTools()
wbt.wbt.set_working_dir("./")

@click.command()
@click.option('--sourcefile', prompt='LIDAR Poincloud LAS sourcefile relative path?')
def lidar2dem(sourcefile):
    export_file_name = (sourcefile).strip('.las') + '.tif'
    wbt.lidar_idw_interpolation(
    i=sourcefile,
    output=export_file_name,
    parameter="elevation",
    returns="last",
    resolution=1.5,
    weight=2.0,
    radius=2.5
    )

if __name__ == '__main__':
  lidar2dem()