import click
from lib.gameCrafterClient import operations as gameCrafterClient
from lib.pipelines import pipeline as pipelineClient
from lib.svgmanipulation import operations as svg

@click.group()
def main():
    """The Tyrus Pipeline CLI"""
    pass

@main.group()
def pipeline():
    """Utilize data entry to production pipelines"""
    pass

@pipeline.command()
def gameToGameCrafter():
    """ImageMagick to Game Crafter"""
    pass

@main.group()
def gamecrafter():
    """Manage game crafter assets"""
    pass

@gamecrafter.group()
def games():
    """Manage games"""
    pass

@games.command()
def ls():
    """List all games"""
    gameCrafterClient.getGames()

@main.group()
def gameManager():
    """Manage game defines"""
    pass

@gameManager.command()
@click.option()
def produce():
    """Produce a game based on a directory"""
    pass

@svgmanip.command()
def createDemoCard():
    """Create a demo card"""
    demoCard = svg.createDemoCard()

def start():
    main(obj={})

if __name__ == '__main__':
    start()