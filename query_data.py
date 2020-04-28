import requests
import json

print("hello")

country_list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Botswana", "Brazil", "Bulgaria", "Burma", "Burundi", "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China", "Colombia", "Congo", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Ecuador", "Egypt", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Greenland", "Guatemala", "Guinea", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palestine", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Rwanda", "Samoa", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia", "Slovenia", "Somalia", "Spain", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Yemen", "Zambia", "Zimbabwe"]

body = '{"operationName": "getCo2ImportsExportsDimension","variables": {"groupNames": ["Canada"],"groupName": "Canada","emissionsUnit": "MtCO2eq","types": ["CO2 Imports","CO2 Exports"],"total": false,"bySector": false,"byCountry": true,"byContinent": false},"query": "query getCo2ImportsExportsDimension($groupNames: [String]!, $groupName: String, $emissionsUnit: CO2eqUnit!, $total: Boolean!, $byCountry: Boolean!, $byContinent: Boolean!, $bySector: Boolean!, $types: [String]!) {  co2ImportsExports {\\n    multiSelects {\\n      name\\n      data {\\n        name\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    total(groupNames: $groupNames, emissionsUnit: $emissionsUnit, types: $types) @include(if: $total) {\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        __typename\\n      }\\n      multiSelects {\\n        name\\n        data {\\n          name\\n          color\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    byCountry(groupName: $groupName, types: $types, numberOfCountries: 8) @include(if: $byCountry) {\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    byContinent(groupName: $groupName, types: $types) @include(if: $byContinent) {\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    bySector(groupName: $groupName, types: $types, numberOfSectors: 6) @include(if: $bySector) {\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'

body_json = json.loads(body)


url = "https://api.theshiftdataportal.org/"

result = {}

for country in country_list:
    body_json["variables"]["groupNames"] = [country]
    body_json["variables"]["groupName"] = country

    r = requests.post(url, data=json.dumps(body_json))

    result[country] = json.loads(r.text)['data']['co2ImportsExports']['byCountry']


with open('shiftdata/importExportAllCountries.json', 'w') as fp:
    json.dump(result, fp)


result
