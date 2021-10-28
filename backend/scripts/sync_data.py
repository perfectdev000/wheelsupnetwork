import json
import requests
import os
import magic
import ntpath
import mimetypes
from slugify import slugify


mime = magic.Magic(mime=True)

PATH_DATA = '/home/x0/scripts/wheelsup_wordpress.json'
PATH_FILES = '/home/x0/scripts/uploads'
PATH_DATA_FILEs = '/home/x0/scripts/soloagentes_mx_files.json'

SCHEMA = [{
    'entity': 'customers',
    'where': 'old_customer_id',
    'action': 'update',
    'fields': {
        'slug': 'slug',
    },
}]

ENTITY_MAP = {
    'promotions': 'promotions',
    # 'prizes': 'prizes',
    'partner-programs': 'partner-programs',
    'webinars': 'webinars',
    'eventos': 'events',
    'specials': 'specials',
    'industry': 'industries',
    'news': 'news-items',
    'evergreen': 'evergreens',
    'fams': 'fams',
    'contest': 'contests'
}

ENTITY_MODEL_MAP = {
    'promotions': 'promotions',
    # 'prizes': 'prizes',
    'partner-programs': 'partner-programs',
    'webinars': 'webinars',
    'eventos': 'events',
    'specials': 'specials',
    'industry': 'industry',
    'news': 'news-item',
    'evergreen': 'evergreen',
    'fams': 'fams',
    'contest': 'contests'
}

ENTITY_MODEL_MAP_INVERT = {
    'promotions':'promotions',
    # 'prizes': 'prizes',
    'partner-programs':'partner-programs',
    'webinars': 'webinars',
    'events': 'eventos',
    'specials': 'specials',
    'industries': 'industry',
    'news-items': 'news',
    'evergreen': 'evergreen',
    'fams': 'fams',
    'contests': 'contests'
}

ENTITY_MODEL_MAP2 = {
    #'promotions': 'promotions',
    #'prizes': 'prizes',
    #'partner-programs': 'partner-programs',
    #'webinars': 'webinars',
    #'events': 'events',
    'specials': 'specials',
    #'industries': 'industry',
    #'news-items': 'news-item',
}

ENTITIES_FIX_SITE_FIELD = [
  'promotions',
  'prizes',
  'partner-programs',
  'webinars',
  'events',
  'specials',
  'industries',
  'news-items',
]




def is_url_image(url):
    mimetype, encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

def is_name_image(name):
  for ext in ['png', 'jpeg','jpg']:
    if ext in name.lower(): return True
  return False

def get_articles_entity(entity, file_json):
  records = []
  articles = file_json['articles']
  for x in articles:
    if entity == x['category']:
      records.append(x)
  return records
