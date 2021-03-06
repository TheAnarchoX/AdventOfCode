import click
import requests

@click.command()
@click.option('-y', '--year', prompt='Which year of AoC would you like to run?', type=click.IntRange(2015, 2019))
@click.option('-d', '--day', prompt='And which day?', type=click.IntRange(1,25))
def main(year, day):
    runAoC(f"year{year}.day{day}.solve", "solve")()

def runAoC(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

if __name__ == '__main__':
    main()