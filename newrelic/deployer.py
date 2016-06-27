


def setdeploy(revision,changelog,description,user):
    
    
    deployer={}
    deployer['revision'] = revision
    deployer['changelog'] = changelog
    deployer['description'] = description
    deployer['user'] = user
                
    deployment={}
    
    deployment['deployment'] = deployer
    
    return deployment

