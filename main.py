from mock.utils import GetRandomChoice
from form_launcher.form_launch import GFormFiller


def main():
    print("Running your Python program...")

    gformFiller = GFormFiller(
        fname="answers",
        url="https://forms.gle/EbR4Tkd9hPEaYKwC8",
    )

    
    gformFiller.run()

    pass


if __name__ == "__main__":
    main()
