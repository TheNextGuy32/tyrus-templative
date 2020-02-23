from client import createArtFileOfPiece

def createArtFilesForComponent(game, component, frontMetaData, backMetaData, componentGamedata, outputDirectory):
    if game == None:
        print("game cannot be None.")
        return
    
    if component == None:
        print("component cannot be None.")
        return

    if frontMetaData == None:
        print("artMetaData cannot be None.")
        return

    if componentGamedata == None:
        print("componentGamedata cannot be None.")
        return

    if outputDirectory == None: 
        print("outputDirectory cannot be None.")
        return
    
    for pieceGamedata in componentGamedata:
        createArtFileOfPiece(game, component, pieceGamedata, frontMetaData, outputDirectory)
    
    createArtFileOfPiece(game, component, {"name":"Back"}, backMetaData, outputDirectory)

def getInstructionSetsForFiles(game, component, componentGamedata, componentFilepath):
    if game == None:
        print("game cannot be None.")
        return
    
    if component == None:
        print("component cannot be None.")
        return

    if componentGamedata == None:
        print("componentGamedata cannot be None.")
        return

    instructionSets = []
    for pieceGamedata in componentGamedata:
        artFilepath = ("%s/%s-%s.jpg" % (componentFilepath, component["name"], pieceGamedata["name"])).replace(" ","")
        instructionSets.append({"name": pieceGamedata["name"], "filepath": artFilepath, "quantity": pieceGamedata["quantity"]})

    return instructionSets