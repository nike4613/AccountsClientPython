from .profiles import *
import json

def findByName(name):
	return find_profile_by_name(name)
	
def findByUUID(uuid):
	return (find_profile_by_uuid(uuid))
	
def getDataByName(name):
	return findByUUID(findByName(name)['id'])
