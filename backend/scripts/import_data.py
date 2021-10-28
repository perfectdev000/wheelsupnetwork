"""
    Module Imports
"""
import os
import re
import sys
import json
import mariadb
import re
import mimetypes
import requests
import copy
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ENV = 'prod'

# Information to connet
if ENV == 'dev':
    USER = "root"
    PASSWORD = "canaima"
    HOST = "127.0.0.1"
    PORT = 3306
else:
    USER =  os.environ.get("DATABASE_USER_MYSQL","wheelsup")
    PASSWORD = os.environ.get("DATABASE_PASSWORD_MYSQL", "")
    HOST = os.environ.get("DATABASE_HOST_MYSQL", "0.0.0.0")
    PORT = 3306

# wheelsup_wordpress, soloagentes_com, soloagentes_mx, spagentesco,
# agents-connect
DATABASE = "soloagentes_com"

DIR_UPLOADS = 'uploads'
DOWNLOAD_FILES = True

DIR_OUTPUT_JSON_DATA = ''

# Local variables
GENERATE_GLOBAL = True
DATA_GLOBAL = {}
DATA_ARTICLES = {}
CATEGORIES_RELATION = {}
SITES_RELATION = {}
CATEGORIES = []
SITES = []
ARTICLES = []
CUSTOMERS = []
DESTINATIONS = []
JOBS = []
AUTHORS = []

DATA_FILES = {}

ALL_CATEGORIES_DB = (
    'promotions',
    'prizes',
    'partner-programs',
    'webinars',
    'eventos',
    'specials',
    'industry',
    'news',
    'destinations',
    'empleos',
    'marketing',
    'evergreen',
    'fams',
    'contest',
)

SITES_LIST = [
    # {
    #     "dbname": 'soloagentes_com',
    #     "old_url": 'http://www.soloparaagentes.com',
    #     "new_url": 'https://admin.globalagents.net',
    #     "uid": "solo-para-agentes-com",
    # },
    {
        "dbname": 'wheelsup_wordpress',
        "old_url": 'https://wheelsupnetwork.com',
        "new_url": 'https://admin.globalagents.net',
        "uid": "wheels-up-network",
    },
    # {
    #     "dbname": 'agents-connect',
    #     "old_url": 'http://www.agents-connect.com',
    #     "new_url": 'https://admin.globalagents.net',
    #     "uid": "agents-connect",
    # },
    # {
    #     "dbname": 'soloagentes_mx',
    #     "old_url": 'http://www.soloparaagentes.mx',
    #     "new_url": 'https://admin.globalagents.net',
    #     "uid": "solo-para-agentes-mx",
    # },
    # {
    #     "dbname": 'spagentesco',
    #     "old_url": 'http://www.soloparaagentes.co',
    #     "new_url": 'https://admin.globalagents.net',
    #     "uid": "solo-para-agentes-co",
    # },
    # {
    #     "dbname": 'soloagentes_mx',
    #     "old_url": 'http://www.soloparaagentes.mx',
    #     "new_url": 'https://admin.globalagents.net',
    #     "uid": "solo-para-agentes-ar",
    # },
]

SITES_RELATION.update({
    'wheelsupnetwork': 1, 'agents-connect': 2, 'soloagentes_mx': 3,
    'soloagentes_com': 4, 'spagentesco': 5
})

MAP_SUPPLIER = {
    # 'eventos',
    # 'prizes',
    'promotions': 'incentive_supplier',
    'partner-programs': 'commission_supplier',
    'webinars': 'webinar_supplier',
    'specials': 'special_supplier',
    'industry': 'industry_supplier',
    'news': 'news_supplier',
    'evergreen': 'evergreen_supplier',
    'fams': 'fams_supplier',
    'contest': 'contest_supplier',
}

