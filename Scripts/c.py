import argparse

parser = argparse.ArgumentParser(description='Process some options.')

# Agrega los argumentos para url, dir y vhost
parser.add_argument('--url', '-u', metavar='URL', type=str, help='URL option')
parser.add_argument('--dir', '-d', metavar='DIR', type=str, help='Directory option')
parser.add_argument('--subd', '-s', metavar='SUBDOMAINS', type=str, help='Subdomains option')

args = parser.parse_args()

# Verifica qué opción se proporcionó y haz algo con esa información
if args.url:
    print(f'URL specified: {args.url}')
    # Aquí puedes realizar acciones relacionadas con la opción --url
elif args.dir:
    print(f'Directory specified: {args.dir}')
    # Aquí puedes realizar acciones relacionadas con la opción --dir
elif args.subd:
    print(f'Virtual host specified: {args.vhost}')
    # Aquí puedes realizar acciones relacionadas con la opción --vhost
else:
    print('No option specified. Please provide one of --url, --dir, or --subd.')
