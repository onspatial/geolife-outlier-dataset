import utils.Files as Files

# four categories
APARTMENT_PAIRS = Files.readPairs('data/category/FourCategory/Apartment.txt')
WORKPLACE_PAIRS = Files.readPairs('data/category/FourCategory/Workplace.txt')
RESTAURANT_PAIRS = Files.readPairs('data/category/FourCategory/Restaurant.txt')
PUB_PAIRS = Files.readPairs('data/category/FourCategory/Pub.txt')

# 10 categories
ACCOMMODATION_PAIRS = Files.readPairs(
    'data/category/TenCategory/Accommodation.txt')
EDUCATION_PAIRS = Files.readPairs('data/category/TenCategory/Education.txt')
ENTERTAINMENT_PAIRS = Files.readPairs(
    'data/category/TenCategory/Entertainment.txt')
FOOD_PAIRS = Files.readPairs('data/category/TenCategory/Food.txt')
GOVERNMENT_PAIRS = Files.readPairs('data/category/TenCategory/Government.txt')
HEALTH_PAIRS = Files.readPairs('data/category/TenCategory/Health.txt')
PROFESSIONAL_SERVICES_PAIRS = Files.readPairs(
    'data/category/TenCategory/ProfessionalServices.txt')
RECREATION_PAIRS = Files.readPairs('data/category/TenCategory/Recreation.txt')
RETAIL_PAIRS = Files.readPairs('data/category/TenCategory/Retail.txt')
TRANSPORTATION_PAIRS = Files.readPairs(
    'data/category/TenCategory/Transportation.txt')
