import zeep

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

capital = zeep.Client(wsdl = url)

country_code = "BR"

result = capital.service.CapitalCity(
	sCountryISOCode = country_code
)

print(f"A capital do Brasil é {result}")

country_code = "US"

result = capital.service.CapitalCity(
	sCountryISOCode = country_code
)

print(f"A capital do Brasil é {result}")

url2 = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

conversion = zeep.Client(wsdl = url2)

number = "5478"

result2 = conversion.service.NumberToWords(
    ubiNum = number
)

print(f"O número {number} é escrito {result2}")