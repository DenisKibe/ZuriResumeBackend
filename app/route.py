from app.api.views import GetDataAndSave

def initialize_routes(api):
    api.add_resource(GetDataAndSave,'/api/ppdata')