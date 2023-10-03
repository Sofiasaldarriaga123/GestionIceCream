# main:

##########################################

import uvicorn

##########################################

def webapi_gestionuber():
	uvicorn.run(
				"application.WebAPIGestionUber:app",
				host="127.0.0.1",
				port=8060,
				reload=True
			)

##########################################

if __name__ == '_main_':
	webapi_gestionuber()

##########################################