if GENERATE_GLOBAL:
    # Set Sites

    # Json Sites
    SITES = [
        {
            "name": "Wheels Up Network",
            "uid": "wheels-up-network",
            "url": "",
            "defaultSeo": {
                "metaTitle": "WheelsUpNetwork | Where the travel industry " +
                "earns, learns, & saves",
                "metaDescription": "WheelsUpNetwork is a one-stop shop " +
                "for all there is to know about the travel industry. You " +
                "can find the most up-to-date travel agent incentives, FAM " +
                "trips, sales tools & resources, webinars, travel agent " +
                "rates and more.",
                "shareImage": []
            },
            "favicon": []
        },
        {
            "name": "Agents Connect",
            "uid": "agents-connect",
            "url": "",
            "defaultSeo": {
                "metaTitle": "Agents Connect | Where the travel industry " +
                "earns, learns, & saves",
                "metaDescription": "Agents Connect is a one-stop shop for " +
                "all there is to know about the travel industry. You can " +
                "find the most up-to-date travel agent incentives, FAM " +
                "trips, sales tools & resources, webinars, travel agent " +
                "rates and more.",
                "shareImage": []
            },
            "favicon": []
        },
        {
            "name": "SoloParaAgentes México",
            "uid": "solo-para-agentes-mx",
            "url": "",
            "defaultSeo": {
                "metaTitle": "Solo Para Agentes | México",
                "metaDescription": "",
                "shareImage": []
            },
            "favicon": []
        },
        {
            "name": "SoloParaAgentes España",
            "uid": "solo-para-agentes-com",
            "url": "",
            "defaultSeo": {
                "metaTitle": "Solo Para Agentes | España",
                "metaDescription": "",
                "shareImage": []
            },
            "favicon": []
        },
        {
            "name": "SoloParaAgentes Colombia",
            "uid": "solo-para-agentes-co",
            "url": "",
            "defaultSeo": {
                "metaTitle": "Solo Para Agentes | Colombia",
                "metaDescription": "",
                "shareImage": []
            },
            "favicon": []
        }
    ]

    # Set Categories
    CATEGORIES_LIST = (
        'promotions',
        'prizes',
        'partner-programs',
        'webinars',
        'eventos',
        'specials',
        'industry',
        'news',
        'evergreen',
        'fams',
        'contest',
    )
    i = 1

    # Json Categories
    for category in ALL_CATEGORIES_DB:
        CATEGORIES.append({'name': category, 'slug': category})
        CATEGORIES_RELATION.update({category: i})
        i += 1

    # Json Authors
    AUTHORS = [
        {
            'name': 'Admin Editor',
            'email': 'admin@editor.com',
            'picture': []
        }
    ]

    DATA_GLOBAL.update({
        'categories': CATEGORIES,
        'sites': SITES,
        'authors': AUTHORS
    })
    with open('global.json', 'w') as json_file:
        json.dump(DATA_GLOBAL, json_file, indent=2)
    print('global.json generated successfully')

def replace_shortcodes(post_content):
  if post_content != None:
    return re.sub(r'\[[^\]]+\]', '', post_content)
  return ''

def valid_extension(text):
    return '.pdf' in text or\
        '.doc' in text or\
        '.docx' in text or\
        '.xls' in text or\
        '.xlsx' in text

def is_url_image(url):
    mimetype, encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

def get_urls_post(content):
    urls = []
    if content is not None:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)

    # remove duplicates
    urls = list(set(urls))

    urls = [url for url in urls if is_url_image(url) or valid_extension(url)]

    return urls

def parse_urls_wp_upload(urls, base_url_site):
    data = {}

    #TODO: lacoste desesperacion
    base_url = base_url_site.split("://").pop()
    base_http = f'http://{base_url}'
    base_https = f'https://{base_url}'

    wpUploadBase1 = base_http + "/wp-content/uploads/"
    wpUploadBase2 = base_https + "/wp-content/uploads/"

    for url in urls:
        if len(url) >= len(wpUploadBase1) and url[0: len(wpUploadBase1)] == wpUploadBase1:
            localImage = url[len(wpUploadBase1):]
            data[localImage] = url
        if len(url) >= len(wpUploadBase2) and url[0: len(wpUploadBase2)] == wpUploadBase2:
            localImage = url[len(wpUploadBase2):]
            data[localImage] = url
    return data

def fix_old_urls(content, old_url, new_url):
  nc = content

  if content != None:
    # replace url wp-content/uploads
    o_url_wp_content = old_url + '/wp-content/uploads'
    n_url_wp_content = new_url + '/uploads'

    nc = nc.replace(o_url_wp_content, n_url_wp_content)

    # replace other urls
    nc = nc.replace(old_url, new_url)

  return nc

def get_metadata(cursor, meta_key, post_id):
    QUERY = """
        SELECT
            meta_value
        FROM wp_postmeta
        WHERE meta_key = '{}' AND post_id = {} """.format(meta_key, post_id)
    cursor.execute(QUERY)

    result = cursor.fetchone()

    return result[0] if result is not None else None

