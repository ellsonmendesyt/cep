from pycep_correios import get_address_from_cep, WebService

endereco = get_address_from_cep('65636-766', webservice=WebService.APICEP)

print(endereco)
