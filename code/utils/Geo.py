import utils.Files as Files
import utils.CategoryType as CategoryType
import config.API as apiConfig


def getOsmDataFromMongo(Latitude, Longitude, database='OSM', collection='GeoData'):
    import config.Sensitive as Sensitive
    from utils.Mongo import getByCoordinate
    try:
        data = getByCoordinate(Sensitive.MONGO_URI, database,
                               collection, Latitude, Longitude)
        if data:
            return data['GeoJSON']
        else:
            return None
    except Exception as e:
        print('getOsmDataFromMongo: ', e)


def getOsmDataFromAPI(latitude, longitude):
    from json import loads as loadJson
    from requests import get as getRequest
    from time import sleep
    data = None
    apiUrl = f"https://nominatim.openstreetmap.org/reverse?format=geojson&extratags=1&lat={latitude}&lon={longitude}"
    try:
        for i in range(10):
            response = getRequest(apiUrl)
            if response.status_code == 200:
                break
            else:
                print('getOsmDataFromAPI: ', response.status_code)
                sleep(2*i)

        data = loadJson(response.text)
        return data
    except Exception as e:
        print('getOsmDataFromAPI: ', e)
        print('apiUrl: ', apiUrl)
        if response:
            print('response: ', response.text)
        if data:
            print('data: ', data)
        return None


def getGoogleMapsData(latitude, longitude):
    from json import loads as loadJson
    from requests import get as getRequest
    data = None
    apiUrl = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=150&key={apiConfig.GOOGLE_PLACES_KEY}"
    try:
        response = getRequest(apiUrl)
        data = loadJson(response.text)
        return data
    except Exception as e:
        print('getGoogleMapsData: ', e)
        print('apiUrl: ', apiUrl)
        if response:
            print('response: ', response.text)
        if data:
            print('data: ', data)
        return None


def getLocationType(latitude, longitude):
    defaultLocationType = 'Apartment'
    try:
        geoJSON = getGeoJSON(latitude, longitude)
        if not geoJSON:
            print('getLocationType: ', 'geoJSON is None')
            return defaultLocationType
        locationType = getFourLocationTypeFromGeoJSON(geoJSON)
        return locationType
    except Exception as e:
        print('getLocationType: ', e)
        return defaultLocationType


def getTenCategoryLocationType(latitude, longitude):
    defaultLocationType = 'Apartment'
    try:
        geoJSON = getGeoJSON(latitude, longitude)
        if not geoJSON:
            print('getTenCategoryLocationType: ', 'geoJSON is None')
            return defaultLocationType
        detailedLocationType = getTenLocationTypeFromGeoJSON(geoJSON)
        return detailedLocationType
    except Exception as e:
        print('getTenCategoryLocationType: ', e)
        return defaultLocationType


def getGeoJSON(latitude, longitude):
    from utils.Mongo import saveOne
    import config.Sensitive as Sensitive
    from config.Parameters import DATABASE, COLLECTION
    try:
        geoJSON = getOsmDataFromMongo(
            latitude, longitude, DATABASE, COLLECTION)
        if not geoJSON:
            geoJSON = getOsmDataFromAPI(latitude, longitude)
            if geoJSON:
                saveOne(Sensitive.MONGO_URI, DATABASE, COLLECTION, {
                    'Latitude': latitude, 'Longitude': longitude, 'GeoJSON': geoJSON})
        return geoJSON
    except Exception as e:
        print('getGeoJSON: ', e)
        return None


def getFourLocationTypeFromGeoJSON(geoJSON):
    defaultLocationType = 'Apartment'
    category_, type_ = getCategoryTypeTuple(geoJSON)
    Files.saveToFile(f'{category_}, {type_}\n', 'category_type')
    if isWorkplace(category_, type_):
        locationType = 'Workplace'
    elif isApartment(category_, type_):
        locationType = 'Apartment'
    elif isPub(category_, type_):
        locationType = 'Pub'
    elif isRestaurant(category_, type_):
        locationType = 'Restaurant'
    else:
        locationType = defaultLocationType
    return locationType


def getOSMCategoryTypeFromGeoJSON(geoJSON):
    category_, type_ = getCategoryTypeTuple(geoJSON)
    Files.saveToFile(f'{category_}, {type_}\n', 'category_type')
    return f'{category_}, {type_}'


