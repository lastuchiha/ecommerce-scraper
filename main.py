import argparse
from flipkart import Flipkart


def main(args):
    urls = []
    if args.url:
        urls = [args.url]

    else:
        with open(args.file, 'r') as f:
            urls = f.readlines()

    results = []
    for i, url in enumerate(urls):
        result = Flipkart(url).get_details(args.include_additional)
        print('Obtained details of product..(%d)' % (i+1))
        results.append(result)

    print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Ecommerce webscrapper')

    parser.add_argument('-url', '--url', help='Url of the website')
    parser.add_argument(
        '-f', '--file', help='file name that contain urls in separate lines')
    parser.add_argument('-a', '--include_additional',
                        help='includes additional product details', action='store_true')

    args = parser.parse_args()
    if args.file and args.url:
        print('Only one of -f or -url can be provided.')

    elif args.file is None and args.url is None:
        print('Either -f or -url must be provided.')
    else:
        main(args)
