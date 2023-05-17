import segno


def mini_qr_code_maker(link: str) -> None:
    # makes the qr code using segno python library
    basic_qr_code = segno.make(link)
    # saves the qr code as a png in the project directory
    basic_qr_code.save("folder-to-save-in/title-you-want-to-save-mini-as.png")


def border_qr_code_maker(link: str) -> None:
    # makes the qr code using segno python library
    border_qr_code = segno.make(link)
    # add a border to the qr code by adding the border parameter
    border_qr_code.save("folder-to-save-in/title-you-want-to-save-border-as.png", border=5)


def large_qr_code_maker(link: str) -> None:
    # makes the qr code using segno python library
    large_qr_code = segno.make(link)
    # make a qr code larger by adding the scale parameter
    large_qr_code.save("folder-to-save-in/title-you-want-to-save-large-as.png",  scale=10)


def colorful_qr_code_maker(link: str) -> None:
    # makes the qr code using segno python library
    large_qr_code = segno.make(link)
    # change 'dark' portion of the qr code (the part that is scanned) by setting
    # a dark color to the dark parameter
    # change background of the qr code by setting a lighter color to the
    # light parameter (for a white/blank background, don't include this parameter)
    large_qr_code.save("folder-to-save-in/title-you-want-to-save-color-as.png", dark='darkblue', light='lightblue', scale=10)


def save_qr_code_as(link: str) -> None:
    # can save a qr code as .svg, .png, .eps, and .pdf
    save_as_qr_code = segno.make(link)
    save_as_qr_code.save("folder-to-save-in/title.png")
    save_as_qr_code.save("folder-to-save-in/title.svg")
    save_as_qr_code.save("folder-to-save-in/title.pdf")
    save_as_qr_code.save("folder-to-save-in/title.eps")


def main() -> None:
    mini_qr_code_maker("Insert Link Here")
    border_qr_code_maker("Insert Link Here")
    large_qr_code_maker("Insert Link Here")
    colorful_qr_code_maker("Insert Link Here")
    save_qr_code_as("Insert Link Here")


if __name__ == '__main__':
    main()
