from django.http import JsonResponse, HttpResponse
import json
import yaml
import django
from . import loader
from django.shortcuts import render
from yaml.scanner import ScannerError


def get_documentation(request, raml_folder):
    try:
        j = json.loads(__fetch_documentation(request, raml_folder))
        context = {
            'title': j["title"],
            'sections': j["sections"]
        }
        return render(request, 'raml_parser/index.html', context)
    except ScannerError as ex:
        return HttpResponse(status=400, content=ex.problem, content_type="application/json")
    except FileNotFoundError as ex:
        print(ex)
        return HttpResponse(status=204)
    except NotADirectoryError:
        return HttpResponse(status=204)


def __fetch_documentation(request, raml_folder):
    with open("raml/%s/application.raml" % raml_folder, 'r') as stream:
        try:
            y = yaml.load(stream, loader.Loader)
            j = json.dumps(y)
            return j
        except ScannerError:
            message = {"code": "PARSER_ERROR",
                       "message": "Unable to parse %s" % raml_folder}
            raise ScannerError(problem=json.dumps(message))