class Strapi():
    def __init__(self):
        self._baseurl = 'http://localhost:1337'
        self._token = None

    def _make_headers(self, file=False):
        h = {'Content-type': 'application/json'}
        if file:
            h = {}

        if self._token != None:
            h['Authorization'] = 'Bearer {}'.format(self._token)

        return h

    def _make_request(self,
                      method,
                      resource,
                      data=None,
                      dd=None,
                      params={},
                      files=None):
        isUpload = True if files != None else False
        headers = self._make_headers(file=isUpload)
        url = self._baseurl + resource
        r = requests.request(method=method,
                             url=url,
                             headers=headers,
                             json=data,
                             data=dd,
                             params=params,
                             files=files)
        if r.status_code == 500 or r.status_code == 400:
          raise Exception(r.text)
        return r.json()

    def login(self):
        email = input('Email: ')
        passwod = input('Password: ')

        data = self._make_request('post',
                                  '/admin/login',
                                  data={
                                      'email': email,
                                      'password': passwod
                                  })

        if 'statusCode' in data:
            raise Exception(data)

        self._token = data['data']['token']

    def get(self, resource, params={}):
        return self._make_request('get', resource, params=params)

    def post(self, resource, data=None, dd=None, files=None):
        return self._make_request('post',
                                  resource,
                                  data=data,
                                  dd=dd,
                                  files=files)

    def put(self, resource, data={}):
        return self._make_request('put', resource, data=data)

    def delete(self, resource):
        return self._make_request("delete", resource)

    """
    relation = {
          'refId': 325,
          'ref': 'article',
          'field': 'files'
        }
    """

    def upload(self, path_file, relation):
        files = {
            'files':
            (ntpath.basename(path_file), open(path_file,
                                              'rb'), mime.from_file(path_file))
        }
        return self.post('/upload', files=files, dd=relation)

    def process_schema(self, schema, data_file_json):
        for item in schema:
            entity = item['entity']
            action = item['action']
            fields = item['fields']
            url = '/{}'.format(entity)

            if entity in data_file_json:
                records = data_file_json[entity]

                for record in records:
                    if 'where' in item:
                        where_field = item['where']
                        q = {where_field: record[where_field]}
                        results = self.get(url, params=q)

                        if len(results) > 0:
                            id = results[0]['id']

                            if action == 'update':
                                d = {}

                                for key_db, key_json in fields.items():
                                    d[key_db] = record[key_json]

                                res_action = self.put(f'{url}/{id}', data=d)

                                if 'statusCode' in res_action:
                                    print('Error update record: {}'.format(id))
                                else:
                                    print('Record updated: ID: {}'.format(id))

    def sync_entity(self, entity, slug_site, data_file_json):
        site = self.get('/sites', params={'uid': slug_site})
        if entity == 'articles':
            url = '/articles'
            articles_data = data_file_json['articles']

            for record in articles_data:
                slug = record['slug']

                results = self.get(url, params={'slug': slug})
                new_article = {
                    "old_post_id": record['old_post_id'],
                    "title": record['title'],
                    "content": record['content'],
                    "publishedDate": record['publishedDate'],
                    "expiration_date": record['expiration_date'],
                    "status": record['status'],
                    "slug": record['slug'],
                    "author": {
                        "id": 1
                    },
                    "description": record['description'],
                    #"featured_image": {},
                    #"slider_images": [],
                    #"files": {
                    #  "2016/03/Mix-330x225.jpg": "http://www.soloparaagentes.mx/wp-content/uploads/2016/03/Mix-330x225.jpg"
                    #},
                    "link": record['link'],
                }

                if len(site) > 0:
                    new_article['sites'] = [{'id': site[0]['id']}]

                category = self.get('/categories',
                                    params={'slug': record['category']})

                if len(category) > 0:
                    new_article['category'] = [{'id': category[0]['id']}]

                customer = self.get(
                    '/customers',
                    params={'old_customer_id': record['customer']})
                if len(customer) > 0:
                    new_article['customer'] = [{'id': customer[0]['id']}]

                self.post(url, data=new_article)
                print("Article created")

        if entity == 'jobs':
            url = '/jobs'
            jobs_data = data_file_json['jobs']

            for record in jobs_data:
                # record['sites'] = [{'id': site[0]['id']}]
                record['sites'] = [{'id': 1}, {'id': 7}] # usa and canada
                self.post(url, data=record)
                print("Jobs created")

        if entity == 'destinations':
          url = '/destinations'
          destinations_data = data_file_json['destinations']

          for record in destinations_data:
            new_record = record.copy()
            # new_record['sites'] = [{'id': site[0]['id']}]
            new_record['sites'] = [{'id': 1}, {'id': 7}] # usa and canada

            if record['slug'] in ['jamaica', 'las-vegas', 'st-kitts', 'cuba']: continue

            del new_record['logo']
            del new_record['files']
            # del new_record['gallery']

            nd = self.post(url, data=new_record)

            if 'logo' in record and record['logo'] != None:
              for key, value in record['logo'].items():
                path = os.path.join(PATH_FILES, key)

                rs = {
                  'refId': nd['id'],
                  'ref': 'destination',
                  'field': 'logo'
                }
                self.upload(path, rs)

            if 'files' in record and record['files'] != None:
              for key, value in record['files'].items():
                if not is_url_image(value):
                  path = os.path.join(PATH_FILES, key)

                  rs = {
                    'refId': nd['id'],
                    'ref': 'destination',
                    'field': 'files'
                  }
                  self.upload(path, rs)
                else:
                  path = os.path.join(PATH_FILES, key)

                  rs = {
                    'refId': nd['id'],
                    'ref': 'destination',
                    'field': 'gallery'
                  }
                  self.upload(path, rs)

            # if 'gallery' in record and record['gallery'] != None:
            #   for key, value in record['gallery'].items():
            #     path = os.path.join(PATH_FILES, key)

            #     rs = {
            #       'refId': nd['id'],
            #       'ref': 'destination',
            #       'field': 'gallery'
            #     }
            #     self.upload(path, rs)
            print("Destination created")

        if entity == 'customers':
          url = '/customers'
          customers_data = data_file_json['customers']

          for record in customers_data:
            new_record = record.copy()
            # new_record['sites'] = [{'id': site[0]['id']}]
            new_record['sites'] = [{'id': 1}, {'id': 7}] # usa and canada

            del new_record['logo']
            del new_record['files']

            nd = self.post(url, data=new_record)

            if 'logo' in record and record['logo'] != None:
              for key, value in record['logo'].items():
                path = os.path.join(PATH_FILES, key)

                rs = {
                  'refId': nd['id'],
                  'ref': 'customer',
                  'field': 'logo'
                }
                self.upload(path, rs)

            if 'files' in record and record['files'] != None:
              for key, value in record['files'].items():
                if not is_url_image(value):
                  path = os.path.join(PATH_FILES, key)

                  rs = {
                    'refId': nd['id'],
                    'ref': 'customer',
                    'field': 'files'
                  }
                  self.upload(path, rs)

            print(f"Customer created {nd['id']} - {slug_site}")

    def sync_articles(self, data_file_json):
        articles = data_file_json['articles']

        for article in articles:
          if article['category'] == 'atwm_prize':
            new_record = {
                "old_post_id": article['old_post_id'],
                "title": article['title'],
                "content": article['content'],
                "publishedDate": article['publishedDate'],
                "expiration_date": article['expiration_date'],
                "status": article['status'],
                "slug": article['slug'],
                "author": {
                    "id": 1
                },
                "description": article['description'],
                "link": article['link'],
            }

            new_record['sites'] = [{'id': 2}]


            # url_entity = ENTITY_MAP.get(article['category'], None)
            url_entity = 'contests'

            if url_entity != None:

              exists = self.get(f'/{url_entity}', params={'old_post_id': article['old_post_id']})

              if len(exists) > 0:
                continue

              if article['customer'] != "" and article['customer'] != None and article['customer'] != "null":
                customer = self.get('/customers', params={'_old_customer_id': article['customer'], 'sites.id': id_site_tmp})

                if len(customer) != 0:
                  new_record['customer'] = {
                    'id': customer[0]['id']
                  }

              res = self.post(f'/{url_entity}', data=new_record)

              if 'featured_image' in article:
                for key, value in article['featured_image'].items():
                  path = os.path.join(PATH_FILES, key)

                  rs = {
                    'refId': res['id'],
                    'ref': ENTITY_MODEL_MAP.get('contest', None),
                    'field': 'featured_image'
                  }
                  self.upload(path, rs)

              if 'files' in article:
                for key, value in article['files'].items():
                  if not is_url_image(value):
                    path = os.path.join(PATH_FILES, key)

                    rs = {
                      'refId': res['id'],
                      'ref': ENTITY_MODEL_MAP.get('contest', None),
                      'field': 'files'
                    }
                    self.upload(path, rs)

              print(f"New record {url_entity}")

    def sync_existing_articles(self, slug_site):
        site = self.get('/sites', params={'uid': slug_site})

        articles = self.get('/articles?_limit=-1')
        count_update = 0
        count_create = 0

        for article in articles:
            new_record = {
                "old_post_id": article['old_post_id'],
                "title": article['title'],
                "content": article['content'],
                "publishedDate": article['publishedDate'],
                "expiration_date": article['expiration_date'],
                "status": article['status'],
                "slug": article['slug'],
                "author": {
                    "id": 1
                },
                "sites": [{
                    "id": site[0]['id']
                }],
                "description": article['description'],
                "link": article['link'],
                "customer": article['customer']['id'] if article['customer'] != None else None,
            }

            url_entity = ENTITY_MAP.get(article['category']['slug'], None)

            if url_entity != None:

              exists = self.get(f'/{url_entity}',params={'slug': article['slug'], 'sites.uid': slug_site })

              if len(exists) > 0:
                res = self.put(f'/{url_entity}/{exists[0]["id"]}', data=new_record)
                count_update += 1
              else:
                if 'featured_image' in article and article['featured_image'] != None:
                  new_record['featured_image'] = {
                    'id': article['featured_image']['id']
                  }

                if 'files' in article and article['files'] != None:
                  new_record['files'] = []

                  for item in article['files']:
                    new_record['files'].append({
                      'id': item['id']
                    })

                if 'slider_images' in article and article['slider_images'] != None:
                  new_record['slider_images'] = []

                  for item in article['slider_images']:
                    new_record['slider_images'].append({
                      'id': item['id']
                    })

                res = self.post(f'/{url_entity}', data=new_record)
                count_create += 1

              print(f"Old article {article['id']} -> New record {url_entity}")

        print(f"updated: {count_update}, created: {count_create}")

    def fix_images(self, entity, entity_model, data):
      url = f'/{entity}'
      articles = data['articles']
      customers = data['customers']
      records = self.get(url, params={'_where[_or][0][sites.uid]': 'wheels-up-network-usa', '_where[_or][1][sites.uid]': 'wheels-up-network-canada', '_limit': '-1'})

      print(f"Fixing {len(records)} records")

      files_not_found = []

      for record in records:
        for article in articles:
          if record['old_post_id'] == article['old_post_id']:
            self.put(f'{url}/{record["id"]}', data={'slug': article['slug']})

            fi = article.get('featured_image', {})
            ff = article.get('files', {})

            count_fi = 0
            count_ff = 0

            if len(fi.items()) > 0 and record['featured_image'] == None:
              for k, v in fi.items():
                path = os.path.join(PATH_FILES, k)

                if os.path.exists(path) == False:
                  files_not_found.append(path)
                  continue

                rs = {
                  'refId': record['id'],
                  'ref': entity_model,
                  'field': 'featured_image'
                }
                self.upload(path, rs)
                count_fi += 1

            if len(ff.items()) > 0:
              for k, v in ff.items():
                if not is_url_image(v):
                  path = os.path.join(PATH_FILES, k)
                  if os.path.exists(path) == False:
                    files_not_found.append(path)
                    continue
                  rs = {
                    'refId': record['id'],
                    'ref': entity_model,
                    'field': 'files'
                  }
                  self.upload(path, rs)
                  count_ff += 1

            # if count_fi > 0:
            #   # remove old featured image
            #   if record.get('featured_image', None) != None:
            #     self.delete(f'/upload/files/{record["featured_image"]["id"]}')

            if count_ff > 0:
              # remove all files
              for rf in record['files']:
                self.delete(f'/upload/files/{rf["id"]}')

            print(f'Fix files {entity} record {record["id"]}')

      with open(f"files_not_found.json", 'w') as json_file:
        json.dump(files_not_found, json_file, indent=2)

    def fix_relation_site(self, entity):
      records = self.get(f'/{entity}', params={'_limit': '-1'})

      for record in records:
        id = record['id']
        d = {}
        d['sites'] = [{'id': record['site']['id']}]
        self.put(f'/{entity}/{id}', data=d)

    def fix_slug_customer(self):
      records = self.get(f'/customers', params={'_limit': '-1'})

      for record in records:
        self.put(f'/customers/{record["id"]}', data={'slug': slugify(record['name'])})

    def fix_customer_files(self, slug_site, data_file_json):
        site = self.get('/sites', params={'uid': slug_site})

        url = '/customers'
        customers_data = data_file_json['customers']

        for record in customers_data:

          results = self.get(url, params={'_sites.uid': slug_site, '_slug': record['slug']})

          if len(results) == 0:
            continue

          nd = results[0]

          if 'logo' in record and record['logo'] != None:
            for key, value in record['logo'].items():
              path = os.path.join(PATH_FILES, key)

              rs = {
                'refId': nd['id'],
                'ref': 'customer',
                'field': 'logo'
              }
              self.upload(path, rs)

          if 'files' in record and record['files'] != None:
            for key, value in record['files'].items():
              if not is_url_image(value):
                path = os.path.join(PATH_FILES, key)

                rs = {
                  'refId': nd['id'],
                  'ref': 'customer',
                  'field': 'files'
                }
                self.upload(path, rs)

          print(f"Customer fix {nd['id']} - {slug_site}")

    def fix_customer_articles(self, slug_site, data_file_json):
        data = data_file_json['articles']

        for article in data:

          if article['customer'] != "" or article['customer'] != None:

            url_entity = ENTITY_MAP.get(article['category'], None)

            if url_entity != None:

              exists = self.get(f'/{url_entity}', params={'slug': article['slug'], 'sites.uid': slug_site })

              if len(exists) == 0:
                continue

              r = exists[0]

              if r['customer'] != None:
                print('Ya tiene customer')
                continue

              customer = self.get('/customers', params={'_old_customer_id': article['customer'], 'sites.uid': slug_site})

              if len(customer) != 0:

                d = {
                  'id': customer[0]['id']
                }

                self.put(f"/{url_entity}/{r['id']}", data={'customer': d})


                print(f"Customer fix - {url_entity} - {r['id']} - {slug_site}")

    def fix_slug_articles(self, slug_site, data_file_json):
      for entity in ENTITIES_FIX_SITE_FIELD:
        url = f'/{entity}'
        entity_records = get_articles_entity(ENTITY_MODEL_MAP_INVERT.get(entity), data_file_json)
        records = self.get(url, params={'_limit': '-1', 'sites.uid': slug_site})

        for record in records:
          old_post = None
          for er in entity_records:
            if er['old_post_id'] == record['old_post_id']:
              old_post = er
              break


          if old_post != None:
            new_slug = old_post['slug']

            # Bucasmos en strapi si el articulo tiene el mismo slug que en wordpress
            exists = self.get(url, params={'slug': new_slug, 'sites.uid': slug_site})

            if len(exists) == 0:
              self.put(f'{url}/{record["id"]}', data={'slug': new_slug})

              print(f'{entity} fixed slug from {record["slug"]} to {new_slug}')

    def fix_relation_wheelsup(self, data_file_json):
      articles = data_file_json['articles']
      customers = data_file_json['customers']
      destinations = data_file_json['destinations']

      t_a = 0
      t_c = 0
      t_d = 0

      for article in articles:
        url_entity = ENTITY_MAP.get(article['category'], None)

        if url_entity != None:
          r = self.get(f'/{url_entity}', params={'old_post_id': article['old_post_id'], 'sites.uid': 'wheels-up-network-usa'})

          if len(r) == 0:
            continue

          id = r[0]['id']

          # Remove sites
          self.put(f'/{url_entity}/{id}', data={'sites': []})

          s = []

          if article['country_content'] == 'CA':
            s = [{'id':7 }]
          if article['country_content'] == 'US':
            s = [{'id': 1}]
          if article['country_content'] == 'CAUS':
            s = [{'id': 1}, {'id': 7}]

          # add new relation sites
          self.put(f'/{url_entity}/{id}', data={'sites': s})

          print(f"update field sites post {id}")
          t_a += 1

      for customer in customers:
        r = self.get(f'/customers', params={'slug': customer['slug'], 'sites.uid': 'wheels-up-network-usa'})

        if len(r) == 0:
          continue

        id = r[0]['id']

        # Remove sites
        self.put(f'/customers/{id}', data={'sites': []})

        s = []

        if customer['country_content'] == 'CA':
          s = [{'id':7 }]
        if customer['country_content'] == 'US':
          s = [{'id': 1}]
        if customer['country_content'] == 'CAUS':
          s = [{'id': 1}, {'id': 7}]

        # add new relation sites
        self.put(f'/customers/{id}', data={'sites': s})


        print(f"update field sites post {id}")
        t_c += 1

      for destination in destinations:
        r = self.get(f'/destinations', params={'slug': destination['slug'], 'sites.uid': 'wheels-up-network-usa'})

        if len(r) == 0:
          continue

        id = r[0]['id']

        # Remove sites
        self.put(f'/destinations/{id}', data={'sites': []})

        s = []

        if destination['country_content'] == 'CA':
          s = [{'id':7 }]
        if destination['country_content'] == 'US':
          s = [{'id': 1}]
        if destination['country_content'] == 'CAUS':
          s = [{'id': 1}, {'id': 7}]

        # add new relation sites
        self.put(f'/destinations/{id}', data={'sites': s})

        print(f"update field sites post {id}")
        t_d += 1


      print(f"total articles {len(articles)} - {t_a}")
      print(f"total customers {len(customers)} - {t_c}")
      print(f"total destinations {len(destinations)} - {t_d}")

    def fix_expiration_date(self, slug_site, data_file_json):
      articles = data_file_json['articles']

      for article in articles:
          url_entity = ENTITY_MAP.get(article['category'], None)

          if url_entity != None:
            s = slug_site

            if 'country_content' in article:
              if article['country_content'] == 'CA':
                s = "wheels-up-network-canada"
              if article['country_content'] == 'US':
                s = "wheels-up-network-usa"

            exists = self.get(f'/{url_entity}', params={'old_post_id': article['old_post_id'], 'sites.uid': s })

            if len(exists) == 0:
              continue

            r = exists[0]

            self.put(f"/{url_entity}/{r['id']}", data={'expiration_date': article['expiration_date']})

            print(f"expiration date fix {s} - {r['id']} - old {r['expiration_date']} - new {article['expiration_date']}")

    def fix_logo_customers(self, data_file_json):
      customers = data_file_json['customers']
      files_not_found = []

      for customer in customers:
        records = self.get('/customers', params={
          '_where[_or][0][sites.uid]': 'wheels-up-network-usa',
          '_where[_or][1][sites.uid]': 'wheels-up-network-canada',
          '_limit': '1',
          'old_customer_id': customer['old_customer_id'],
        })

        if len(records) > 0:
          record = records[0]
          if record['logo'] == None and type(customer['logo']) is dict:
            for k, v in customer['logo'].items():
              path = os.path.join(PATH_FILES, k)

              if os.path.exists(path) == False:
                files_not_found.append(path)
                continue

              rs = {
                'refId': record['id'],
                'ref': 'customer',
                'field': 'logo'
              }
              self.upload(path, rs)

              print(f"logo fix customer {record['id']}")
        else:
          continue

      with open(f"files_not_found_customers.json", 'w') as json_file:
        json.dump(files_not_found, json_file, indent=2)

    def add_data_uk(self, entity):
      site_uid = 'agents-connect'
      site_uid_wun = 'wheels-up-network-usa'

      if entity == 'fams':
        records = self.get('/fams', params={'sites.uid': site_uid_wun})

        for record in records:
          s = []
          for site in record.get('sites', []):
            s.append({'id': site['id']})

          # site id uk
          s.append({'id': 2})

          self.put(f'/fams/{record["id"]}', data={'sites': s})

          print(f'add site uk to fams {record["id"]}')

      if entity == 'destinations':
        records = self.get('/destinations', params={'sites.uid': site_uid_wun})

        for record in records:
          s = []
          for site in record.get('sites', []):
            s.append({'id': site['id']})

          # site id uk
          s.append({'id': 2})

          self.put(f'/destinations/{record["id"]}', data={'sites': s})

          print(f'add site uk to destinations {record["id"]}')

    def fix_old_url_uploads(self):
      customers = self.get('/customers', params={
        '_where[_or][0][sites.uid]': 'wheels-up-network-usa',
        '_where[_or][1][sites.uid]': 'wheels-up-network-canada',
        '_limit': '-1',
      })

      for customer in customers:
        http_url = 'http://wheelsupnetwork.com/wp-content/uploads/'
        https_url = 'https://wheelsupnetwork.com/wp-content/uploads/'
        admin_url = 'https://admin.globalagents.net/uploads/'

        content = customer['description']

        content = content.replace(http_url, admin_url)
        content = content.replace(https_url, admin_url)


        self.put(f'/customers/{customer["id"]}', data={
          'description': content
        })

        print(f'update content')

    def migrate_prizes(self):

      records = self.get('/prizes')

      ids_ignore = [77, 42, 43, 44]

      for record in records:
        if record['id'] in ids_ignore:
          print(f"ignoring existing record {record['id']}")
          continue

        new_record = record.copy()

        del new_record['id']

        if record['featured_image'] != None and 'id' in record.get('featured_image', {}):
          new_record['featured_image'] = {
            'id': record['featured_image']['id']
          }

        images = record.get('slider_images', [])
        ni = []
        for image in images:
          ni.append({'id': image['id']})
        new_record['slider_images'] = ni

        files = record.get('files', [])
        nf = []
        for file in files:
          nf.append({'id': file['id']})
        new_record['files'] = nf


        if record['author'] != None and 'id' in record.get('author', {}):
          new_record['author'] = {
            'id': record['author']['id']
          }

        if record['customer'] != None and 'id' in record.get('customer', {}):
          new_record['customer'] = {
            'id': record['customer']['id']
          }

        sites = record.get('sites', [])
        ns = []
        for site in sites:
          ns.append({'id': site['id']})
        new_record['sites'] = ns


        nr = self.post('/contests', data=new_record)

        print(f"migrated record -> prizes {record['id']} - contests {nr['id']}")

    def fix_images_in_files(self):
      for key, value in ENTITY_MAP.items():
        records = self.get(f'/{value}', params={'_limit': '-1'})

        for record in records:
          files = record.get('files', [])

          r = [] # list files
          found_images = 0

          for f in files:
            if is_name_image(f['name']):
              found_images += 1
            if 'name' in f and not is_name_image(f['name']):
              r.append({'id': f['id']})


          if len(r) > 0 or found_images > 0:
            self.put(f'/{value}/{record["id"]}', data={'files': r})

            print(f"Fix files entity {key} {record['id']}")

    def fill_display_title_customer(self):

      records = self.get('/customers', {"_limit": "-1"})

      for record in records:
        sites = record.get('sites', [])

        sites_uids = []

        for site in sites:
          sites_uids.append(site['uid'])

        t = '/'.join(sites_uids)
        label = f"{record['name']} - {t}"

        self.put(f'/customers/{record["id"]}', data={
          'display_title': label
        })

        print("update cusomter")

    def fill_field_vip(self):
      records = self.get('/customers', {'_limit': '-1'})
      count = 0
      for record in records:
        self.put(f"/customers/{record['id']}", data={
          'vip': False
        })

        print(f'updated field vip {count}/{len(records)}')
        count += 1

    def fill_slug_destination(self):
      records = self.get('/destinations', {'_limit': '-1'})
      count = 0

      for record in records:
        slug = slugify(record['name'])
        count = 0
        self.put(f'/destinations/{record["id"]}', data={
          'slug': slug
        })

        print(f'updated field slug {count}/{len(records)}')
        count += 1



