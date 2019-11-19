from django.http import JsonResponse, HttpResponse
import json
import yaml
from . import loader


def get_documentation(request, raml_name):
    try:
        with open("raml/%s" % raml_name, 'r') as stream:
            try:
                y = yaml.load(stream, loader.Loader)
                j = json.dumps(y)
                return HttpResponse(status=200, content=j)
            except yaml.scanner.ScannerError:
                message = {"code": "PARSER_ERROR",
                           "message": "Unable to parse %s" % raml_name}
                return HttpResponse(status=400, content=json.dumps(message))
            else:
                return HttpResponse(status=500)
    except FileNotFoundError:
        return HttpResponse(status=204)
