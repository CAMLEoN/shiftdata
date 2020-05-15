import requests
import json

print("hello")

# country_list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Botswana", "Brazil", "Bulgaria", "Burma", "Burundi", "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China", "Colombia", "Congo", "Croatia", "Cuba", "Cyprus", "Czechia", "Denmark", "Djibouti", "Ecuador", "Egypt", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Greenland", "Guatemala", "Guinea", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palestine", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Rwanda", "Samoa", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia", "Slovenia", "Somalia", "Spain", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Yemen", "Zambia", "Zimbabwe"]

country_list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "British Virgin Islands", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burma", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Faeroe Islands", "Fiji", "Finland", "France", "French Polynesia", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Greenland", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Moldova", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russian Federation \u0026 USSR", "Rwanda", "Samoa", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Viet Nam", "Zambia", "Zimbabwe"]

body_import_export = '{"operationName": "getCo2ImportsExportsDimension","variables": {"groupNames": ["Canada"],"groupName": "Canada","emissionsUnit": "MtCO2eq","types": ["CO2 Imports","CO2 Exports"],"total": false,"bySector": false,"byCountry": true,"byContinent": false},"query": "query getCo2ImportsExportsDimension($groupNames: [String]!, $groupName: String, $emissionsUnit: CO2eqUnit!, $total: Boolean!, $byCountry: Boolean!, $byContinent: Boolean!, $bySector: Boolean!, $types: [String]!) {  co2ImportsExports {\\n    multiSelects {\\n      name\\n      data {\\n        name\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    total(groupNames: $groupNames, emissionsUnit: $emissionsUnit, types: $types) @include(if: $total) {\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        __typename\\n      }\\n      multiSelects {\\n        name\\n        data {\\n          name\\n          color\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    byCountry(groupName: $groupName, types: $types, numberOfCountries: 8) @include(if: $byCountry) {\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    byContinent(groupName: $groupName, types: $types) @include(if: $byContinent) {\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    bySector(groupName: $groupName, types: $types, numberOfSectors: 6) @include(if: $bySector) {\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'

body_footprint = '{"operationName": "getFootprintDimension", "variables": {"groupNames":["Afghanistan"],"emissionsUnit":"MtCO2","perGDP":false,"dimension":"total","gdpUnit":"GDP (constant 2010 US$)","total":true,"perCapita":false,"scopes":["Carbon Footprint","Territorial Emissions"],"yearStart":0,"yearEnd":3000},"query":"query getFootprintDimension($gdpUnit: String!, $groupNames: [String]!, $emissionsUnit: CO2Unit!, $total: Boolean!, $perCapita: Boolean!, $yearStart: Int!, $perGDP: Boolean!, $yearEnd: Int!, $dimension: FootprintDimensions!, $scopes: [String]!) {\\n  footprint {\\n    multiSelects(dimension: $dimension) {\\n      name\\n      data {\\n        name\\n        color\\n        __typename\\n      }\\n      __typename\\n    }\\n    total(groupNames: $groupNames, emissionsUnit: $emissionsUnit, yearStart: $yearStart, yearEnd: $yearEnd, scopes: $scopes) @include(if: $total) {\\n      multiSelects {\\n        name\\n        data {\\n          name\\n          color\\n          __typename\\n        }\\n        __typename\\n      }\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        dashStyle\\n        __typename\\n      }\\n      __typename\\n    }\\n    perGDP(gdpUnit: $gdpUnit, groupNames: $groupNames, emissionsUnit: $emissionsUnit, yearStart: $yearStart, yearEnd: $yearEnd, scopes: $scopes) @include(if: $perGDP) {\\n      multiSelects {\\n        name\\n        data {\\n          name\\n          color\\n          __typename\\n        }\\n        __typename\\n      }\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        dashStyle\\n        __typename\\n      }\\n      __typename\\n    }\\n    perCapita(groupNames: $groupNames, emissionsUnit: $emissionsUnit, yearStart: $yearStart, yearEnd: $yearEnd, scopes: $scopes) @include(if: $perCapita) {\\n      multiSelects {\\n        name\\n        data {\\n          name\\n          color\\n          __typename\\n        }\\n        __typename\\n      }\\n      categories\\n      series {\\n        name\\n        data\\n        color\\n        dashStyle\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'

body = body_import_export
body = body_footprint

body_json = json.loads(body)


url = "https://api.theshiftdataportal.org/"

result = {}

# CO2 import export
for country in country_list:
    body_json["variables"]["groupNames"] = [country]
    body_json["variables"]["groupName"] = country

    r = requests.post(url, data=json.dumps(body_json))

    result[country] = json.loads(r.text)['data']['co2ImportsExports']['byCountry']

with open('importExportAllCountries_v2.json', 'w') as fp:
    json.dump(result, fp)



# footprint and territorial emissions over time
for country in country_list:
    body_json["variables"]["groupNames"] = [country]

    r = requests.post(url, data=json.dumps(body_json))

    result[country] = json.loads(r.text)['data']['footprint']['total']

with open('footprintAllCountries_v2.json', 'w') as fp:
    json.dump(result, fp)



result
