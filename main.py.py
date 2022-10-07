import pdfplumber
from gtts import gTTS
from pathlib import Path
from art import tprint


def exist_file_check(file_path, language):
    """ Проверка на существование этого файла и на то, что он pdf """
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print(f"[+] Original file: {Path(file_path).name}")
        print(f"[+] Processing...")
        text = read_pdf(file_path)
        record_mp3(file_path=file_path, text=text, language=language)
    else:
        return "File not exists, check the file path!"


def read_pdf(file_path):
    """Читаем PDF файл"""
    with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
    text = "".join(pages)
    text = text.replace("\n", "")
    return text


def record_mp3(file_path, text, language="en"):
    """Запись в mp3 текст, полученный из pdf файла"""
    my_audio = gTTS(text=text, lang=language)
    file_name = Path(file_path).stem
    my_audio.save(f"{file_name}.mp3")
    return f"[+] {file_name}.mp3 saved successfully!\n Have a nice day!..."


def main():
    tprint('FROM PDF TO MP3', font='bulbhead')
    file_path = input('\nEnter a file path: ')
    language = input('choose the language, for example "en" or "ru": ')
    print(exist_file_check(file_path, language))


if __name__ == '__main__':
    main()
