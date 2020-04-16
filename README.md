# Springer Downloader

Thanks Springer!

## Setup

```terminal
$ poetry install
```

## Run

Before executing script, edit following sction of `main.py`

```python
PACKAGE_NAMES = [
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
]
```

```terminal
$ poetry run python3 main.py
```
