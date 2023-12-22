import argparse
import requests

def check_urls(file_path, output_file=None):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    status_codes = {}
    errors = []

    for url in urls:
        try:
            response = requests.get(url, verify=False, allow_redirects=False)
            status_code = response.status_code

            if status_code not in status_codes:
                status_codes[status_code] = [url]
            else:
                status_codes[status_code].append(url)

            print(f"URL: {url} - Status Code: {status_code}")
        except Exception as e:
            print(f"URL: {url} - Error: {str(e)}")
            errors.append(f"URL: {url} - Error: {str(e)}")
            

    if output_file:
        with open(output_file, 'w') as out_file:
            for code, url_list in sorted(status_codes.items()):
                out_file.write(f"Status code {code}:\n")
                out_file.write("\n".join(url_list) + "\n\n")
            if errors:
                out_file.write("Errors: \n")
                for line in errors:
                    out_file.write("%s\n" % line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check URLs and display their status codes.")
    parser.add_argument("-i", "--input_file", help="Path to the file containing a list of URLs.")
    parser.add_argument("-o", "--output_file", help="Path to the output file.")

    args = parser.parse_args()

    check_urls(args.input_file, args.output_file)
