"""
          ::
            Usage:
                  object [--object=SERVICE] put --object=OBJECT
                  object [--object=SERVICE] put --key=KEY
                  object [--object=SERVICE] get --object=OBJECT
                  object [--object=SERVICE] get --key=KEY
                  object [--object=SERVICE] list --object=OBJECT
                  object [--object=SERVICE] list --key=KEY
                  object [--object=SERVICE] delete BUCKET | KEY              
                  object [--object=SERVICE] createObjectOrKey BUCKET | KEY
                  object [--object=SERVICE] uploadObjectOrKey BUCKET | KEY 
                  object [--object=SERVICE] createfile BUCKET | KEY 

                  KEY [--KEY=API_KEY] SET API_KEY  #API key or username to be used (required)
                  SECRET [--SECRET=SECRET] SET SECRET #Secret password to be used (required)
                  SECURE [--SECURE=SECURE] SET SECURE #Whether to use HTTPS or HTTP. Note: Some providers only support HTTPS, and it is on by default.
                  HOST [--HOST=HOST] SET HOST #Override hostname used for connections
                  PORT [--PORT=PORT] SET PORT #Override port used for connections.
                  OBJECT_VERSION [--OBJECT_VERSION=OBJECT_VERSION] SET OBJECT_VERSION #Optional API version. Only used by drivers which support multiple API versions.
                  REGION [--REGION=REGION] SET REGION # Optional driver region. Only used by drivers which support multiple regions.      

            Parameters:
                BUCKET  NAME OF THE FOLDER or DIRECTORY in CLOUD STORAGE
                KEY FOLDER NAME WITH IN CLOUD STORAGE or BUCKET
                                
          
            Example:
              SET OBJECT=s3
              OBEJECT PUT BUCKET | KEY
              
              object put o.nn
              object put k.nn
              object put key NAME
              
   """
