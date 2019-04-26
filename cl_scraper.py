from craigslist import CraigslistHousing
import settings

cl = CraigslistHousing

cl = CraigslistHousing(site='seattle', area='see', category='apa',
results = cl.get_results(sort_by='newest', geotagged=True, limit=25))
for result in results:
    print(result)
