import requests
import json

from .global_functions import *


OMIE_URL = "https://app.omie.com.br/api/v1/"


class OmieConnection:
    def __init__(self, app_key, app_secret):
        trace(f"Instance OmieConnection: {app_key= }, {app_secret= }")
        self.app_key = app_key
        self.app_secret = app_secret

    def do_requests(self, path, call, content=None):
        _data = {
            "call": call,
            "app_key": self.app_key,
            "app_secret": self.app_secret,
            "param": [content]
        }
        headers = {
            'Content-type': 'application/json'
        }

        trace(f"do_requests: {path=}, params={_data}")
        r = requests.post(OMIE_URL + path, headers=headers, json=_data)
        if r.status_code == 200:
            try:
                return r.json()
            except Exception as erro:
                return {
                    'Error': 'JSON Decode Error',
                    'Message': f'{erro}'
                }
    
    def listar_clientes(self):
        trace(f"Omie..listar_clientes")
        try:
            path = "geral/clientes/"
            call = "ListarClientesResumido"

            result_list = []
            _params = {
                "pagina": 1,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N"
            }
            ret = self.do_requests(path, call, _params)
            
            pag_total = ret["total_de_paginas"]
            result_list += ret["clientes_cadastro_resumido"]

            for page in range(2, pag_total + 1):
                try:
                    _params["pagina"] = page
                    ret = self.do_requests(path, call, _params)
                    result_list += ret["clientes_cadastro_resumido"]
                
                except Exception as ex:
                    report_exception(ex)

            trace(f'Omie..listar_clientes: Returning {len(result_list)} client')
            return result_list
        
        except Exception as ex:
            report_exception(ex)
            return []
        
    def listar_ordem_servicos(self):
        trace(f"Omie..listar_ordem_servicos")
        try:
            path = "servicos/os/"
            call = "ListarOS"

            result_list = []
            _params = {
                "pagina": 1,
                "registros_por_pagina": 60,
                "apenas_importado_api": "N"
            }
            
            ret = self.do_requests(path, call, _params)
            pag_total = ret["total_de_paginas"]
            result_list += ret["osCadastro"]

            for page in range(2, pag_total + 1):
                try:
                    _params["pagina"] = page
                    ret = self.do_requests(path, call, _params)
                    result_list += ret["osCadastro"]
                
                except Exception as ex:
                    report_exception(ex)

        except Exception as ex:
            report_exception(ex)
        
        return result_list

    def listar_projetos(self):
        trace("Omie..listar_projetos")
        try:
            path = "geral/projetos/"
            call = "ListarProjetos"

            result_list = []
            _params = {
                "pagina": 1,
                "registros_por_pagina": 50,
                "apenas_importado_api": "N"
            }
            
            ret = self.do_requests(path, call, _params)
            pag_total = ret["total_de_paginas"]
            result_list += ret["cadastro"]

            for page in range(2, pag_total + 1):
                try:
                    _params["pagina"] = page
                    ret = self.do_requests(path, call, _params)
                    result_list += ret["cadastro"]
                except Exception as ex:
                    report_exception(ex)

        except Exception as ex:
            report_exception(ex)
        
        return result_list
