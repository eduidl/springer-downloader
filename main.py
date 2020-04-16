from pathlib import Path
from time import sleep
from typing import List

import pandas as pd  # type: ignore
import requests
from tqdm import tqdm  # type: ignore

ROOT = Path(__file__).parent.resolve()
DOWNLOADS = ROOT / 'downloads'
DOWNLOADS.mkdir(exist_ok=True)

PACKAGE_NAMES: List[str] = [
    # 'Behavioral Science',
    # 'Behavioral Science and Psychology',
    # 'Biomedical and Life Sciences',
    # 'Business and Economics',
    # 'Business and Management',
    # 'Chemistry and Materials Science',
    'Computer Science',
    # 'Earth and Environmental Science',
    # 'Economics and Finance',
    # 'Education',
    # 'Energy',
    'Engineering',
    # 'Humanities, Social Sciences and Law',
    'Intelligent Technologies and Robotics',
    # 'Law and Criminology',
    # 'Literature, Cultural and Media Studies',
    'Mathematics and Statistics',
    # 'Medicine',
    # 'Physics and Astronomy',
    # 'Religion and Philosophy',
    # 'Social Sciences'
]  # yapf: disable


def get_output_stem(title: str, author: str) -> str:

    def escape_invalid_char(string: str) -> str:
        replaces = [(',', '-'), ('.', ''), ('/', ' '), (':', ' ')]
        out = string
        for from_, to in replaces:
            out = out.replace(from_, to)
        return out

    return f"{escape_invalid_char(title)}-{escape_invalid_char(author)}"


def download(url: str, out: Path) -> None:
    file_ = requests.get(url, allow_redirects=True)
    with out.open('wb') as f:
        f.write(file_.content)

    sleep(3)


def main() -> None:
    df = pd.read_csv(ROOT / 'list.csv')
    df = df[df['English Package Name'].isin(PACKAGE_NAMES)]
    keys = ['OpenURL', 'Book Title', 'Author', 'English Package Name']
    for url, title, author, package_name in tqdm(df[keys].values):
        package_dir = DOWNLOADS / package_name
        package_dir.mkdir(exist_ok=True)

        req_url = requests.get(url).url
        output_stem = get_output_stem(title, author)

        # PDF
        pdf_out_path = package_dir / f'{output_stem}.pdf'
        if not pdf_out_path.exists():
            pdf_url = req_url.replace('/book/', '/content/pdf/') + '.pdf'
            download(pdf_url, pdf_out_path)

        # EPUB
        epub_out_path = package_dir / f'{output_stem}.epub'
        if not epub_out_path.exists():
            epub_url = req_url.replace('/book/', '/download/epub/') + '.epub'
            if requests.get(epub_url).status_code == 200:
                download(epub_url, epub_out_path)


if __name__ == '__main__':
    main()