strapi = Strapi()

strapi.login()

f = open(PATH_DATA)

data_json = json.load(f)

# strapi.fill_field_vip()
# strapi.fill_slug_destination()

# strapi.sync_articles(data_json)
# strapi.process_schema(SCHEMA, data_json)
# strapi.fix_slug_customer()
# strapi.sync_articles('solo-para-agentes-mx', data_json)
# strapi.sync_existing_articles('solo-para-agentes-com')



# for e in ENTITIES_FIX_SITE_FIELD:
#   print(f"Fixing {e}")
#   strapi.fix_relation_site(e)

# strapi.sync_existing_articles('solo-para-agentes-com')

# strapi.fix_customer_files('solo-para-agentes-co', data_json)

# strapi.fix_customer_articles('agents-connect', data_json)

for entity in ['destinations']:
  strapi.sync_entity(entity, 'wheels-up-network-usa', data_json)

# strapi.sync_articles('wheels-up-network-usa', data_json)

# strapi.fix_customer_articles('agents-connect', data_json)
# strapi.fix_slug_articles('agents-connect', data_json)

#strapi.fix_expiration_date('wheels-up-network-usa', data_json)

# for entity, model in ENTITY_MODEL_MAP2.items():
#  strapi.fix_images(entity, model, data_json)

# strapi.fix_logo_customers(data_json)

# strapi.sync_articles(data_json)

# strapi.fix_old_url_uploads()

# strapi.fix_images_in_files();
# strapi.fill_display_title_customer()
