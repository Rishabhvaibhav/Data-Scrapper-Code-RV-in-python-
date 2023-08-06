from bs4 import BeautifulSoup

def extract_phone_numbers_with_name(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')

    phone_numbers_with_name = []

    candidate_elements = soup.select('div.candidate-headline')
    for element in candidate_elements:
        name = element.select_one('span').text.strip()
        phone_element = element.find_next('div', class_='phone')
        if phone_element:
            phone_number = phone_element.select_one('div.number').text.strip().split()[0]
            phone_numbers_with_name.append((name, phone_number))

    return phone_numbers_with_name

# Replace 'your_file_path.html' with the actual path to your HTML file
file_path = 'D:\\demo\\Resdex_data_naukari_from_inspect.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_code = file.read()

phone_numbers_with_name = extract_phone_numbers_with_name(html_code)
for name, number in phone_numbers_with_name:
    print(f"{name} : {number}")