def getTenLocationTypeFromGeoJSON(geoJSON):
    defaultLocationType = 'Pub'
    category_, type_ = getCategoryTypeTuple(geoJSON)
    Files.saveToFile(f'{category_}, {type_}\n', 'category_type')

    if isAccommodation(category_, type_):
        locationType = 'Accommodation'
    elif isEducation(category_, type_):
        locationType = 'Education'
    elif isEntertainment(category_, type_):
        locationType = 'Entertainment'
    elif isFood(category_, type_):
        locationType = 'Food'
    elif isGovernment(category_, type_):
        locationType = 'Government'
    elif isHealth(category_, type_):
        locationType = 'Health'
    elif isProfessionalServices(category_, type_):
        locationType = 'ProfessionalServices'
    elif isRecreation(category_, type_):
        locationType = 'Recreation'
    elif isRetail(category_, type_):
        locationType = 'Retail'
    elif isTransportation(category_, type_):
        locationType = 'Transportation'
    else:
        locationType = defaultLocationType
    return locationType


def getCategoryTypeTuple(geoJSON):
    try:
        category_, type_ = geoJSON['features'][0]['properties']['category'], geoJSON['features'][0]['properties']['type']
        Files.saveToFile(f'{category_}, {type_}\n', 'category_type')
        return category_, type_
    except (KeyError, IndexError, TypeError):
        print('getCategoryTypeTuple: ', 'error in getting category and type')
        return None, None


def isAccommodation(category_, type_):
    return (category_, type_) in CategoryType.ACCOMMODATION_PAIRS


def isEducation(category_, type_):
    return (category_, type_) in CategoryType.EDUCATION_PAIRS


def isEntertainment(category_, type_):
    return (category_, type_) in CategoryType.ENTERTAINMENT_PAIRS


def isFood(category_, type_):
    return (category_, type_) in CategoryType.FOOD_PAIRS


def isGovernment(category_, type_):
    return (category_, type_) in CategoryType.GOVERNMENT_PAIRS


def isHealth(category_, type_):
    return (category_, type_) in CategoryType.HEALTH_PAIRS


def isProfessionalServices(category_, type_):
    return (category_, type_) in CategoryType.PROFESSIONAL_SERVICES_PAIRS


def isRecreation(category_, type_):
    return (category_, type_) in CategoryType.RECREATION_PAIRS


def isRetail(category_, type_):
    return (category_, type_) in CategoryType.RETAIL_PAIRS


def isTransportation(category_, type_):
    return (category_, type_) in CategoryType.TRANSPORTATION_PAIRS


def isUncategorized(category_, type_):
    return (category_, type_) in CategoryType.UNCATEGORIZED_PAIRS


def isApartment(category_, type_):
    return (category_, type_) in CategoryType.APARTMENT_PAIRS


def isWorkplace(category_, type_):
    return (category_, type_) in CategoryType.WORKPLACE_PAIRS


def isRestaurant(category_, type_):
    return (category_, type_) in CategoryType.RESTAURANT_PAIRS


def isPub(category_, type_):
    return (category_, type_) in CategoryType.PUB_PAIRS


def getBoundingBox(dataset, boundingBox=(39.741936, 116.186732,  116.541860, 40.069034), longitudeColumnName='Longitude',  latitudeColumnName='Latitude'):
    import pandas as pd
    # TODO: There is a bug in this function. It is not returning the correct bounding box. Need to fix it.
    # The reason is that the order of data and boundingBox
    print("There is a BUG here. This function is not returning the correct bounding box. Need to fix it.")

    lowerLongitude, lowerLatitude, upperLongitude, upperLatitude = boundingBox

    try:
        df = pd.read_csv(dataset, sep='\s+')
        print(df.head())

        minimumLongitude = df[longitudeColumnName].clip(
            lower=lowerLongitude).min()
        minimumLatitude = df[latitudeColumnName].clip(
            lower=lowerLatitude).min()
        maximumLongitude = df[longitudeColumnName].clip(
            upper=upperLongitude).max()
        maximumLatitude = df[latitudeColumnName].clip(
            upper=upperLatitude).max()
        return minimumLongitude, minimumLatitude, maximumLongitude, maximumLatitude
    except Exception as e:
        print('getBoundingBox: ', e)
        print("Columns in dataset: ", df.columns)
        print("Data types in dataset: ", df.dtypes)
        return None, None, None, None