# Connect to MariaDB Platform
for record in SITES_LIST:
    db = record['dbname']
    print('DB:' + db)
    ARTICLES.clear()
    CUSTOMERS.clear()
    DESTINATIONS.clear()
    JOBS.clear()
    DATA_ARTICLES.clear()

    try:
        CONN = mariadb.connect(user=USER, password=PASSWORD, host=HOST,
                               port=PORT, database=db)
    except mariadb.Error as error:
        print(f"Error connecting to MariaDB Platform: {error}")
        sys.exit(1)

    print("CONNECTED TO DB: " + db)
    # Get Cursor
    CUR = CONN.cursor()

    # Get Data
    QUERY = """SELECT wpost.id, wpost.post_content, wpost.post_title,
       wpost.post_name, wpost.post_date, wpost.post_type, wpost.post_excerpt,
       wpost.post_status, (SELECT guid FROM wp_posts wpost2 WHERE id IN
       (SELECT meta_value FROM wp_postmeta wmeta WHERE
       wmeta.post_id = wpost.id AND meta_key='_thumbnail_id')) as
       featured_image FROM wp_posts wpost WHERE post_type IN {0}  GROUP BY wpost.post_name
       ORDER BY wpost.post_date asc;""".format(ALL_CATEGORIES_DB)

    #  QUERY = """SELECT wpost.id, wpost.post_content, wpost.post_title,
    #  wpost.post_name, wpost.post_date, wpost.post_type, wpost.post_excerpt,
    #  wpost.post_status, (SELECT guid FROM wp_posts wpost2 WHERE id IN
    #  (SELECT meta_value FROM wp_postmeta wmeta WHERE
    #  wmeta.post_id = wpost.id AND meta_key='_thumbnail_id')) as
    #  featured_image FROM wp_posts wpost WHERE post_type = 'news' AND
    #  post_status='publish' GROUP BY wpost.post_name
    #  ORDER BY wpost.post_date desc, wpost.id LIMIT 50;"""
    CUR.execute(QUERY)

    results = CUR.fetchall()

    print('Articles count: %s' % len(results))

    isWheelsup = db == 'wheelsup_wordpress';

    # Fetch articles
    for (post_id, post_content, post_title, post_name, post_date, post_type,
         post_excerpt, post_status, featured_image) in results:
        urls = get_urls_post(post_content)

        rc = replace_shortcodes(post_content)
        clean_content = fix_old_urls(rc, record['old_url'], record['new_url'])

        if featured_image is not None:
            urls.append(featured_image)
        d = {}
        fi = {}

        if len(urls) != 0:
            d = parse_urls_wp_upload(urls, record['old_url'])
            DATA_FILES.update(d)

        if featured_image is not None:
            fi = parse_urls_wp_upload([featured_image], record['old_url'])

        # fetch attachments
        QUERY = """SELECT guid FROM wp_posts WHERE post_type = "attachment" AND post_parent = {} ORDER BY ID, post_mime_type""".format(post_id)
        CUR.execute(QUERY)

        attach_results = CUR.fetchall()

        urls_attach = [guid[0] for guid in attach_results]

        if len(urls_attach) != 0:
            temp = parse_urls_wp_upload(urls_attach, record['old_url'])
            d.update(temp)
            DATA_FILES.update(temp)

        # replace featured image
        if isWheelsup and len(urls_attach) != 0 and len(fi) == 0:
          fi = parse_urls_wp_upload([urls_attach[0]], record['old_url'])

        # Validate if wheelsup database
        country_content = None
        if isWheelsup:
          country_content = get_metadata(CUR, 'country_content', post_id)

        type_contest = None
        if isWheelsup and post_type == 'contest':
          type_contest = get_metadata(CUR, 'contest_winner_post', post_id)

        if post_type in ('destinations', 'marketing'):
            sppf = get_metadata(CUR, 'supplier_featured', post_id) == 'yes'

            # get expiration date
            expiration = get_metadata(CUR, '_expiration-date', post_id)

            if expiration != None:
                expiration = datetime.fromtimestamp(int(expiration))

            data_p = {
                'name': post_title,
                'slug': post_name,
                'description': clean_content,
                'excerpt': post_excerpt,
                'featured': sppf,
                'sites': record['uid'],
                'files': d,
                'logo': fi,
                'status': 'published' if post_status == 'publish' else 'draft',
                'published_date': str(post_date),
                'expiration_date':  str(expiration) if expiration != None else None,
            }

            if isWheelsup:
              data_p['country_content'] = country_content

            if post_type == 'destinations':
                DESTINATIONS.append(data_p)

            if post_type == 'marketing':
                data_p['old_customer_id'] = post_id
                CUSTOMERS.append(data_p)

        if post_type == 'empleos':
            oferta = get_metadata(CUR, 'oferta', post_id)
            city = get_metadata(CUR, 'ciudad', post_id)
            link = get_metadata(CUR, 'link', post_id)
            company = get_metadata(CUR, 'empresa', post_id)

            # get expiration date
            expiration = get_metadata(CUR, '_expiration-date', post_id)

            if expiration != None:
                expiration = datetime.fromtimestamp(int(expiration))

            data_j = {
                'name': post_title,
                'description': oferta,
                'city': city,
                'link': link,
                'company': company,
                'sites': record['uid'],
                'slug': post_name,
                'status': 'published' if post_status == 'publish' else 'draft',
                'published_date': str(post_date),
                'expiration_date':  str(expiration) if expiration != None else None,
            }

            if isWheelsup:
              data_j['country_content'] = country_content

            JOBS.append(data_j)

        if post_type in CATEGORIES_LIST:
            customer = None
            expiration = None
            link_partner = None

            # get customer
            customer = get_metadata(CUR, 'incentive_supplier', post_id)

            # get customer
            if post_type in MAP_SUPPLIER:
                customer = get_metadata(CUR, MAP_SUPPLIER.get(post_type), post_id)

            # get expiration date
            expiration = get_metadata(CUR, '_expiration-date', post_id)

            if expiration != None:
                expiration = datetime.fromtimestamp(int(expiration))

            if post_type == 'partner-programs':
              link_partner = get_metadata(CUR, 'commission_website', post_id)

            data_aa = {
                'old_post_id': post_id,
                'title': post_title,
                'content': clean_content,
                'publishedDate': str(post_date),
                'expiration_date':  str(expiration) if expiration != None else None,
                'status': 'published' if post_status == 'publish' else 'draft',
                'slug': post_name,
                # Esto se reemplaza en la importacion de strapi
                # por un modelo relacional
                'category': post_type,
                'author': {'id': 1},
                # Esto se reemplaza en la importacion de strapi
                # por un modelo relacional
                'sites': record['uid'],
                'description': post_excerpt,
                'featured_image': fi,
                'slider_images': [],
                'files': d,
                # Esto se reemplaza en la importacion de strapi
                # por un modelo relacional
                'customer': customer,
                # for partner-programs
                'link': link_partner,
            }

            if isWheelsup:
              data_aa['country_content'] = country_content

              if post_type == 'contest':
                data_aa['type'] = type_contest

            ARTICLES.append(data_aa)

    DATA_ARTICLES.update({
        'articles': ARTICLES,
        'customers': CUSTOMERS,
        'destinations': DESTINATIONS,
        'jobs': JOBS,
    })

    # Close Connection
    CONN.close()

    with open(f"{db}.json", 'w') as json_file:
        json.dump(DATA_ARTICLES, json_file, indent=2)
    print(f"File {db}.json generated")

    with open(f"{db}_files.json", 'w') as json_file:
        json.dump(DATA_FILES, json_file, indent=2)
    print(f"File {db}_files.json generated")


# Download all files
if DOWNLOAD_FILES:
    for local_file, url in DATA_FILES.items():
        localPath = os.path.join(DIR_UPLOADS, local_file)
        if not os.path.exists(localPath):
            os.makedirs(os.path.dirname(localPath), exist_ok= True)
            try:
                print("Downloading - %s" % url)
                r = requests.get(url)

                with open(localPath, 'wb') as f:
                    f.write(r.content)
            except Exception as e:
                print(e)
                print("Error downloading - %s" % url)

# for local_file, url in DATA_FILES.items():
#   localPath = os.path.join(DIR_UPLOADS, local_file)
#   if not os.path.exists(localPath):
#       os.makedirs(os.path.dirname(localPath), exist_ok= True)
#   try:
#       u = url.replace('http://www.soloparaagentes.mx', 'https://wun-mx.josesalinero.dev')
#       print("Downloading - %s" % u)
#       r = requests.get(u)

#       if r.status_code == 200:
#         with open(localPath, 'wb') as f:
#             f.write(r.content)
#       else:
#         print("File not found")
#   except Exception as e:
#       print(e)
#       print("Error downloading - %s" % url)

